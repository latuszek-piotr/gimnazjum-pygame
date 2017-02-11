import pygame
from pixel import Pixel


class Door(Pixel):
    def __init__(self, rect, color=(255, 255, 255)):
        self.color = color
        self.kolor_drzwi_zamknietych = (130, 130, 130)
        self.rect = rect
        self.rect_def = rect.copy()  # definicja rect w momencie utworzenia drzwi
        self.sala_1 = None
        self.sala_2 = None

    def sa_pionowe(self):
        if self.rect_def.width < self.rect_def.height:
            return True
        return False

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

    def draw(self, screen):
        if (self.sala_1 is None) or (self.sala_2 is None):
            pygame.draw.rect(screen, self.kolor_drzwi_zamknietych, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
