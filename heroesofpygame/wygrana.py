# -*- coding: UTF-8 -*-
import pygame
from heroesofpygame.okno_wyboru import OknoWyboru


class Wygrana(OknoWyboru):
    def __init__(self, szerokosc, wysokosc):
        super(Wygrana, self).__init__(szerokosc, wysokosc, u"Zwycięstwo :-)")

    def on_entry(self):
        super(Wygrana, self).on_entry()

    def on_exit(self):
        super(Wygrana, self).on_exit()

    def on_clock_tick(self):
        return "wygrana"

    def on_event(self, event):
        decyzja = self.grac_ponownie(event)
        if decyzja == "TAK":
            return "rozgrywka"
        elif decyzja == "NIE":
            return "zakonczenie"
        return "wygrana"

    def draw(self, screen):
        screen.fill((0, 0, 0))
        super(Wygrana, self).draw(screen)
