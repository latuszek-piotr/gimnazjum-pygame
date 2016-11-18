import pygame
from pixel import Pixel


class Door(Pixel):
    def __init__(self, pos, width, length, color=(255, 0, 0)):
        self.pos = pos
        self.width = width
        self.length = length
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], width, length)


