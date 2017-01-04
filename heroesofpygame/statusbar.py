import pygame
import random
import os
from heroesofpygame.wall import NewWall
from heroesofpygame.flower import Flower


class Wynik(object):
    def __init__(self):
        self.ile_kwiatow = 0
        self.ile_szaranczy = 0
        self.zjedzone_kwiaty = 0
        self.zabite_szarancze = 0


__wynik = None


def daj_wynik():
    global __wynik
    if __wynik is None:
        __wynik = Wynik()
    return __wynik


def resetuj_wynik(ile_kwiatow, ile_szaranczy):
    global __wynik
    __wynik = Wynik()
    __wynik.ile_kwiatow = ile_kwiatow
    __wynik.ile_szaranczy = ile_szaranczy


class StatusBar(object):
    szarancza = os.path.join('grafika', 'szarancza', 'szarancza_lot2.png')
    kwiat = os.path.join('grafika', 'status_flower.png')

    def __init__(self, pos, size=50, pionowy=True):
        self.pos = pos
        self.size = size
        self.ile_kwiatow = daj_wynik().ile_kwiatow
        self.ile_szaranczy = daj_wynik().ile_szaranczy
        self.pionowy = pionowy
        self.obszary_kwiatow = self.oblicz_obszary_statusu(pos, size, self.ile_kwiatow, pionowy)
        if pionowy:
            bottomleft = self.obszary_kwiatow[-1].bottomleft
            szarancza_start_pos = (bottomleft[0], bottomleft[1] + 10)
        else:
            topright = self.obszary_kwiatow[-1].topright
            szarancza_start_pos = (topright[0] + 10, topright[1])
        self.obszary_szaranczy = self.oblicz_obszary_statusu(szarancza_start_pos, size, self.ile_szaranczy, pionowy)
        self.szarancza_img = pygame.transform.scale(pygame.image.load(StatusBar.szarancza).convert_alpha(), (int(size*1.9*0.4), int(size*0.4)))
        self.kwiat_img = pygame.transform.scale(pygame.image.load(StatusBar.kwiat).convert_alpha(), (int(size*0.8), int(size*0.8)))

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
            pygame.draw.lines(screen, (255, 255, 255), False, [rect.topleft, rect.bottomleft, rect.bottomright, rect.topright, rect.topleft], 2)

    def draw(self, screen):
        self.draw_obszary(screen, self.obszary_kwiatow)
        for idx, rect in enumerate(self.obszary_kwiatow):
            dx = (rect.width - self.kwiat_img.get_width()) / 2
            dy = (rect.height - self.kwiat_img.get_height()) / 2
            img_pos = (rect.left+dx, rect.top+dy)
            screen.blit(self.kwiat_img, img_pos)
            if idx < daj_wynik().zjedzone_kwiaty:
                img_rect = self.kwiat_img.get_rect().move(img_pos)
                pygame.draw.lines(screen, (255,0,0), False, [img_rect.topleft, img_rect.bottomright], 4)
                pygame.draw.lines(screen, (255,0,0), False, [img_rect.bottomleft, img_rect.topright], 4)

        self.draw_obszary(screen, self.obszary_szaranczy)
        for idx, rect in enumerate(self.obszary_szaranczy):
            dx = (rect.width - self.szarancza_img.get_width()) / 2
            dy = (rect.height - self.szarancza_img.get_height()) / 2
            img_pos = (rect.left+dx, rect.top+dy)
            screen.blit(self.szarancza_img, img_pos)
            if idx < daj_wynik().zabite_szarancze:
                img_rect = self.szarancza_img.get_rect().move(img_pos)
                pygame.draw.lines(screen, (255,0,0), False, [img_rect.topleft, img_rect.bottomright], 4)
                pygame.draw.lines(screen, (255,0,0), False, [img_rect.bottomleft, img_rect.topright], 4)
