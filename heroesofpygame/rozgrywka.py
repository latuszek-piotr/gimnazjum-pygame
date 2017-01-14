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
from heroesofpygame.mapa import Mapa

from heroesofpygame.stan_gry import StanGry
from heroesofpygame import statusbar
from heroesofpygame.userevents import USEREVENT_PASS_DOOR


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
        # self.player1 = self.players["Wiktor"]
        # self.player2 = self.players["Dominik"]
        # self.player3 = self.players["Dawid"]
        # self.player4 = self.players["Piotr"]
        self.remote_players = {}  # lista graczy zdalnych
        self.parter = Parter()
        self.mapa = Mapa(self.parter.sale())
        self.podglad_mapy = False
        self.aktywna_sala = self.ustaw_sale_startowa()
        self.zaatakowane_sale = []
        self.aktywne_szarancze = []
        self.all_objects = self.obiekty_mogace_wchodzic_w_kolizje()
        self.wszystkie_kwiaty = []
        self.statusbar = None

    def wylosuj_sale_zaatakowane(self):
        sale_mozliwe_do_zaatakowania = self.parter.sale_do_losowania()
        max_ilosc_sal = len(sale_mozliwe_do_zaatakowania)
        ilosc_sal_zaatakowanych = random.randint(1, int(max_ilosc_sal*0.75))
        zaatakowane_sale = random.sample(sale_mozliwe_do_zaatakowania,  ilosc_sal_zaatakowanych)
        return zaatakowane_sale
    
    def ustaw_sale_startowa(self):
        '''wyswietlana sala na ktorej dzieje sie akcja'''
        sala = random.choice(self.parter.sale_do_losowania())
        # sala = self.parter.korytarz_szatni
        # sala = self.parter.korytarz_parteru
        sala = self.parter.hall_glowny  # wejscie glowne jest w hallu glownym
        sala = self.parter.hall_parteru  # wejscie glowne jest w hallu glownym
        # sala = self.parter.korytarz_parteru
        # sala = self.parter.sala_gimn
        return sala

    def przeskaluj_wszystkie_sale(self, szerokosc, wysokosc):
        for sala in self.parter.sale():
            sala.oblicz_rect_widoku(szerokosc, wysokosc)
            # sala.przeskaluj(szerokosc, wysokosc)

    def obiekty_mogace_wchodzic_w_kolizje(self):
        all_objects = []
        for player_name in self.players:
            all_objects.append(self.players[player_name])
        all_objects.append(self.strzal)
        all_objects.extend(self.aktywna_sala.walls())
        all_objects.extend(self.aktywna_sala.wszystkie_drzwi())
        return all_objects

    def sprawdz_strzal(self, x, y, kierunek):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.strzal.direction = kierunek
            self.strzal.ustaw_pozycje(x, y)
            self.strzal.start()
            return True
        return False

    def sprawdz_podglad_mapy(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_m]:
            self.podglad_mapy = True
        else:
            self.podglad_mapy = False

    def move_player_using_keyboard(self, key_left, key_right, key_up, key_down, active_player, all_objects):
        key = pygame.key.get_pressed()
        moved = True
        if key[key_left]:
            active_player.zmien_humor("suprised")
            # katy rosna zgodnie ze wskazowkami zegara (odwrotnie niz w ukladzie kartezjanskim)
            # obrot w lewo zmniejsza kat
            active_player.direction -= 2
            active_player.move_at_direction(0, all_objects)
        elif key[key_right]:
            active_player.zmien_humor("suprised")
            active_player.direction += 2
            active_player.move_at_direction(0, all_objects)
        elif key[key_up]:
            active_player.zmien_humor("happy")
            active_player.move_at_direction(2, all_objects)
        elif key[key_down]:
            active_player.zmien_humor("happy")
            active_player.move_at_direction(-2, all_objects)
        else:
            moved = False  # no move
        if moved:
            active_player.pos_teren = self.aktywna_sala.wylicz_pozycje_w_terenie(active_player.rect.center)

    def zainicjuj_kwiaty(self, sale):
        self.wszystkie_kwiaty = []
        for sala in sale:
            sala.usun_wszystkie_kwiaty()
            ilosc_kwiatow = random.randint(1, 3)
            for nr in range(ilosc_kwiatow):
                kwiat = sala.dodaj_kwiat()
                if kwiat:
                    self.wszystkie_kwiaty.append(kwiat)
        self.mapa.ustaw_ilosc_kwiatow(self.ilosc_wszystkich_kwiatow())
        for idx, kwiat in enumerate(self.wszystkie_kwiaty):
            self.mapa.update_pozycji_kwiatu(idx, kwiat, sala)

    def ilosc_wszystkich_kwiatow(self):
        return len(self.wszystkie_kwiaty)

    def ilosc_zjedzonych_kwiatow(self):
        zjedzone = [kwiat for kwiat in self.wszystkie_kwiaty if kwiat.zjedzony]
        return len(zjedzone)

    def reinicjuj_pojedyncza_szarancze(self, szarancza, sala):
        pozycja_startowa_szaranczy = sala.wylosuj_pozycje_startowa_szaranczy()
        szarancza.pos = pozycja_startowa_szaranczy
        szarancza.start(sala.daj_losowy_niezjedzony_kwiat())

    def zainicjuj_szarancze(self, sala):
        self.aktywne_szarancze = []
        ilosc_szaranczy = random.randint(1, 11)
        max_ilosc_sal = len(self.parter.sale_do_losowania())
        ilosc_sal_zaatakowanych = random.randint(1, int(max_ilosc_sal*0.75))
        zaatakowane_sale = random.sample([1, 2, 3, 4, 5],  3)
        if ilosc_szaranczy < ilosc_sal_zaatakowanych:
            ilosc_sal_zaatakowanych = ilosc_szaranczy
        for nr in range(ilosc_szaranczy):
            pozycja_startowa_szaranczy = sala.wylosuj_pozycje_startowa_szaranczy()
            szarancza = Szarancza(pozycja_startowa_szaranczy)
            szarancza.start(sala.daj_losowy_niezjedzony_kwiat())
            self.aktywne_szarancze.append(szarancza)
        self.mapa.ustaw_ilosc_szaranczy(self.ilosc_wszystkich_szaranczy())

    def ilosc_wszystkich_szaranczy(self):
        return len(self.aktywne_szarancze)

    def ilosc_zabitych_szaranczy(self):
        zabite = [szarancza for szarancza in self.aktywne_szarancze if (szarancza.stan == "martwa") or (szarancza.stan == "anihilowana")]
        return len(zabite)

    def szarancze_ktore_juz_zjadly_kwiat(self):
        najedzone = [szarancza for szarancza in self.aktywne_szarancze if (szarancza.stan == "stojaca")]
        return najedzone

    def zainicjuj_gracza(self, sala):
        active_player_name = statusbar.daj_status().active_player_name
        self.active_player = self.players[active_player_name]
        pozycja_startowa_gracza = sala.wylosuj_pozycje_startowa_gracza()
        self.active_player.move_to(pozycja_startowa_gracza)
        self.active_player.pos_teren = sala.wylicz_pozycje_w_terenie(pozycja_startowa_gracza)
        self.active_player.mood = 'happy'
        self.active_player.direction = 0
        self.mapa.ustaw_ilosc_graczy(ilosc_wszystkich_graczy=1)

    def zainicjuj_sale(self):
        self.zaatakowane_sale = self.wylosuj_sale_zaatakowane()
        self.aktywna_sala = self.ustaw_sale_startowa()
        self.przeskaluj_wszystkie_sale(self.szerokosc, self.wysokosc)
        self.aktywna_sala.przeskaluj(self.szerokosc, self.wysokosc)
        self.mapa.ustaw_aktywna_sale(self.aktywna_sala)

    def on_entry(self):
        super(Rozgrywka, self).on_entry()
        self.zainicjuj_sale()
        sale = self.zaatakowane_sale[:]
        sale.append(self.aktywna_sala)
        # sale = [self.aktywna_sala, self.parter.sekretariat]
        # sale = [self.aktywna_sala]
        self.zainicjuj_kwiaty(sale)
        self.zainicjuj_szarancze(self.aktywna_sala)
        self.zainicjuj_gracza(self.aktywna_sala)

        self.all_objects = self.obiekty_mogace_wchodzic_w_kolizje()

        statusbar.resetuj_wynik(self.ilosc_wszystkich_kwiatow(), self.ilosc_wszystkich_szaranczy())
        statusbar.daj_status().nazwa_aktualnej_sali = self.aktywna_sala.nazwa
        self.statusbar = statusbar.StatusBar(pos=(0,self.wysokosc+1), size=(self.szerokosc,70), pionowy=False)

    def on_exit(self):
        super(Rozgrywka, self).on_exit()
        statusbar.daj_status().nazwa_aktualnej_sali = ''

    def on_clock_tick(self):
        # Move the player if an arrow key is pressed
        self.move_player_using_keyboard(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, self.active_player, self.all_objects)
        # rozgrywka.move_player_using_keyboard(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, player2, rozgrywka.all_objects)
        # rozgrywka.move_player_using_keyboard(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k, player3, rozgrywka.all_objects)
        # rozgrywka.move_player_using_keyboard(pygame.K_f, pygame.K_h, pygame.K_t, pygame.K_g, player4, rozgrywka.all_objects)
        self.mapa.update_pozycji_gracza(idx_gracza=0, gracz=self.active_player)

        self.sprawdz_podglad_mapy()
        czy_strzela = self.sprawdz_strzal(x=self.active_player.rect.centerx, y=self.active_player.rect.centery,
                                          kierunek=self.active_player.direction)
        if czy_strzela:
            self.active_player.zmien_humor("angry")

        for idx, szarancza in enumerate(self.aktywne_szarancze):
            szarancza.update_pozycji_i_kolizji(self.all_objects)
            szarancza.pos_teren = self.aktywna_sala.wylicz_pozycje_w_terenie(szarancza.rect.center)
            self.mapa.update_pozycji_szaranczy(idx, szarancza)

        statusbar.daj_status().zjedzone_kwiaty = self.ilosc_zjedzonych_kwiatow()
        statusbar.daj_status().zabite_szarancze = self.ilosc_zabitych_szaranczy()

        if statusbar.daj_status().zjedzone_kwiaty >= self.ilosc_wszystkich_kwiatow():
            porazka_sound = pygame.mixer.Sound('dzwiek/dzwiek_walki/dzwiek_porazki.wav') # TODO: dac do on_exit() stanu rozgrywka
            porazka_sound.play()
            return "przegrana"
        elif statusbar.daj_status().zabite_szarancze >= self.ilosc_wszystkich_szaranczy():
            wygrana_sound = pygame.mixer.Sound('dzwiek/dzwiek_walki/dzwiek_sukcesu.wav')
            wygrana_sound.play()
            return "wygrana"

        for szarancza in self.szarancze_ktore_juz_zjadly_kwiat():
            self.reinicjuj_pojedyncza_szarancze(szarancza, self.aktywna_sala)

        return "rozgrywka"

    def wysun_gracza_za_drzwi(self, gracz, move_direction, drzwi):
        if move_direction == 'right': # Moving right; Hit the left side of drzwi
            gracz.rect.left = drzwi.rect.right + 2
            gracz.rect.top = drzwi.rect.top
            gracz.real_x = gracz.rect.x
            gracz.real_y = gracz.rect.y
        elif move_direction == 'left': # Moving left; Hit the right side of drzwi
            gracz.rect.right = drzwi.rect.left - 2
            gracz.rect.top = drzwi.rect.top
            gracz.real_x = gracz.rect.x
            gracz.real_y = gracz.rect.y
        elif move_direction == 'bottom': # Moving down; Hit the top side of drzwi
            gracz.rect.top = drzwi.rect.bottom + 2
            gracz.rect.left = drzwi.rect.left
            gracz.real_x = gracz.rect.x
            gracz.real_y = gracz.rect.y
        elif move_direction == 'top': # Moving up; Hit the bottom side of drzwi
            gracz.rect.bottom = drzwi.rect.top - 2
            gracz.rect.left = drzwi.rect.left
            gracz.real_x = gracz.rect.x
            gracz.real_y = gracz.rect.y

    def on_event(self, event):
        if event.type == USEREVENT_PASS_DOOR:
            door = event.door
            move_direction = event.move_direction
            if door.sala_1 and door.sala_2:
                sasiednia = door.daj_sale_sasiednia(self.aktywna_sala)
                self.aktywna_sala = sasiednia
                self.aktywna_sala.przeskaluj(self.szerokosc, self.wysokosc)
                self.wysun_gracza_za_drzwi(self.active_player, move_direction, door)
                self.mapa.ustaw_aktywna_sale(self.aktywna_sala)

                #TODO szarancze i kwiaty po zmianie sali

                self.all_objects = self.obiekty_mogace_wchodzic_w_kolizje()

                statusbar.daj_status().nazwa_aktualnej_sali = self.aktywna_sala.nazwa
        return "rozgrywka"

    def draw(self, screen):
        screen.fill((80,80,80))
        self.aktywna_sala.draw(screen)
        self.active_player.draw(screen)
        # # player1.draw(screen)
        # # player2.draw(screen)
        # # player3.draw(screen)
        # # player4.draw(screen)
        for szarancza in self.aktywne_szarancze:
            if szarancza.is_started():
                szarancza.draw(screen)
        self.strzal.draw(screen)
        if self.podglad_mapy:
            self.mapa.draw(screen)
        self.statusbar.draw(screen)
