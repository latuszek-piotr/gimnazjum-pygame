import pygame
from pixel import Pixel


class Wall(Pixel):
    def __init__(self, pos, size=16, color=(255, 255, 255)):
        super(Wall, self).__init__(pos, size, color)
