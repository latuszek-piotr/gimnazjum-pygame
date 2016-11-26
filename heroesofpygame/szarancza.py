import pygame
import os
from player import Player


class Szarancza(Player):
    lot1 = os.path.join('grafika', 'szarancza', 'szarancza_lot1.png')
    lot2 = os.path.join('grafika', 'szarancza', 'szarancza_lot2.png')
    lot3 = os.path.join('grafika', 'szarancza', 'szarancza_lot3.png')
    stoi = os.path.join('grafika', 'szarancza', 'szarancza_stoi.png')


    def __init__(self, pos=(440, 120), size=50):
        super(Szarancza, self).__init__(pos, size)
        self.mood = 'happy'
        self.img = pygame.transform.scale(pygame.image.load(Szarancza.lot1).convert_alpha(), (size, size+10))

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])
