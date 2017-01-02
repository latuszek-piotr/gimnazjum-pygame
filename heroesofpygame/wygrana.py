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
        return "wygrana"
