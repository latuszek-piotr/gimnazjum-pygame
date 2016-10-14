import os
import random
import pygame
import sys

from heroesofpygame.player import Player
from heroesofpygame.wall import Wall
from heroesofpygame.flat import Flat, flat_1_data

from heroesofpygame.wiktor import Wiktor
from heroesofpygame.dominik import Dominik
from heroesofpygame.piotr import Piotr
from heroesofpygame.dawid import Dawid

from heroesofpygame.udp_broadcast_client_server import NetworkConnection

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

pygame.display.set_caption("szkola_1_pietro")
screen = pygame.display.set_mode((1300, 650))

net_connection = NetworkConnection()
players = {
    "Wiktor":  Wiktor(),
    "Dominik":  Dominik(),
    "Dawid":  Dawid(),
    "Piotr":  Piotr(),
    }
active_player_name = sys.argv[1]
active_player = players[active_player_name]
player1 = players["Wiktor"]
player2 = players["Dominik"]
player3 = players["Dawid"]
player4 = players["Piotr"]

flat1 = Flat(flat_1_data)

all_objects = flat1.walls
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

def move_remote_player(net_connection, active_player, players):
    network_data = net_connection.receive()
    # x=363, y=231, name=Wiktor

    if network_data is not None:
        parts = network_data.split(',')
        #print parts
        x = int(parts[0].split('=')[1])
        y = int(parts[1].split('=')[1])
        name = parts[2].split('=')[1]
        if name != active_player.__class__.__name__:
            moved_player = players[name]
            moved_player.rect.x = x
            moved_player.rect.y = y

def move_player_using_keyboard(key_left, key_right, key_up, key_down, active_player, all_objects, net_connection):
    key = pygame.key.get_pressed()
    nowa_pozycja = None
    if key[key_left]:
        nowa_pozycja = active_player.move(-1, 0, all_objects)
    if key[key_right]:
        nowa_pozycja = active_player.move(1, 0, all_objects)
    if key[key_up]:
        nowa_pozycja = active_player.move(0, -1, all_objects)
    if key[key_down]:
        nowa_pozycja = active_player.move(0, 1, all_objects)
    if (net_connection != None) and (nowa_pozycja != None):
        net_connection.broadcast(data=nowa_pozycja)

# ---------------------------- glowna petla zdarzen pygame

running = True
while running:

    clock.tick(60)

    running = is_game_finished()
    # move_remote_player(net_connection, active_player, players)

    # Move the player if an arrow key is pressed
    move_player_using_keyboard(pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, active_player, all_objects, net_connection)
    move_player_using_keyboard(pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s, player2, all_objects, None)
    move_player_using_keyboard(pygame.K_j, pygame.K_l, pygame.K_i, pygame.K_k, player3, all_objects, None)
    move_player_using_keyboard(pygame.K_f, pygame.K_h, pygame.K_t, pygame.K_g, player4, all_objects, None)

    # Draw the scenea
    screen.fill((0, 0, 0))
    flat1.draw(screen)

    active_player.draw(screen)
    player2.draw(screen)
    player3.draw(screen)
    player4.draw(screen)

    pygame.display.flip()
