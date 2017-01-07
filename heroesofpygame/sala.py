import pygame
import random
from heroesofpygame.wall import NewWall
from heroesofpygame.flower import Flower
from heroesofpygame.door import Door


class ClassRoom(object):
    def __init__(self, nazwa, pos, room_width, room_length, wall_width=3, color=(75, 5, 205)):
        self.nazwa = nazwa
        self.font = pygame.font.SysFont("comic sans MS", 15, bold=True)
        self.room_width = room_width
        self.room_length = room_length
        self.pos = pos
        self.wall_width = wall_width
        self.color = color
        self.skala_widoku = 1.0
        self.drzwi = []
        self.polozenie_drzwi = []
        self.przelicz_sciany(self.pos, self.room_width, self.room_length)
        self.obszary_kwiatowe = self.oblicz_obszary_kwiatowe()  # slownik postaci {nr_oszaru: rect_obszaru}
        self.kwiaty = {}  # slownik postaci {nr_oszaru: obiekt_kwiat}

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
        (x_start, y_start) = self.daj_naroznik(ktory='lewy-gorny')
        return y_start < x_start

    def oblicz_obszary_kwiatowe(self, wielkosc_obszaru=60):
        (x_start, y_start) = self.daj_naroznik(ktory='lewy-gorny')
        if self.widok_pionowy(): # widok pionowy sali to kwiaty w gornym wierszu
            (x_end, y_end) = self.daj_naroznik(ktory='prawy-gorny')
            room_width = x_end - x_start
            ilosc_kolumn = int((room_width - 5 - 5) // wielkosc_obszaru)
            obszary = {}
            for nr_obszaru in range(ilosc_kolumn):
                x = x_start + 5 + nr_obszaru*wielkosc_obszaru
                y = 10
                obszary[nr_obszaru] = pygame.Rect(x, y, wielkosc_obszaru, wielkosc_obszaru)
        else:  # widok poziomy sali to kwiaty w lewej kolumnie
            (x_end, y_end) = self.daj_naroznik(ktory='lewy-dolny')
            room_heigth = y_end - y_start
            ilosc_wierszy = int((room_heigth - 5 - 5) // wielkosc_obszaru)
            obszary = {}
            for nr_obszaru in range(ilosc_wierszy):
                x = 10
                y = y_start + 5 + nr_obszaru*wielkosc_obszaru
                obszary[nr_obszaru] = pygame.Rect(x, y, wielkosc_obszaru, wielkosc_obszaru)
        return obszary

    def wylosuj_pozycje_startowa_szaranczy(self):
        (x_end, y_end) = self.daj_naroznik(ktory='prawy-dolny')
        if self.widok_pionowy(): # widok pionowy sali to szarancze w dolnym wierszu
            (x_start, y_start) = self.daj_naroznik(ktory='lewy-dolny')
            room_width = int(x_end - x_start)
            przesuniecie = random.randint(1, room_width - 1)
            pozycja_startowa = (x_start + przesuniecie, y_start - 60)
        else:  # widok poziomy sali to szarancze w prawej kolumnie
            (x_start, y_start) = self.daj_naroznik(ktory='prawy-gorny')
            room_heigth = int(y_end - y_start)
            przesuniecie = random.randint(1, room_heigth - 1)
            pozycja_startowa = (x_start - 60, y_start + przesuniecie)
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

    def dodaj_kwiat(self):
        puste_obszary = self.puste_obszary_kwiatowe()
        if puste_obszary:
            wybrany_obszar = random.choice(puste_obszary)
            naroznik = self.obszary_kwiatowe[wybrany_obszar].topleft
            kwiat = Flower(pos=naroznik)
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

    def oblicz_rect_drzwi(self, door_location, door_delta, skala=1):
        door_delta = door_delta * skala
        wall = self.daj_sciane(nazwa_sciany=door_location)
        rect = wall.oblicz_rect_drzwi(door_delta=door_delta, skala=skala)
        return rect

    def wstaw_drzwi(self, door, door_location):
        self.drzwi.append(door)
        wektor_polozenia = (door.rect.left - self.pos[0], door.rect.top - self.pos[1])
        self.polozenie_drzwi.append((wektor_polozenia, door_location))

    def przelicz_drzwi(self, skala_widoku):
        (x_start, y_start) = self.daj_naroznik(ktory='lewy-gorny')
        for idx, drzwi in enumerate(self.drzwi):
            (wektor_polozenia, door_location) = self.polozenie_drzwi[idx]
            wall = self.daj_sciane(nazwa_sciany=door_location)
            pos_drzwi = [x_start + wektor_polozenia[0]*skala_widoku, y_start + wektor_polozenia[1]*skala_widoku]
            if drzwi.rect_def.height > drzwi.rect_def.width:  # pionowe drzwi
                width = self.wall_width
                height = drzwi.rect_def.height*skala_widoku
                pos_drzwi[0] = wall.rect.left  # korekta polozenia, dosuniecie drzwi "w sciane"
            else:
                width = drzwi.rect_def.width*skala_widoku
                height = self.wall_width
                pos_drzwi[1] = wall.rect.top  # korekta polozenia, dosuniecie drzwi "w sciane"
            drzwi.rect = pygame.Rect(pos_drzwi[0], pos_drzwi[1], width, height)

    def przelicz_sciany(self, pos, room_width, room_length):
        self.left_wall = NewWall((pos[0], pos[1]),
                                 self.wall_width, room_length)

        self.right_wall = NewWall((pos[0]+room_width-self.wall_width, pos[1]),
                                  self.wall_width, room_length)

        self.top_wall = NewWall((pos[0]+self.wall_width, pos[1]),
                                room_width-2*self.wall_width, self.wall_width)

        self.bottom_wall = NewWall((pos[0]+self.wall_width, pos[1]+room_length-self.wall_width),
                                   room_width-2*self.wall_width, self.wall_width)

    def walls(self):
        return [self.left_wall, self.right_wall, self.top_wall, self.bottom_wall]

    def skala_pozioma(self, docelowa_szerokosc):
        return docelowa_szerokosc / float(self.room_width)

    def skala_pionowa(self, docelowa_dlugosc):
        return docelowa_dlugosc / float(self.room_length)

    def przeskaluj(self, docelowa_szerokosc, docelowa_dlugosc):
        skala_pion = self.skala_pionowa(docelowa_dlugosc)
        skala_poziom = self.skala_pozioma(docelowa_szerokosc)

        room_width_pion = self.room_width * skala_pion
        room_length_pion = self.room_length * skala_pion
        room_width_poziom = self.room_width * skala_poziom
        room_length_poziom = self.room_length * skala_poziom

        if (room_width_pion <= docelowa_szerokosc) and (room_length_pion <= docelowa_dlugosc):
            self.skala_widoku = skala_pion
            roznica_szerokosci = docelowa_szerokosc - room_width_pion
            poz_x = roznica_szerokosci / 2
            self.przelicz_sciany((poz_x,0), room_width_pion, room_length_pion)
        else:
            self.skala_widoku = skala_poziom
            roznica_dlugosci = docelowa_dlugosc - room_length_poziom
            poz_y = roznica_dlugosci / 2
            self.przelicz_sciany((0,poz_y), room_width_poziom, room_length_poziom)
        self.przelicz_drzwi(self.skala_widoku)

        self.obszary_kwiatowe = self.oblicz_obszary_kwiatowe()


    def draw_podloga(self, screen):
        (x_start, y_start) = self.daj_naroznik(ktory='lewy-gorny')
        (x_end, y_end) = self.daj_naroznik(ktory='prawy-dolny')
        rect = pygame.Rect(x_start, y_start, x_end-x_start, y_end-y_start)
        pygame.draw.rect(screen, (0,0,0), rect)

    def draw(self, screen):
        self.draw_podloga(screen)
        for wall in self.walls():
            wall.draw(screen)
        for kwiat in self.kwiaty.values():
            kwiat.draw(screen)
        for drzwi in self.drzwi:
            drzwi.draw(screen)
        # for nr_obszaru in self.obszary_kwiatowe:
        #     rect = self.obszary_kwiatowe[nr_obszaru]
        #     pygame.draw.lines(screen, ((nr_obszaru*10)%255, (nr_obszaru*70)%255, (nr_obszaru*30)%255), False, [rect.topleft, rect.bottomleft, rect.bottomright, rect.topright, rect.topleft], 1)
