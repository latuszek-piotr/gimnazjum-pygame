import pygame
from heroesofpygame.okno_wyboru import OknoWyboru


class Przegrana(OknoWyboru):
    def __init__(self, szerokosc, wysokosc):
        super(Przegrana, self).__init__(szerokosc, wysokosc, "Przegrana ;-(")
