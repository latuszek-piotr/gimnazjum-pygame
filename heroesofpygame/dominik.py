import pygame
import os
from player import Player


class Dominik(Player):
    happy_img = os.path.join('grafika', 'dominik_wesoly.png')
    sad_img = os.path.join('grafika', 'dominik_smutny.png')
    angry_img = os.path.join('grafika', 'dominik_zly.png')
    surprised_img = os.path.join('grafika', 'dominik_zdziwiony.png')
    scared_img = os.path.join('grafika', 'dominik_przestraszony.png')

    def __init__(self, pos=(380, 70), size=50):
        super(Dominik, self).__init__(pos, size)
        self.mood = 'sad'
        self.img = pygame.transform.scale(pygame.image.load(Dominik.sad_img).convert_alpha(), (size, size+10))

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])
