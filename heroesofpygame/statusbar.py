import pygame
import random
import os
import time
from heroesofpygame.wall import NewWall
from heroesofpygame.flower import Flower


class Status(object):
    def __init__(self):
        self.ile_kwiatow = 0
        self.ile_szaranczy = 0
        self.zjedzone_kwiaty = 0
        self.zabite_szarancze = 0
        self.nazwa_aktualnej_sali = ''
        self.active_player_name = ''


__status = None


def daj_status():
    global __status
    if __status is None:
        __status = Status()
    return __status


def resetuj_wynik(ile_kwiatow, ile_szaranczy):
    global __status
    __status = Status()
    __status.ile_kwiatow = ile_kwiatow
    __status.ile_szaranczy = ile_szaranczy


class StatusBar(object):
    szarancza = os.path.join('grafika', 'szarancza', 'szarancza_martwa_ikona.png')
    lot1 = os.path.join('grafika', 'szarancza', 'szarancza2_lot1.png')
    lot2 = os.path.join('grafika', 'szarancza', 'szarancza2_lot2.png')
    lot3 = os.path.join('grafika', 'szarancza', 'szarancza2_lot3.png')
    kwiat = os.path.join('grafika', 'status_flower.png')

    def __init__(self, pos, size=50, pionowy=True):
        self.pos = pos
        self.size = size
        self.rect = pygame.Rect(pos[0], pos[1], self.size[0], self.size[1])
        self.rect_lokalizacji = pygame.Rect(pos[0]+10, pos[1]+10, 300, self.size[1]-20)
        self.font = pygame.font.SysFont("comic sans MS", 15, bold=True)
        self.ile_kwiatow = daj_status().ile_kwiatow
        self.ile_szaranczy = daj_status().ile_szaranczy
        self.pionowy = pionowy
        rozmiar_obszaru = self.rect_lokalizacji.height / 1.7
        kwiat_start_pos = (self.rect_lokalizacji.right+20, self.rect_lokalizacji.top)
        self.obszary_kwiatow = self.oblicz_obszary_statusu(kwiat_start_pos, rozmiar_obszaru, self.ile_kwiatow, pionowy)
        if pionowy:
            bottomleft = self.obszary_kwiatow[-1].bottomleft
            szarancza_start_pos = (bottomleft[0], bottomleft[1] + 10)
        else:
            topright = self.obszary_kwiatow[-1].topright
            szarancza_start_pos = (self.rect_lokalizacji.right+20, self.rect_lokalizacji.top+self.rect_lokalizacji.height/2)
        self.obszary_szaranczy = self.oblicz_obszary_statusu(szarancza_start_pos, rozmiar_obszaru, self.ile_szaranczy, pionowy)
        self.szarancza_img = pygame.transform.scale(pygame.image.load(StatusBar.szarancza).convert_alpha(), (int(rozmiar_obszaru*1.9*0.4), int(rozmiar_obszaru*0.4)))
        self.szarancza_lot = [pygame.transform.scale(pygame.image.load(StatusBar.lot1).convert_alpha(), (int(rozmiar_obszaru*1.9*0.4), int(rozmiar_obszaru*0.4))),
                              pygame.transform.scale(pygame.image.load(StatusBar.lot2).convert_alpha(), (int(rozmiar_obszaru*1.9*0.4), int(rozmiar_obszaru*0.4))),
                              pygame.transform.scale(pygame.image.load(StatusBar.lot3).convert_alpha(), (int(rozmiar_obszaru*1.9*0.4), int(rozmiar_obszaru*0.4)))]
        self.czas_machniecia_skrzydel = 0.1
        self.start_time = time.time()
        self.kwiat_img = pygame.transform.scale(pygame.image.load(StatusBar.kwiat).convert_alpha(), (int(rozmiar_obszaru*0.8), int(rozmiar_obszaru*0.8)))

    def oblicz_obszary_statusu(self, start_pos, wielkosc_obszaru, ile_obszarow, pionowy=True):
        (x_start, y_start) = start_pos
        obszary = []
        for nr_obszaru in range(ile_obszarow):
            if pionowy:
                x = x_start
                y = y_start + nr_obszaru*wielkosc_obszaru
            else:
                x = x_start + nr_obszaru*wielkosc_obszaru
                y = y_start
            obszary.append(pygame.Rect(x, y, wielkosc_obszaru, wielkosc_obszaru))
        return obszary

    def draw_obszary(self, screen, obszary):
        for rect in obszary:
            pygame.draw.lines(screen, (255, 255, 255), True, [rect.topleft, rect.bottomleft, rect.bottomright, rect.topright], 2)

    def draw_lokalizacja(self, screen):
        text_lokalizacji = daj_status().nazwa_aktualnej_sali
        if text_lokalizacji:
            pygame.draw.rect(screen, (80,80,80), self.rect_lokalizacji)
            rect = self.rect_lokalizacji.copy()
            for grubosc in range(3):
                pygame.draw.lines(screen, (200,200,200), False, [rect.bottomleft, rect.bottomright, rect.topright], 1)
                pygame.draw.lines(screen, (20,20,20), False, [rect.bottomleft, rect.topleft, rect.topright], 2)
                rect.inflate_ip(-2,-2)
            text = self.font.render(text_lokalizacji, False, (255,255,0))
            (width, height) = self.font.size(text_lokalizacji)
            pozycja_napisu = (self.rect_lokalizacji.centerx - width/2, self.rect_lokalizacji.centery - height/2)
            screen.blit(text, pozycja_napisu)

    def draw_kwiaty(self, screen):
        # self.draw_obszary(screen, self.obszary_kwiatow)
        for idx, rect in enumerate(self.obszary_kwiatow):
            dx = (rect.width - self.kwiat_img.get_width()) / 2
            dy = (rect.height - self.kwiat_img.get_height()) / 2
            img_pos = (rect.left+dx, rect.top+dy)
            screen.blit(self.kwiat_img, img_pos)
            if idx < daj_status().zjedzone_kwiaty:
                img_rect = self.kwiat_img.get_rect().move(img_pos)
                pygame.draw.lines(screen, (255,0,0), False, [img_rect.topleft, img_rect.bottomright], 4)
                pygame.draw.lines(screen, (255,0,0), False, [img_rect.bottomleft, img_rect.topright], 4)

    def ktory_obraz(self):
        now = time.time()
        time_delta = now - self.start_time
        ile_machniec = int(time_delta / self.czas_machniecia_skrzydel)
        ktora_pozycja_lotu = ile_machniec % 3
        return ktora_pozycja_lotu

    def draw_szarancza(self, screen):
        # self.draw_obszary(screen, self.obszary_szaranczy)
        for idx, rect in enumerate(self.obszary_szaranczy):
            dx = (rect.width - self.szarancza_img.get_width()) / 2
            dy = (rect.height - self.szarancza_img.get_height()) / 2
            img_pos = (rect.left+dx, rect.top+dy)
            if idx < daj_status().zabite_szarancze:
                screen.blit(self.szarancza_img, img_pos)
            else:
                image_index = self.ktory_obraz()
                image_index = (image_index + idx) % 3
                image = self.szarancza_lot[image_index]
                screen.blit(image, img_pos)

    def draw(self, screen):
        pygame.draw.rect(screen, (80,80,80), self.rect)
        self.draw_lokalizacja(screen)
        self.draw_kwiaty(screen)
        self.draw_szarancza(screen)
