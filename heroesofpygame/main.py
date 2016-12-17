import os
import sys
from pygame.locals import *
import pygame
from heroesofpygame.przegrana import Przegrana
from heroesofpygame import Pietro
from heroesofpygame.player import Player
from heroesofpygame.wiktor import Wiktor
from heroesofpygame.dominik import Dominik
from heroesofpygame.piotr import Piotr
from heroesofpygame.dawid import Dawid
from heroesofpygame.parter import Parter
from heroesofpygame.strzal import Strzal
from heroesofpygame.udp_broadcast_client_server import NetworkConnection
from heroesofpygame.szarancza import Szarancza

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("szkola_1_pietro")
srodek_ekranu = (650, 325)

########################### zmienne globalne

szerokosc_ekranu = 1300
wysokosc_ekranu = 650
screen = pygame.display.set_mode((szerokosc_ekranu, wysokosc_ekranu))
players = {  # lista mozliwych graczy
    "Wiktor":  Wiktor(),
    "Dominik":  Dominik(),
    "Dawid":  Dawid(),
    "Piotr":  Piotr(),
    }
remote_players = {}  # lista graczy zdalnych
active_player_name = sys.argv[1]
active_player = players[active_player_name]  # aktywny gracz
player1 = players["Wiktor"]
player2 = players["Dominik"]
player3 = players["Dawid"]
player4 = players["Piotr"]
parter = Parter()

aktywna_sala = parter.klasa_info  # wyswietlana sala na ktorej dzieje sie akcja
aktywna_sala.przeskaluj(1300, 650)
aktywna_sala.dodaj_kwiat()

lewy_dol = aktywna_sala.daj_naroznik(ktory='lewy-dolny')
pozycja_startowa = (lewy_dol[0]+10, lewy_dol[1] - 60)
aktywna_szarancza = Szarancza(pozycja_startowa)
aktywna_szarancza.start(aktywna_sala.daj_kwiat())

strzal = Strzal()
sound = pygame.mixer.Sound('dzwiek/fanfary.wav')
all_objects = None  # wszystkie obiekty ktore moga wchodzic w kolizje

stan_gry = "rozgrywka"  #mozliwe : "rozpoczecie", "rozgrywka", "przegrana", "wygrana", "zakonczenie"
stan_gry = "przegrana"
przegrana = Przegrana(szerokosc_ekranu, wysokosc_ekranu)

######################################## inicjalizacja

all_objects = aktywna_sala.walls()
for player_name in players:
    all_objects.append(players[player_name])
all_objects.append(strzal)


def is_game_finished(event):
    running = True
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    return running


def handle_remote_player(net_connection, active_player, players, remote_players):
    network_data = net_connection.receive()
    # x=363, y=231, name=Wiktor

    if network_data is not None:
        (pos, name, action) = Player.unpack_network_record(network_data)
        if name != active_player.__class__.__name__:
            # print "network: %s, %s, %s" % (pos, name, action)
            if action == 'move':
                if name not in remote_players:
                    joining_player = players[name]
                    remote_players[name] = joining_player
                moved_player = remote_players[name]
                moved_player.move_to(pos)
            elif action == 'join':
                joining_player = players[name]
                remote_players[name] = joining_player
            elif action == 'leave':
                leaving_player_name = name
                del remote_players[leaving_player_name]


def broadcast_active_player(active_player, net_connection, action='move', await_confirmation=False):
    if net_connection != None:
        network_record = active_player.serialize_for_network(action=action)
        net_connection.broadcast(data=network_record, await_confirmation=await_confirmation)


def move_player_using_keyboard(key_left, key_right, key_up, key_down, active_player, all_objects, net_connection):
    key = pygame.key.get_pressed()
    if key[key_left]:
        active_player.move(-1, 0, all_objects)
    elif key[key_right]:
        active_player.move(1, 0, all_objects)
    elif key[key_up]:
        active_player.move(0, -1, all_objects)
    elif key[key_down]:
        active_player.move(0, 1, all_objects)
    else:
        return  # no move
    broadcast_active_player(active_player, net_connection)


def draw_remote(screen, remote_players):
    for player in remote_players.values():
        player.draw(screen)


def sprawdz_strzal(strzal, x, y):
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        strzal.ustaw_pozycje(x, y)
        strzal.start()
        return True
    return False


def muzyka_pod_przyciskiem():
    key = pygame.key.get_pressed()
    muza = pygame.mixer.Sound('dzwiek/dzwiek_walki/dzwiek_porazki.wav')
    if key[pygame.K_b]:
        muza.play()


# ---------------------------- glowna petla zdarzen pygame
net_connection = NetworkConnection(active_player.nazwa)
active_player.move_to(srodek_ekranu)
# broadcast_active_player(active_player, net_connection, action='join', await_confirmation=True)

running = True

while running:

    clock.tick(60)

    for event in pygame.event.get():

        running = is_game_finished(event)

        ################################### Akcje na planszy gry

        if stan_gry == "rozgrywka":  #mozliwe : "rozpoczecie", "rozgrywka", "przegrana", "wygrana", "zakonczenie"
            handle_remote_player(net_connection, active_player, players, remote_players)

            # Move the player if an arrow key is pressed
            move_player_using_keyboard(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, active_player, all_objects, net_connection)
            move_player_using_keyboard(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, player2, all_objects, None)
            move_player_using_keyboard(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k, player3, all_objects, None)
            move_player_using_keyboard(pygame.K_f, pygame.K_h, pygame.K_t, pygame.K_g, player4, all_objects, None)

            czy_strzela = sprawdz_strzal(strzal, x=active_player.rect.x, y=active_player.rect.y)
            if czy_strzela:
                active_player.zmien_humor("angry")

            aktywna_szarancza.update_pozycji_i_kolizji(all_objects)
            muzyka_pod_przyciskiem()
        elif stan_gry == "wygrana":
            pass
        elif stan_gry == "przegrana":
            decyzja = przegrana.grac_ponownie(event)
            if decyzja is None:
                pass  # nic nie robie, brak decyzji
            elif decyzja == "TAK":
                stan_gry = "rozgrywka"
            else:
                stan_gry = "zakonczenie"
                running = False
                break


        ################################### Rysowanie planszy gry

        screen.fill((0, 0, 0))
        if stan_gry == "rozgrywka":  #mozliwe : "rozpoczecie", "rozgrywka", "przegrana", "wygrana", "zakonczenie"
            # parter.draw(screen)     # rysujemy go tylko w trybie "podglad mapy"
            aktywna_sala.draw(screen)
            # flower_1.draw(screen)   # to ma sie narysowac w sali
            # flower_2.draw(screen)
            active_player.draw(screen)
            draw_remote(screen, remote_players)
            # player1.draw(screen)
            # player2.draw(screen)
            # player3.draw(screen)
            # player4.draw(screen)
            aktywna_szarancza.draw(screen)
            strzal.draw(screen)
        elif stan_gry == "wygrana":
            pass
        elif stan_gry == "przegrana":
            przegrana.draw(screen)

        pygame.display.flip()

#broadcast_active_player(active_player, net_connection, action='leave')
