import pygame
import os
import time
from player import Player


class Szarancza(Player):
    lot1 = os.path.join('grafika', 'szarancza', 'szarancza_lot1.png')
    lot2 = os.path.join('grafika', 'szarancza', 'szarancza_lot2.png')
    lot3 = os.path.join('grafika', 'szarancza', 'szarancza_lot3.png')
    stoi = os.path.join('grafika', 'szarancza', 'szarancza_stoi.png')


    def __init__(self, pos=(440, 120), size=70):
        size_do_kolizji = size - 30  # rect kolizji jest mniejszy od rect obrazka
        super(Szarancza, self).__init__(pos, size_do_kolizji)
        self.mood = 'happy'
        szarancza_stojaca = pygame.transform.scale(pygame.image.load(Szarancza.stoi).convert_alpha(), (int(size*1.9), size))
        self.images = [
                       (pygame.transform.scale(pygame.image.load(Szarancza.lot1).convert_alpha(), (int(size*2.0), int(size*1.8))), (size*0.1, -size*0.6)),
                       (pygame.transform.scale(pygame.image.load(Szarancza.lot2).convert_alpha(), (int(size*2.0), size)), (0, 0)),
                       (pygame.transform.scale(pygame.image.load(Szarancza.lot3).convert_alpha(), (int(size*1.9), int(size*1.3))), (0, 0)),
                       (szarancza_stojaca, (0, 0)),
                       (pygame.transform.flip(szarancza_stojaca, False, True), (0, 0)),
                      ]
        # self.images[3][0] = pygame.transform.flip(self.images[3][0], False, True)
        self.dzwiek_zjadania = pygame.mixer.Sound('dzwiek/dzwiek_walki/szarancza_zjada_kwiat.wav')
        self.start_time = None
        self.czas_dojscia = 10
        self.czas_machniecia_skrzydel = 0.1
        self.odleglosc_do_kwiatu = {'deltaX':0, 'deltaY':0}
        self.kwiat_docelowy = None
        self.stan = "lecaca"  # mozliwe wartosci: "lecaca", "stojaca", "martwa", "anihilowana"

    def start(self, kwiat):
        if kwiat is None:
            return
        self.kwiat_docelowy = kwiat
        self.start_time = time.time()
        self.start_pos = self.pos
        self.odleglosc_do_kwiatu = self.wylicz_odleglosc(self.rect.center, kwiat.rect.midright)

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
                self.stan = "stojaca"

        if time_delta > self.czas_dojscia + 2:
            self.stan = "martwa"

        if time_delta > self.czas_dojscia + 5:
            self.stan = "anihilowana"
        return self.pos

    def ktory_obraz(self):
        if self.stan == "stojaca":
            return 3  # Szarancza.stoi
        elif self.stan == "martwa":
            return 4  # odwrocona Szarancza.stoi
        # if self.start_time is None:
        #     return 3  # Szarancza.stoi
        now = time.time()
        time_delta = now - self.start_time
        ile_machniec = int(time_delta / self.czas_machniecia_skrzydel)
        ktora_pozycja_lotu = ile_machniec % 3
        return ktora_pozycja_lotu

    def draw(self, screen):
        if self.stan == "anihilowana":
            return
        # Copy image to screen:
        self.biezaca_pozycja()
        image_index = self.ktory_obraz()
        (image, (delta_x, delta_y)) = self.images[image_index]
        pos = (self.pos[0] - delta_x, self.pos[1] + delta_y)
        screen.blit(image, [pos[0], pos[1]])
