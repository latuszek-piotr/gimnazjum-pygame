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
        self.doors = []

    def oblicz_rect_drzwi(self, door_delta, skala=1, door_length = 5):
        if self.jest_pionowa():
            drzwi_rect = pygame.Rect(self.pos[0], self.pos[1] + door_delta, self.width, door_length * skala)
        else:
            drzwi_rect = pygame.Rect(self.pos[0] + door_delta, self.pos[1], door_length * skala, self.length)
        return drzwi_rect

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
