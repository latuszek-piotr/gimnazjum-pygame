import os
import random
import pygame

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
active_player = players["Wiktor"]

flat1 = Flat(flat_1_data)

all_objects = flat1.walls
for player_name in players:
    all_objects.append(players[player_name])

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

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

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        nowa_pozycja = active_player.move(-1, 0, all_objects)
        net_connection.broadcast(data=nowa_pozycja)
    if key[pygame.K_RIGHT]:
        nowa_pozycja = active_player.move(1, 0, all_objects)
        net_connection.broadcast(data=nowa_pozycja)
    if key[pygame.K_UP]:
        nowa_pozycja = active_player.move(0, -1, all_objects)
        net_connection.broadcast(data=nowa_pozycja)
    if key[pygame.K_DOWN]:
        nowa_pozycja = active_player.move(0, 1, all_objects)
        net_connection.broadcast(data=nowa_pozycja)

    # if key[pygame.K_a]:
    #     player2.move(-2, 0, all_objects)
    # if key[pygame.K_d]:
    #     player2.move(2, 0, all_objects)
    # if key[pygame.K_w]:
    #     player2.move(0, -2, all_objects)
    # if key[pygame.K_s]:
    #     player2.move(0, 2, all_objects)
    # 
    # if key[pygame.K_j]:
    #     player3.move(-2, 0, all_objects)
    # if key[pygame.K_l]:
    #     player3.move(2, 0, all_objects)
    # if key[pygame.K_i]:
    #     player3.move(0, -2, all_objects)
    # if key[pygame.K_k]:
    #     player3.move(0, 2, all_objects)
    # 
    # 
    # if key[pygame.K_f]:
    #     player4.move(-2, 0, all_objects)
    # if key[pygame.K_h]:
    #     player4.move(2, 0, all_objects)
    # if key[pygame.K_t]:
    #     player4.move(0, -2, all_objects)
    # if key[pygame.K_g]:
    #     player4.move(0, 2, all_objects)


    # Draw the scenea
    screen.fill((0, 0, 0))
    flat1.draw(screen)

    active_player.draw(screen)
    # player2.draw(screen)
    # player3.draw(screen)
    # player4.draw(screen)

    pygame.display.flip()
