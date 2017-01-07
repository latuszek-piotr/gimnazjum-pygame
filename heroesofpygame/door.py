import pygame
from pixel import Pixel


class Door(Pixel):
    def __init__(self, rect, color=(255, 0, 0)):
        self.color = color
        self.rect = rect
        self.rect_def = rect.copy()  # definicja rect w momencie utworzenia drzwi
        self.sala_1 = None
        self.sala_2 = None

    def ustaw_w_sali(self, sala):
        if (self.sala_1 is None) and (self.sala_2 is None):
            self.sala_1 = sala
        elif (self.sala_1 is not None) and (self.sala_2 is None):
            self.sala_2 = sala
        elif (self.sala_2 is not None) and (self.sala_1 is None):
            self.sala_1 = sala

    def ustaw_miedzy_salami(self, sala_1, sala_2):
        self.sala_1 = sala_1
        self.sala_2 = sala_2

    def daj_sale_sasiednia(self, sala):
        if self.sala_1 == sala:
            return self.sala_2
        else:
            return self.sala_1
