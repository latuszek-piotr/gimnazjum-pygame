import pygame
from heroesofpygame.okno_wyboru import OknoWyboru


class Wygrana(OknoWyboru):
    def __init__(self, szerokosc, wysokosc):
        super(Wygrana, self).__init__(szerokosc, wysokosc, "Zwyciestwo :-)")
