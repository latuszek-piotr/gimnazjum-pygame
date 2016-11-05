import pygame
from pixel import Pixel


class Wall(Pixel):
    def __init__(self, pos, size=3, color=(255, 255, 255)):
        super(Wall, self).__init__(pos, size, color)


class NewWall(Pixel):
    def __init__(self, pos, width, length, color=(75, 5, 205)):
        self.pos = pos
        self.width = width
        self.length = length
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], width, length)
