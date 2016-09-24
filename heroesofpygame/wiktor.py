import pygame
import os
from pixel import Pixel


class Wiktor(Pixel):
    happy_img = os.path.join('grafika', 'wiktor_wesoly.png')

    def __init__(self, pos=(50, 50), size=4):
        super(Wiktor, self).__init__(pos, size)
        self.mood = 'sad'
        self.img = pygame.transform.scale(pygame.image.load(Wiktor.happy_img).convert_alpha(), (50, 60))

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])
