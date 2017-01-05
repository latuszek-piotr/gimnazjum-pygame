import pygame
from pixel import Pixel


class Door(Pixel):
    def __init__(self, pos, width, length, color=(255, 0, 0)):
        self.pos = pos
        self.width = width
        self.length = length
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], width, length)

    def ustaw_miedzy_salami(self, sala_1, sala_2):
        self.sala_1 = sala_1
        self.sala_2 = sala_2

    def daj_sale_sasiednia(self, sala):
        if self.sala_1 == sala:
            return self.sala_2
        else:
            return self.sala_1
