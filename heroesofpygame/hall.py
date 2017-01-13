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
        self.rect_widoku = None  # wspolrzedne wyswietlane
        self.color = hall_glowny.color
        self.skala_widoku = 1.0
        self.polozenie_drzwi = []
        self.przelicz_sciany(self.pos, self.room_width, self.room_length)
        self.obszary_kwiatowe = {}  # slownik postaci {nr_oszaru: rect_obszaru}
        self.kwiaty = {}  # slownik postaci {nr_oszaru: obiekt_kwiat}
        self.left_top_hall_wall = None
        self.left_bottom_hall_wall = None


    def skala_widok_teren(self):
        if self.rect_widoku is None:
            return 1
        skala = float(self.teren.width) / self.rect_widoku.width
        return skala

    def daj_naroznik(self, ktory):
        if ktory == 'lewy-gorny':
            return self.left_wall.pos
        elif ktory == 'lewy-dolny':
            return (self.left_wall.pos[0], self.left_wall.pos[1] + self.left_wall.length)
        elif ktory == 'prawy-gorny':
            return (self.right_wall.pos[0] + self.right_wall.width, self.right_wall.pos[1])
        elif ktory == 'prawy-dolny':
            return (self.right_wall.pos[0] + self.right_wall.width, self.right_wall.pos[1] + self.right_wall.length)

    def widok_pionowy(self):
        '''dla pionowego wyswietlania sali wspolrzedna y (odleglosc od gornej krawedzi)
        jest mniejsza od wspolrzednej x (odleglosci od lewej krawedzi)'''
        (x_start, y_start) = self.rect_widoku.topleft
        return y_start < x_start

    def oblicz_obszary_kwiatowe(self, wielkosc_obszaru=60):
        (x_start, y_start) = self.rect_widoku.topleft
        if self.widok_pionowy(): # widok pionowy sali to kwiaty w gornym wierszu
            room_width = self.rect_widoku.width
            ilosc_kolumn = int((room_width - 5 - 5) // wielkosc_obszaru)
            obszary = {}
            for nr_obszaru in range(ilosc_kolumn):
                x = x_start + 5 + nr_obszaru*wielkosc_obszaru
                y = 10
                obszary[nr_obszaru] = pygame.Rect(x, y, wielkosc_obszaru, wielkosc_obszaru)
        else:  # widok poziomy sali to kwiaty w lewej kolumnie
            room_heigth = self.rect_widoku.height
            ilosc_wierszy = int((room_heigth - 5 - 5) // wielkosc_obszaru)
            obszary = {}
            for nr_obszaru in range(ilosc_wierszy):
                x = 10
                y = y_start + 5 + nr_obszaru*wielkosc_obszaru
                obszary[nr_obszaru] = pygame.Rect(x, y, wielkosc_obszaru, wielkosc_obszaru)
        self.obszary_kwiatowe = obszary

    def daj_obszar_lotu_szaranczy(self):
        return self.hall_glowny.rect_widoku

    def wylosuj_pozycje_startowa_szaranczy(self):
        rect = self.daj_obszar_lotu_szaranczy()
        # w hallu szarancze zawsze startuja w dolnym wierszu
        przesuniecie = random.randint(1, rect.width - 1)
        pozycja_startowa = (rect.left + przesuniecie, rect.bottom - 60)
        return pozycja_startowa

    def puste_obszary_kwiatowe(self):
        puste_obszary = []
        for obszar_nr in self.obszary_kwiatowe:
            if obszar_nr not in self.kwiaty:
                puste_obszary.append(obszar_nr)
        return puste_obszary

    def daj_losowy_niezjedzony_kwiat(self):
        if self.kwiaty:
            niezjedzone = [kwiat for kwiat in self.kwiaty.values() if not kwiat.zjedzony]
            return random.choice(niezjedzone)
        return None

    def usun_wszystkie_kwiaty(self):
        self.kwiaty = {}

    def usun_zjedzone_kwiaty(self):
        if self.kwiaty:
            zjedzone = [obszar_nr for obszar_nr in self.kwiaty if self.kwiaty[obszar_nr].zjedzony]
            for obszar_nr in zjedzone:
                del self.kwiaty[obszar_nr]

    def wylicz_pozycje_w_terenie(self, pozycja_w_widoku):
        naroznik_widoku = self.rect_widoku.topleft
        naroznik_terenu = self.teren.topleft
        dx_w_widoku = pozycja_w_widoku[0] - naroznik_widoku[0]
        dy_w_widoku = pozycja_w_widoku[1] - naroznik_widoku[1]
        skala = self.skala_widok_teren()
        dx_w_terenie = dx_w_widoku * skala
        dy_w_terenie = dy_w_widoku * skala
        pozycja_w_terenie = (naroznik_terenu[0] + dx_w_terenie, naroznik_terenu[1] + dy_w_terenie)
        return pozycja_w_terenie

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

    def daj_sciane(self, nazwa_sciany):
        if nazwa_sciany == 'left_wall':
            return self.left_wall
        elif nazwa_sciany == 'right_wall':
            return self.right_wall
        elif nazwa_sciany == 'top_wall':
            return self.top_wall
        elif nazwa_sciany == 'bottom_wall':
            return self.bottom_wall
        raise Exception("zla nazwa sciany")

    def wszystkie_drzwi(self):
        drzwi = self.hall_glowny.drzwi[:]
        drzwi.extend(self.korytarz_do_sal.drzwi)
        return drzwi

    def oblicz_rect_drzwi(self, door_location, door_delta, skala=1):
        door_delta = door_delta * skala
        wall = self.daj_sciane(nazwa_sciany=door_location)
        rect = wall.oblicz_rect_drzwi(door_delta=door_delta, skala=skala)
        return rect

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
        lewa_sciana_hallu = self.hall_glowny.daj_sciane('left_wall')
        prawa_sciana_korytarz = self.korytarz_do_sal.daj_sciane('right_wall')
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
        self.rect_widoku = self.hall_glowny.rect_widoku # TODO - to moze byc inne

        #TODO oblicz self.korytarz_do_sal
        korytarz_width = self.korytarz_do_sal.room_width * self.skala_widoku
        korytarz_length = self.korytarz_do_sal.room_length * self.skala_widoku
        self.korytarz_do_sal.rect_widoku = pygame.Rect(self.hall_glowny.rect_widoku.left - korytarz_width + 1, dy_korytarz_hall*self.skala_widoku,
                                                       korytarz_width, korytarz_length)
        self.hall_glowny.oblicz_obszary_kwiatowe()
        self.obszary_kwiatowe = self.hall_glowny.obszary_kwiatowe

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
