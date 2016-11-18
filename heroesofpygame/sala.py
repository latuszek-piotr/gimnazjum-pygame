import pygame
from heroesofpygame.wall import NewWall
from heroesofpygame.door import Door


class ClassRoom(object):
    def __init__(self, pos, room_width, room_length, wall_width=3, color=(75, 5, 205)):
        self.room_width = room_width
        self.room_length = room_length
        self.pos = pos
        self.wall_width = wall_width
        self.color = color
        self.przelicz_sciany(self.pos, self.room_width, self.room_length)
        self.doors = []
        self.przelicz_drzwi(self.pos)


    def przelicz_sciany(self, pos, room_width, room_length):
        self.left_wall = NewWall((pos[0], pos[1]), self.wall_width, room_length)
        self.right_wall = NewWall((pos[0]+room_width-self.wall_width, pos[1]), self.wall_width, room_length)
        self.top_wall = NewWall((pos[0]+self.wall_width, pos[1]), room_width-2*self.wall_width, self.wall_width)
        self.bottom_wall = NewWall((pos[0]+self.wall_width, pos[1]+room_length-self.wall_width), room_width-2*self.wall_width, self.wall_width)

    def przelicz_drzwi(self, pos):
        drzwi = Door(pos,self.wall_width,30)
        self.doors = [drzwi]

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
            self.przelicz_sciany((poz_x,0), room_width_pion, room_length_pion)
            self.przelicz_drzwi((poz_x,0))

        else:
            roznica_dlugosci = docelowa_dlugosc - room_length_poziom
            poz_y = roznica_dlugosci / 2
            self.przelicz_sciany((0,poz_y), room_width_poziom, room_length_poziom)
            self.przelicz_drzwi((0,poz_y))

    def draw(self, screen):
        for wall in self.walls():
            wall.draw(screen)
        for door in self.doors:
            door.draw(screen)
