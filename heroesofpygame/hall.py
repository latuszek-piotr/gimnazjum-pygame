# -*- coding: UTF-8 -*-
import pygame
import random
from heroesofpygame.wall import NewWall
from heroesofpygame.flower import Flower
from heroesofpygame.sala import ClassRoom

# self.korytarz_parteru = ClassRoom(nazwa="korytarz parteru", pos=(86,199), room_width=82, room_length=19)
# self.hall_glowny = ClassRoom(nazwa=u"hall główny parteru", pos=(168,135), room_width=67, room_length=120)

class Hall(ClassRoom):
    def __init__(self, hall_glowny, korytarz_do_sal):
        self.hall_glowny = hall_glowny
        self.korytarz_do_sal = korytarz_do_sal
        self.nazwa = "korytarz parteru"
        self.font = hall_glowny.font
        self.pos = (korytarz_do_sal.pos[0], hall_glowny.pos[1])
        self.room_width = hall_glowny.room_width + korytarz_do_sal.room_width
        self.room_length = hall_glowny.room_length
        self.wall_width = hall_glowny.wall_width
        self.skala_terenu = 10
        skala = self.skala_terenu
        self.teren = pygame.Rect(self.pos[0]*skala, self.pos[1]*skala, self.room_width*skala, self.room_length*skala) # wirtualne wspolrzedne na mapie calosci
        self.rect_widoku = None
        self.color = hall_glowny.color
        self.skala_widoku = 1.0
        self.polozenie_drzwi = []
        self.przelicz_sciany(self.pos, self.room_width, self.room_length)
        self.obszary_kwiatowe = {}  # slownik postaci {nr_oszaru: rect_obszaru}
        self.kwiaty = {}  # slownik postaci {nr_oszaru: obiekt_kwiat}
        self.left_top_hall_wall = None
        self.left_bottom_hall_wall = None

    def daj_obrys_sali(self, skala):
        obszar_hallu = pygame.Rect(self.hall_glowny.pos[0]*skala, self.hall_glowny.pos[1]*skala,
                                   self.hall_glowny.room_width*skala, self.hall_glowny.room_length*skala)
        obszar_korytarza = pygame.Rect(self.korytarz_do_sal.pos[0]*skala, self.korytarz_do_sal.pos[1]*skala,
                                       self.korytarz_do_sal.room_width*skala, self.korytarz_do_sal.room_length*skala)
        punkty_obrysu = [obszar_hallu.topleft,
                         obszar_korytarza.topright, obszar_korytarza.topleft, obszar_korytarza.bottomleft, obszar_korytarza.bottomright,
                         obszar_hallu.bottomleft, obszar_hallu.bottomright, obszar_hallu.topright]
        return punkty_obrysu

    def daj_obszar_lotu_szaranczy(self):
        return self.hall_glowny.rect_widoku

    def wylosuj_pozycje_startowa_szaranczy(self):
        rect = self.daj_obszar_lotu_szaranczy()
        # w hallu szarancze zawsze startuja w dolnym wierszu
        przesuniecie = random.randint(1, rect.width - 1)
        pozycja_startowa = (rect.left + przesuniecie, rect.bottom - 60)
        return pozycja_startowa

    def wylosuj_pozycje_startowa_gracza(self):
        (x, y) = self.hall_glowny.wylosuj_pozycje_startowa_gracza()
        return (x, y)

    def puste_obszary_kwiatowe(self):
        puste_obszary = []
        for obszar_nr in self.obszary_kwiatowe:
            if obszar_nr not in self.kwiaty:
                puste_obszary.append(obszar_nr)
        return puste_obszary

    def daj_losowy_niezjedzony_kwiat(self):
        if self.kwiaty:
            niezjedzone = [kwiat for kwiat in self.kwiaty.values() if not kwiat.zjedzony]
            if niezjedzone:
                return random.choice(niezjedzone)
        return None

    def usun_wszystkie_kwiaty(self):
        self.kwiaty = {}

    def usun_zjedzone_kwiaty(self):
        if self.kwiaty:
            zjedzone = [obszar_nr for obszar_nr in self.kwiaty if self.kwiaty[obszar_nr].zjedzony]
            for obszar_nr in zjedzone:
                del self.kwiaty[obszar_nr]

    def dodaj_kwiat(self):
        puste_obszary = self.puste_obszary_kwiatowe()
        if puste_obszary:
            wybrany_obszar = random.choice(puste_obszary)
            naroznik = self.obszary_kwiatowe[wybrany_obszar].topleft
            srodek = self.obszary_kwiatowe[wybrany_obszar].center
            pozycja_w_terenie = self.wylicz_pozycje_w_terenie(srodek)
            kwiat = Flower(pos=naroznik, pos_teren=pozycja_w_terenie)
            self.kwiaty[wybrany_obszar] = kwiat
            return kwiat
        return None  # nie mozna juz dodac, brak miejsca

    def wszystkie_drzwi(self):
        drzwi = self.hall_glowny.drzwi[:]
        drzwi.extend(self.korytarz_do_sal.drzwi)
        return drzwi

    def wstaw_drzwi(self, door, door_location):
        pass  # nie da sie wstawic drzwi, hall uzywa drzwi z parametrow konstruktora:  hall_glowny i korytarz_do_sal

    def przelicz_drzwi(self, skala_widoku):
        self.hall_glowny.przelicz_drzwi(skala_widoku)
        self.korytarz_do_sal.przelicz_drzwi(skala_widoku)

    def przelicz_sciany(self, pos, room_width, room_length):
        self.left_wall = NewWall((pos[0], pos[1]),
                                 self.wall_width, room_length)

        self.right_wall = NewWall((pos[0]+room_width-self.wall_width, pos[1]),
                                  self.wall_width, room_length)

        self.top_wall = NewWall((pos[0]+self.wall_width, pos[1]),
                                room_width-2*self.wall_width, self.wall_width)

        self.bottom_wall = NewWall((pos[0]+self.wall_width, pos[1]+room_length-self.wall_width),
                                   room_width-2*self.wall_width, self.wall_width)

    def przelicz_sciany_styczne(self):
        lewa_sciana_hallu = self.hall_glowny.left_wall
        prawa_sciana_korytarz = self.korytarz_do_sal.right_wall
        self.korytarz_do_sal.top_wall.rect.width += prawa_sciana_korytarz.width * 2
        self.korytarz_do_sal.bottom_wall.rect.width += prawa_sciana_korytarz.width * 2
        self.left_top_hall_wall = NewWall((lewa_sciana_hallu.pos[0], lewa_sciana_hallu.pos[1]),
                                          self.wall_width, prawa_sciana_korytarz.pos[1] - lewa_sciana_hallu.pos[1])
        y_sciany_dolnej = prawa_sciana_korytarz.pos[1] + prawa_sciana_korytarz.length
        self.left_bottom_hall_wall = NewWall((lewa_sciana_hallu.pos[0], y_sciany_dolnej),
                                             self.wall_width, lewa_sciana_hallu.pos[1] + lewa_sciana_hallu.length - y_sciany_dolnej)

    def walls(self):
        all_walls = [self.hall_glowny.right_wall, self.hall_glowny.top_wall, self.hall_glowny.bottom_wall]
        if self.left_top_hall_wall is not None:
            all_walls.append(self.left_top_hall_wall)
        if self.left_bottom_hall_wall is not None:
            all_walls.append(self.left_bottom_hall_wall)
        all_walls.extend([self.korytarz_do_sal.top_wall, self.korytarz_do_sal.left_wall, self.korytarz_do_sal.bottom_wall])
        return all_walls

    def skala_pozioma(self, docelowa_szerokosc):
        return docelowa_szerokosc / float(self.room_width)

    def skala_pionowa(self, docelowa_dlugosc):
        return docelowa_dlugosc / float(self.room_length)

    def oblicz_rect_widoku(self, docelowa_szerokosc, docelowa_dlugosc):
        dy_korytarz_hall = self.korytarz_do_sal.pos[1] - self.hall_glowny.pos[1]
        self.hall_glowny.oblicz_rect_widoku(docelowa_szerokosc, docelowa_dlugosc)
        self.skala_widoku = self.hall_glowny.skala_widoku

        korytarz_width = self.korytarz_do_sal.room_width * self.skala_widoku
        korytarz_length = self.korytarz_do_sal.room_length * self.skala_widoku
        self.korytarz_do_sal.rect_widoku = pygame.Rect(self.hall_glowny.rect_widoku.left - korytarz_width + 1, dy_korytarz_hall*self.skala_widoku,
                                                       korytarz_width, korytarz_length)
        self.hall_glowny.oblicz_obszary_kwiatowe()
        self.obszary_kwiatowe = self.hall_glowny.obszary_kwiatowe
        self.rect_widoku = self.oblicz_rect_widoku_ze_skladowych_sal()

    def oblicz_rect_widoku_ze_skladowych_sal(self):
        return pygame.Rect(self.korytarz_do_sal.rect_widoku.left, self.hall_glowny.rect_widoku.top,
                           self.korytarz_do_sal.rect_widoku.width + self.hall_glowny.rect_widoku.width,
                           self.hall_glowny.rect_widoku.height)

    def przeskaluj(self, docelowa_szerokosc, docelowa_dlugosc):
        self.hall_glowny.przeskaluj(docelowa_szerokosc, docelowa_dlugosc)
        #TODO przeskaluj self.korytarz_do_sal
        self.korytarz_do_sal.przelicz_sciany_wg_widoku()
        self.korytarz_do_sal.przelicz_drzwi(self.skala_widoku)
        self.przelicz_sciany_styczne()

    def draw(self, screen):
        self.hall_glowny.draw_podloga(screen)
        self.korytarz_do_sal.draw_podloga(screen)
        for wall in self.walls():
            wall.draw(screen)
        for kwiat in self.kwiaty.values():
            kwiat.draw(screen)
        for drzwi in self.hall_glowny.drzwi:
            drzwi.draw(screen)
        for drzwi in self.korytarz_do_sal.drzwi:
            drzwi.draw(screen)
        # for nr_obszaru in self.obszary_kwiatowe:
        #     rect = self.obszary_kwiatowe[nr_obszaru]
        #     pygame.draw.lines(screen, ((nr_obszaru*10)%255, (nr_obszaru*70)%255, (nr_obszaru*30)%255), False, [rect.topleft, rect.bottomleft, rect.bottomright, rect.topright, rect.topleft], 1)
