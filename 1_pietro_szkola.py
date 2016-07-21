import os
import random
import pygame

class Wall(object):

    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

pygame.display.set_caption("szkola_1_pietro")
screen = pygame.display.set_mode((890, 500))

walls = [] # List to hold the walls

level = [
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w             e                      w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    p                                                          w",
"w                                    p                                                          w",
"w                                    w                                                          w","wwww""pp""wwwwwwwwwwwwwwwwwwwwwwwww"
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          p",
"w                                    w                                                          p",
"w                                    w                                                          w",
"w                                   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww""pp""wwwww""pp""wwwwwwwwwwww",
"w                                   w            w",
"w                                   w            w",
"w                                   p            w",
"w                                   p            w",
"w                                   w            w",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww            w",
                                     "w"         "w",
                                     "w"         "w",
                                     "wwwwwwwwwwwww""wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
]


x = y = 0
for row in level:
    for col in row:
        if col == "W":
            Wall((x, y))
        if col == "E":
            end_rect = pygame.Rect(x, y, 16, 16)
        x += 16
    y += 16
    x = 0