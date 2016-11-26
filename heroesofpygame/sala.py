import pygame
from heroesofpygame.wall import NewWall
from heroesofpygame.flower import Flower


class ClassRoom(object):
    def __init__(self, pos, room_width, room_length, wall_width=3, color=(75, 5, 205), drzwi=None):
        self.room_width = room_width
        self.room_length = room_length
        self.pos = pos
        self.wall_width = wall_width
        self.color = color
        self.door_definition = drzwi
        self.przelicz_sciany(self.pos, self.room_width, self.room_length)
        self.kwiaty = []

    def daj_naroznik(self, ktory):
        if ktory == 'lewy-gorny':
            return self.left_wall.pos
        elif ktory == 'lewy-dolny':
            return (self.left_wall.pos[0], self.left_wall.pos[1] + self.left_wall.length)
        elif ktory == 'prawy-gorny':
            return (self.right_wall.pos[0] + self.right_wall.width, self.right_wall.pos[1] + self.right_wall.length)
        elif ktory == 'prawy-dolny':
            return (self.right_wall.pos[0] + self.right_wall.width, self.right_wall.pos[1] + self.right_wall.length)

    def dodaj_kwiat(self):
        pos = self.daj_naroznik(ktory='lewy-gorny')
        kwiat = Flower(pos=(pos[0]+10, pos[1]+10))
        self.kwiaty.append(kwiat)

    def przelicz_sciany(self, pos, room_width, room_length, skala=1):

        door_delta = None
        if self.door_definition and self.door_definition['location'] == 'left':
            door_delta = self.door_definition['door_delta'] * skala
        self.left_wall = NewWall((pos[0], pos[1]),
                                 self.wall_width, room_length, door_delta=door_delta)
        self.left_wall.przelicz_drzwi(skala=skala)

        door_delta = None
        if self.door_definition and self.door_definition['location'] == 'right':
            door_delta = self.door_definition['door_delta'] * skala
        self.right_wall = NewWall((pos[0]+room_width-self.wall_width, pos[1]),
                                  self.wall_width, room_length, door_delta=door_delta)
        self.right_wall.przelicz_drzwi(skala=skala)

        door_delta = None
        if self.door_definition and self.door_definition['location'] == 'top':
            door_delta = self.door_definition['door_delta'] * skala
        self.top_wall = NewWall((pos[0]+self.wall_width, pos[1]),
                                room_width-2*self.wall_width, self.wall_width, door_delta=door_delta)
        self.top_wall.przelicz_drzwi(skala=skala)

        door_delta = None
        if self.door_definition and self.door_definition['location'] == 'bottom':
            door_delta = self.door_definition['door_delta'] * skala
        self.bottom_wall = NewWall((pos[0]+self.wall_width, pos[1]+room_length-self.wall_width),
                                   room_width-2*self.wall_width, self.wall_width, door_delta=door_delta)
        self.bottom_wall.przelicz_drzwi(skala=skala)

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
            roznica_szerokosci = docelowa_szerokosc - room_width_pion
            poz_x = roznica_szerokosci / 2
            self.przelicz_sciany((poz_x,0), room_width_pion, room_length_pion, skala_pion)
        else:
            roznica_dlugosci = docelowa_dlugosc - room_length_poziom
            poz_y = roznica_dlugosci / 2
            self.przelicz_sciany((0,poz_y), room_width_poziom, room_length_poziom, skala_poziom)

    def draw(self, screen):
        for wall in self.walls():
            wall.draw(screen)
        for kwiat in self.kwiaty:
            kwiat.draw(screen)
