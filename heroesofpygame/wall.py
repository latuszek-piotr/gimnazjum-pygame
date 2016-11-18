import pygame
from pixel import Pixel
from heroesofpygame.door import Door


class Wall(Pixel):
    def __init__(self, pos, size=3, color=(255, 255, 255)):
        super(Wall, self).__init__(pos, size, color)


class NewWall(Pixel):
    def __init__(self, pos, width, length, color=(75, 5, 205), door_delta=None):
        self.pos = pos
        self.width = width
        self.length = length
        self.color = color
        self.door_delta = door_delta
        self.rect = pygame.Rect(pos[0], pos[1], width, length)
        self.doors = []
        self.door_length = 7
        self.przelicz_drzwi()

    def przelicz_drzwi(self, skala=1):
        if self.door_delta is None:
            self.doors = []
            return
        if self.jest_pionowa():
            pos = (self.pos[0], self.pos[1] + self.door_delta)
        else:
            pos = (self.pos[0] + self.door_delta, self.pos[1])
        drzwi = Door(pos, self.width, self.door_length * skala)
        self.doors = [drzwi]

    def poczatek_sciany(self):
        return self.pos

    def jest_pionowa(self):
        if self.length > self.width:
            return True
        else:
            return False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

        for door in self.doors:
            door.draw(screen)
