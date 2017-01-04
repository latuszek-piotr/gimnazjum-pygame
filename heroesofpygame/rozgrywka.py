import pygame
import random

from heroesofpygame.strzal import Strzal

from heroesofpygame.player import Player
from heroesofpygame.wiktor import Wiktor
from heroesofpygame.dominik import Dominik
from heroesofpygame.piotr import Piotr
from heroesofpygame.dawid import Dawid

from heroesofpygame.szarancza import Szarancza

from heroesofpygame.parter import Parter
from heroesofpygame.Pietro import Pietro

from heroesofpygame.udp_broadcast_client_server import NetworkConnection

from heroesofpygame.stan_gry import StanGry


class Rozgrywka(StanGry):
    def __init__(self, szerokosc, wysokosc, active_player_name):
        super(Rozgrywka, self).__init__()
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.strzal = Strzal()
        self.players = {  # lista mozliwych graczy
                        "Wiktor":  Wiktor(),
                        "Dominik":  Dominik(),
                        "Dawid":  Dawid(),
                        "Piotr":  Piotr(),
                       }
        self.active_player = self.players[active_player_name]
        self.net_connection = NetworkConnection(self.active_player.nazwa)
        # self.player1 = self.players["Wiktor"]
        # self.player2 = self.players["Dominik"]
        # self.player3 = self.players["Dawid"]
        # self.player4 = self.players["Piotr"]
        self.remote_players = {}  # lista graczy zdalnych
        self.parter = Parter()
        self.aktywna_sala = self.wylosuj_sale()
        self.aktywna_szarancza = None
        self.all_objects = self.obiekty_mogace_wchodzic_w_kolizje()

    def wylosuj_sale(self):
        sala = self.parter.klasa_info  # wyswietlana sala na ktorej dzieje sie akcja #TODO losowanie; teraz na sztywno
        return sala

    def obiekty_mogace_wchodzic_w_kolizje(self):
        all_objects = []
        for player_name in self.players:
            all_objects.append(self.players[player_name])
        all_objects.append(self.strzal)
        return all_objects

    def sprawdz_strzal(self, x, y, kierunek):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.strzal.direction = kierunek
            self.strzal.ustaw_pozycje(x, y)
            self.strzal.start()
            return True
        return False

    def move_player_using_keyboard(self, key_left, key_right, key_up, key_down, active_player, all_objects):
        key = pygame.key.get_pressed()
        if key[key_left]:
            # active_player.move(-1, 0, all_objects)
            self.active_player.zmien_humor("suprised")
            # katy rosna zgodnie ze wskazowkami zegara (odwrotnie niz w ukladzie kartezjanskim)
            # obrot w lewo zmniejsza kat
            active_player.direction -= 2
            active_player.move_at_direction(0, all_objects)
        elif key[key_right]:
            # active_player.move(1, 0, all_objects)
            self.active_player.zmien_humor("suprised")
            active_player.direction += 2
            active_player.move_at_direction(0, all_objects)
        elif key[key_up]:
            # active_player.move(0, -1, all_objects)
            self.active_player.zmien_humor("happy")
            active_player.move_at_direction(2, all_objects)
        elif key[key_down]:
            # active_player.move(0, 1, all_objects)
            self.active_player.zmien_humor("happy")
            active_player.move_at_direction(-2, all_objects)
        else:
            return  # no move
        self.broadcast_active_player(active_player)

    def broadcast_active_player(self, active_player, action='move', await_confirmation=False):
        if self.net_connection != None:
            network_record = active_player.serialize_for_network(action=action)
            self.net_connection.broadcast(data=network_record, await_confirmation=await_confirmation)

    def handle_remote_player(self):
        network_data = self.net_connection.receive()
        # x=363, y=231, name=Wiktor

        if network_data is not None:
            (pos, name, action) = Player.unpack_network_record(network_data)
            if name != self.active_player.__class__.__name__:
                # print "network: %s, %s, %s" % (pos, name, action)
                if action == 'move':
                    if name not in self.remote_players:
                        joining_player = self.players[name]
                        self.remote_players[name] = joining_player
                    moved_player = self.remote_players[name]
                    moved_player.move_to(pos)
                elif action == 'join':
                    joining_player = self.players[name]
                    self.remote_players[name] = joining_player
                elif action == 'leave':
                    leaving_player_name = name
                    del self.remote_players[leaving_player_name]

    def draw_remote(self, screen, remote_players):
        for player in remote_players.values():
            player.draw(screen)

    def wylosuj_pozycje_startowa_szaranczy(self, sala):
        (x_start, y_start) = sala.daj_naroznik(ktory='lewy-dolny')
        (x_end, y_end) = self.aktywna_sala.daj_naroznik(ktory='prawy-dolny')
        room_width = x_end - x_start
        przesuniecie = random.randint(10, room_width - 80)
        pozycja_startowa = (x_start+przesuniecie, y_start - 60)
        return pozycja_startowa

    def wylosuj_pozycje_startowa_gracza(self, sala):
        (x_start, y_start) = sala.daj_naroznik(ktory='lewy-gorny')
        (x_end, y_end) = sala.daj_naroznik(ktory='prawy-dolny')
        room_width = x_end - x_start
        przesuniecie = random.randint(10, room_width - 80)
        x = x_start + przesuniecie
        y = y_start + int((y_end - y_start) / 2)
        return (x, y)

    def on_entry(self):
        super(Rozgrywka, self).on_entry()
        self.aktywna_sala.przeskaluj(self.szerokosc, self.wysokosc)
        ilosc_kwiatow = random.randint(1, 3)
        ilosc_szaranczy = random.randint(1, 5)
        for nr in range(ilosc_kwiatow):
            self.aktywna_sala.dodaj_kwiat()
        pozycja_startowa_szaranczy = self.wylosuj_pozycje_startowa_szaranczy(self.aktywna_sala)
        self.aktywna_szarancza = Szarancza(pozycja_startowa_szaranczy)
        self.all_objects = self.obiekty_mogace_wchodzic_w_kolizje()
        self.all_objects.extend(self.aktywna_sala.walls())

        pozycja_startowa_gracza = self.wylosuj_pozycje_startowa_gracza(self.aktywna_sala)
        self.active_player.move_to(pozycja_startowa_gracza)
        self.active_player.mood = 'happy'
        self.active_player.direction = 0
        # self.broadcast_active_player(active_player, self.net_connection, action='join', await_confirmation=True)

        self.aktywna_szarancza.start(self.aktywna_sala.daj_losowy_kwiat())

    def on_exit(self):
        super(Rozgrywka, self).on_exit()

    def on_clock_tick(self):
        if self.aktywna_szarancza is None:  # TODO: dac do on_entry() stanu rozgrywka
            self.on_entry()

        self.handle_remote_player()

        # Move the player if an arrow key is pressed
        self.move_player_using_keyboard(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, self.active_player, self.all_objects)
        # rozgrywka.move_player_using_keyboard(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, player2, rozgrywka.all_objects)
        # rozgrywka.move_player_using_keyboard(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k, player3, rozgrywka.all_objects)
        # rozgrywka.move_player_using_keyboard(pygame.K_f, pygame.K_h, pygame.K_t, pygame.K_g, player4, rozgrywka.all_objects)

        czy_strzela = self.sprawdz_strzal(x=self.active_player.rect.centerx, y=self.active_player.rect.centery,
                                          kierunek=self.active_player.direction)
        if czy_strzela:
            self.active_player.zmien_humor("angry")

        wynik = self.aktywna_szarancza.update_pozycji_i_kolizji(self.all_objects)
        if wynik is None:
            pass  # nic nie robie, nic sie nie stalo
        elif wynik == "zjedzony_kwiat":
            self.aktywna_szarancza = None
            porazka_sound = pygame.mixer.Sound('dzwiek/dzwiek_walki/dzwiek_porazki.wav') # TODO: dac do on_exit() stanu rozgrywka
            porazka_sound.play()
            return "przegrana"
        elif wynik == "martwa_szarancza":
            self.aktywna_szarancza = None
            wygrana_sound = pygame.mixer.Sound('dzwiek/dzwiek_walki/dzwiek_sukcesu.wav')
            wygrana_sound.play()
            return "wygrana"

        return "rozgrywka"

    def on_event(self, event):
        return "rozgrywka"

    def draw(self, screen):
        screen.fill((0, 0, 0))
        # parter.draw(screen)     # rysujemy go tylko w trybie "podglad mapy"
        self.aktywna_sala.draw(screen)
        # # flower_1.draw(screen)   # to ma sie narysowac w sali
        # # flower_2.draw(screen)
        self.active_player.draw(screen)
        self.draw_remote(screen, self.remote_players)
        # # player1.draw(screen)
        # # player2.draw(screen)
        # # player3.draw(screen)
        # # player4.draw(screen)
        if self.aktywna_szarancza and self.aktywna_szarancza.is_started():
            self.aktywna_szarancza.draw(screen)
        self.strzal.draw(screen)
