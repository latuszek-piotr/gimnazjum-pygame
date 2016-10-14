import pygame
import os

class Flower(object):
    flower_img =  os.path.join('grafika', 'flower.png')

    def __init__(self, pos=(410, 300), size=50):
        self.img = pygame.transform.scale(pygame.image.load(Flower.flower_img).convert_alpha(), (size, size+10))
        self.pos = pos

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, self.pos)
