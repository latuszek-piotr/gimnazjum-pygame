import pygame
import os
from pixel import Pixel


class Dawid(Pixel):
    happy_img = os.path.join('grafika', 'dawid_wesoly.png')
    sad_img = os.path.join('grafika', 'dawid_smutny.png')
    angry_img = os.path.join('grafika', 'dawid_zly.png')
    surprised_img = os.path.join('grafika', 'dawid_zdziwiony.png')
    scared_img = os.path.join('grafika', 'dawid_prestraszony.png')

    def __init__(self, pos=(50, 50), size=4):
        super(Dawid, self).__init__(pos, size)
        self.mood = 'happy'
        self.img = pygame.transform.scale(pygame.image.load(Dawid.happy_img).convert_alpha(), (50, 60))

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])
