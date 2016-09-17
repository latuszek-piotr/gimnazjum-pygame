import pygame
from pixel import Pixel


class Door(Pixel):
    def __init__(self, pos, size=16, color=(50, 50, 50)):
        super(Door, self).__init__(pos, size, color)
