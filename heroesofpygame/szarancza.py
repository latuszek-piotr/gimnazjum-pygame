import pygame
import os
import time
from player import Player


class Szarancza(Player):
    lot1 = os.path.join('grafika', 'szarancza', 'szarancza_lot1.png')
    lot2 = os.path.join('grafika', 'szarancza', 'szarancza_lot2.png')
    lot3 = os.path.join('grafika', 'szarancza', 'szarancza_lot3.png')
    stoi = os.path.join('grafika', 'szarancza', 'szarancza_stoi.png')


    def __init__(self, pos=(440, 120), size=50):
        super(Szarancza, self).__init__(pos, size)
        self.mood = 'happy'
        self.img = pygame.transform.scale(pygame.image.load(Szarancza.lot1).convert_alpha(), (size, size+10))
        self.dzwiek_zjadania = pygame.mixer.Sound('dzwiek/dzwiek_walki/szarancza_zjada_kwiat.wav')
        self.start_time = None
        self.czas_dojscia = 10
        self.odleglosc_do_kwiatu = {'deltaX':0, 'deltaY':0}
        self.kwiat_docelowy = None

    def start(self, kwiat):
        if kwiat is None:
            return
        self.kwiat_docelowy = kwiat
        self.start_time = time.time()
        self.start_pos = self.pos
        self.odleglosc_do_kwiatu = self.wylicz_odleglosc(self.pos, kwiat.pos)

    def wylicz_odleglosc(self, pos_start, pos_koncowa):
        odleglosc = {'deltaX': pos_koncowa[0] - pos_start[0], 'deltaY': pos_koncowa[1] - pos_start[1]}
        return odleglosc

    def biezaca_pozycja(self):
        if self.start_time is None:
            return self.pos
        now = time.time()
        time_delta = now - self.start_time
        if time_delta < self.czas_dojscia:
            pos_x = (self.odleglosc_do_kwiatu['deltaX'] * time_delta / self.czas_dojscia) + self.start_pos[0]
            pos_y = (self.odleglosc_do_kwiatu['deltaY'] * time_delta / self.czas_dojscia) + self.start_pos[1]
            self.pos = (pos_x, pos_y)
            self.rect.x = pos_x
            self.rect.y = pos_y
            if self.collides(self.kwiat_docelowy):
                self.dzwiek_zjadania.play()
        return self.pos

    def draw(self, screen):
        # Copy image to screen:
        pos = self.biezaca_pozycja()
        screen.blit(self.img, [pos[0], pos[1]])
