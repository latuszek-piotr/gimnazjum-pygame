import pygame
from heroesofpygame.okno_wyboru import OknoWyboru


class Przegrana(OknoWyboru):
    def __init__(self, szerokosc, wysokosc):
        super(Przegrana, self).__init__(szerokosc, wysokosc, "Przegrana ;-(")

    def on_entry(self):
        super(Przegrana, self).on_entry()

    def on_exit(self):
        super(Przegrana, self).on_exit()

    def on_clock_tick(self):
        return "przegrana"

    def on_event(self, event):
        return "przegrana"
