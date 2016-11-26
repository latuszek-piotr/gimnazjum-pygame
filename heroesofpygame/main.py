import os
import sys
from pygame.locals import *
import pygame

from heroesofpygame import Pietro
from heroesofpygame.player import Player
from heroesofpygame.wiktor import Wiktor
from heroesofpygame.dominik import Dominik
from heroesofpygame.piotr import Piotr
from heroesofpygame.dawid import Dawid
from heroesofpygame.parter import Parter
from heroesofpygame.strzal import Strzal
from heroesofpygame.udp_broadcast_client_server import NetworkConnection

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

pygame.display.set_caption("szkola_1_pietro")
screen = pygame.display.set_mode((1300, 650))
srodek_ekranu = (650, 325)

players = {
    "Wiktor":  Wiktor(),
    "Dominik":  Dominik(),
    "Dawid":  Dawid(),
    "Piotr":  Piotr(),
    }
remote_players = {}
active_player_name = sys.argv[1]
active_player = players[active_player_name]
player1 = players["Wiktor"]
player2 = players["Dominik"]
player3 = players["Dawid"]
player4 = players["Piotr"]
parter = Parter()

aktywna_sala = parter.osiem_a
aktywna_sala.przeskaluj(1300, 650)
aktywna_sala.dodaj_kwiat()

strzal = Strzal()
sound = pygame.mixer.Sound('dzwiek/ca_fire1.wav')
# all_objects = parter.walls()
all_objects = aktywna_sala.walls()
for player_name in players:
    all_objects.append(players[player_name])


def is_game_finished():
    running = True
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
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


def sprawdz_strzal(strzal):
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        strzal.start()


def muzyka_pod_przyciskiem():
    key = pygame.key.get_pressed()
    pygame.mixer.init()
    muza = pygame.mixer.Sound('dzwiek/dzwiek_walki/dzwiek_sukcesu.wav')
    if key[pygame.K_b]:
        muza.play()


# ---------------------------- glowna petla zdarzen pygame
net_connection = NetworkConnection(active_player.nazwa)
active_player.move_to(srodek_ekranu)
# broadcast_active_player(active_player, net_connection, action='join', await_confirmation=True)

running = True

while running:

    clock.tick(60)

    running = is_game_finished()
    handle_remote_player(net_connection, active_player, players, remote_players)

    # Move the player if an arrow key is pressed
    move_player_using_keyboard(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, active_player, all_objects, net_connection)
    move_player_using_keyboard(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, player2, all_objects, None)
    move_player_using_keyboard(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k, player3, all_objects, None)
    move_player_using_keyboard(pygame.K_f, pygame.K_h, pygame.K_t, pygame.K_g, player4, all_objects, None)

    sprawdz_strzal(strzal)
    muzyka_pod_przyciskiem()
    # Draw the scenea

    screen.fill((0, 0, 0))
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
    strzal.draw(screen)

    pygame.display.flip()

broadcast_active_player(active_player, net_connection, action='leave')
