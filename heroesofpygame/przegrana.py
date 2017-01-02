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
        decyzja = self.grac_ponownie(event)
        if decyzja == "TAK":
            return "rozgrywka"
        elif decyzja == "NIE":
            return "zakonczenie"
        return "przegrana"

    def draw(self, screen):
        screen.fill((0, 0, 0))
        super(Przegrana, self).draw(screen)
