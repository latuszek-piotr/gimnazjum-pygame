import os
import random
import pygame

from heroesofpygame.player import Player
from heroesofpygame.wall import Wall
from heroesofpygame.flat import Flat, flat_1_data
from heroesofpygame.wiktor import Wiktor
from heroesofpygame.dominik import Dominik

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()

pygame.display.set_caption("szkola_1_pietro")
screen = pygame.display.set_mode((1300, 650))

player1 = Player(color=(255, 200, 0)) # Create the player
player2 = Player(color=(255, 0, 200)) # Create the player
player3 = Player(color=(0, 255 ,0 )) # Create the player
player1 = Wiktor()
player2 = Dominik()


flat1 = Flat(flat_1_data)

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
        player1.move(-2, 0, flat1.walls)
    if key[pygame.K_RIGHT]:
        player1.move(2, 0, flat1.walls)
    if key[pygame.K_UP]:
        player1.move(0, -2, flat1.walls)
    if key[pygame.K_DOWN]:
        player1.move(0, 2, flat1.walls)

    if key[pygame.K_a]:
        player2.move(-2, 0, flat1.walls)
    if key[pygame.K_d]:
        player2.move(2, 0, flat1.walls)
    if key[pygame.K_w]:
        player2.move(0, -2, flat1.walls)
    if key[pygame.K_s]:
        player2.move(0, 2, flat1.walls)

    if key[pygame.K_j]:
        player3.move(-2, 0, flat1.walls)
    if key[pygame.K_l]:
        player3.move(2, 0, flat1.walls)
    if key[pygame.K_i]:
        player3.move(0, -2, flat1.walls)
    if key[pygame.K_k]:
        player3.move(0, 2, flat1.walls)




    # # Just added this to make it slightly fun ;)
    # if player.rect.colliderect(end_rect):
    #     raise SystemExit,sound.play()
    #     print "You win Wiktor!"
    # if player1.rect.colliderect(end_rect):
    #     raise SystemExit, "You win piotrek!"
    # if player2.rect.colliderect(end_rect):
    #     raise SystemExit, "You win! "

    # Draw the scenea
    screen.fill((0, 0, 0))
    flat1.draw(screen)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    player1.draw(screen)
    # pygame.draw.rect(screen, (255, 0, 0), end_rect)
    player2.draw(screen)
    player3.draw(screen)

    pygame.display.flip()
