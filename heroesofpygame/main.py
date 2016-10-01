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

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

pygame.display.set_caption("szkola_1_pietro")
screen = pygame.display.set_mode((1300, 650))

player1 = Wiktor()
player2 = Dominik()
player3 = Dawid()
player4 = Piotr()

flat1 = Flat(flat_1_data)

all_objects = flat1.walls
all_objects.append(player1)
all_objects.append(player2)
all_objects.append(player3)
all_objects.append(player4)

running = True
while running:

    clock.tick(60)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
            running = False

    # Move the player if an arrow key is pressed
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        player1.move(-1, 0, all_objects)
    if key[pygame.K_RIGHT]:
        player1.move(1, 0, all_objects)
    if key[pygame.K_UP]:
        player1.move(0, -1, all_objects)
    if key[pygame.K_DOWN]:
        player1.move(0, 1, all_objects)

    if key[pygame.K_a]:
        player2.move(-2, 0, all_objects)
    if key[pygame.K_d]:
        player2.move(2, 0, all_objects)
    if key[pygame.K_w]:
        player2.move(0, -2, all_objects)
    if key[pygame.K_s]:
        player2.move(0, 2, all_objects)

    if key[pygame.K_j]:
        player3.move(-2, 0, all_objects)
    if key[pygame.K_l]:
        player3.move(2, 0, all_objects)
    if key[pygame.K_i]:
        player3.move(0, -2, all_objects)
    if key[pygame.K_k]:
        player3.move(0, 2, all_objects)


    if key[pygame.K_f]:
        player4.move(-2, 0, all_objects)
    if key[pygame.K_h]:
        player4.move(2, 0, all_objects)
    if key[pygame.K_t]:
        player4.move(0, -2, all_objects)
    if key[pygame.K_g]:
        player4.move(0, 2, all_objects)


    # Draw the scenea
    screen.fill((0, 0, 0))
    flat1.draw(screen)

    player1.draw(screen)
    player2.draw(screen)
    player3.draw(screen)
    player4.draw(screen)

    pygame.display.flip()
