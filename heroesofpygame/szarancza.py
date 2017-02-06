import pygame
import os
import time
import random
from player import Player
from strzal import Strzal


class Szarancza(Player):
    lot1 = os.path.join('grafika', 'szarancza', 'szarancza2_lot1.png')
    lot2 = os.path.join('grafika', 'szarancza', 'szarancza_lot2.png')
    lot3 = os.path.join('grafika', 'szarancza', 'szarancza2_lot3.png')
    stoi = os.path.join('grafika', 'szarancza', 'szarancza2_stoi.png')
    martwa = os.path.join('grafika', 'szarancza', 'szarancza_martwa.png')


    def __init__(self, pos=(440, 120), size=40):
        size_do_kolizji = size - 30  # rect kolizji jest mniejszy od rect obrazka
        super(Szarancza, self).__init__(pos, size_do_kolizji)
        self.mood = 'happy'
        szarancza_stojaca = pygame.transform.scale(pygame.image.load(Szarancza.stoi).convert_alpha(), (int(size*1.9), size))
        szarancza_martwa = pygame.transform.scale(pygame.image.load(Szarancza.martwa).convert_alpha(), (int(size*1.9), size))
        self.images = [
                       (pygame.transform.scale(pygame.image.load(Szarancza.lot1).convert_alpha(), (int(size*2.0), int(size*1.8))), (size*0.1, -size*0.6)),
                       (pygame.transform.scale(pygame.image.load(Szarancza.lot2).convert_alpha(), (int(size*2.0), size)), (0, 0)),
                       (pygame.transform.scale(pygame.image.load(Szarancza.lot3).convert_alpha(), (int(size*1.9), int(size*1.3))), (0, 0)),
                       (szarancza_stojaca, (0, 0)),
                       (szarancza_martwa, (0, 0)),
                      ]
        self.dzwiek_zjadania = pygame.mixer.Sound('dzwiek/dzwiek_walki/szarancza_zjada_kwiat.wav')
        self.start_time = None
        self.czas_dojscia = 10
        self.czas_machniecia_skrzydel = 0.1
        self.odleglosc_do_kwiatu = {'deltaX':0, 'deltaY':0}
        self.kwiat_docelowy = None
        self.stan = "oczekujaca"  # mozliwe wartosci: "oczekujaca", "lecaca", "stojaca", "martwa", "anihilowana"
        self.czas_trafienia = None

    def is_started(self):
        return self.start_time is not None

    def start(self, kwiat):
        if kwiat is None:
            return
        self.czas_dojscia = random.choice([8,10,12,14,16])
        self.kwiat_docelowy = kwiat
        self.start_time = time.time()
        self.start_pos = self.pos
        self.rect.topleft = self.start_pos
        self.odleglosc_do_kwiatu = self.wylicz_odleglosc(self.rect.center, kwiat.rect.midright)
        self.stan = "lecaca"

    def update_pozycji_i_kolizji(self, all_objects_thay_may_colide):
        if (self.stan == "anihilowana") or (self.stan == "oczekujaca"):
            return None
        if self.stan == "martwa":
            now = time.time()
            czas_od_trafienia = now - self.czas_trafienia
            if czas_od_trafienia > 2:
                self.stan = "anihilowana"
            return None
        self.biezaca_pozycja()
        if (self.stan != "stojaca"):
            if self.kwiat_docelowy.zjedzony:  # inna szarancza zjadla go wczesniej
                self.stan = "stojaca"
            elif self.collides(self.kwiat_docelowy):
                self.dzwiek_zjadania.play()
                self.kwiat_docelowy.zjedzony = True
                self.stan = "stojaca"
                return "zjedzony_kwiat"  # TODO opoznic by bylo widac ja stojaca
        for scene_object in all_objects_thay_may_colide:
            if scene_object is self:
                continue
            if self.collides(scene_object):
                if isinstance(scene_object, Strzal):
                    if scene_object.is_running():
                        self.stan = "martwa"
                        self.czas_trafienia = time.time()
                        return "martwa_szarancza"  # TODO opoznic by bylo widac ja odwrocona
        return None

    def wylicz_odleglosc(self, pos_start, pos_koncowa):
        odleglosc = {'deltaX': pos_koncowa[0] - pos_start[0], 'deltaY': pos_koncowa[1] - pos_start[1]}
        return odleglosc

    def biezaca_pozycja(self):
        if (self.start_time is None) or (self.stan != "lecaca"):
            return self.pos
        now = time.time()
        time_delta = now - self.start_time
        if time_delta < self.czas_dojscia / 1.0:
            pos_x = (self.odleglosc_do_kwiatu['deltaX'] * time_delta / self.czas_dojscia) + self.start_pos[0]
            pos_y = (self.odleglosc_do_kwiatu['deltaY'] * time_delta / self.czas_dojscia) + self.start_pos[1]
            self.pos = (pos_x, pos_y)
            self.rect.x = pos_x
            self.rect.y = pos_y
        #
        # if time_delta > self.czas_dojscia + 5:
        #     self.stan = "anihilowana"
        return self.pos

    def ktory_obraz(self):
        if (self.stan == "stojaca") or (self.stan == "oczekujaca"):
            return 3  # Szarancza.stoi
        elif self.stan == "martwa":
            return 4  # odwrocona Szarancza.stoi  # TODO zamienic na zweglona
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
        image_index = self.ktory_obraz()
        (image, (delta_x, delta_y)) = self.images[image_index]
        pos = (self.pos[0] - delta_x, self.pos[1] + delta_y)
        screen.blit(image, [pos[0], pos[1]])
