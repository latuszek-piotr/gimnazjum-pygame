import pygame
import os
from player import Player


class Piotr(Player):
    happy_img = os.path.join('grafika', 'piotr_wesoly.png')
    sad_img = os.path.join('grafika', 'piotr_smutny.png')
    angry_img = os.path.join('grafika', 'piotr_zly.png')
    surprised_img = os.path.join('grafika', 'piotr_zdziwiony.png')
    scared_img = os.path.join('grafika', 'piotr_przestraszony.png')

    def __init__(self, pos=(350, 50), size=50):
        super(Piotr, self).__init__(pos, size)
        self.mood = 'happy'
        self.img = pygame.transform.scale(pygame.image.load(Piotr.happy_img).convert_alpha(), (size, size+10))

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])
