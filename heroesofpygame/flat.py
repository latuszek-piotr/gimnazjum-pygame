import pygame
from wall import Wall


class Flat(object):
    def __init__(self, flat_data, wall_thikness=16):
        self.flat_data = flat_data
        self.wall_thikness = wall_thikness
        self.color = (255, 155, 105)
        self.walls = self.create_walls()

    def create_walls(self):
        walls = []
        x = y = 0
        for row in self.flat_data:
            for col in row:
                if col == "w":
                    single_wall = Wall((x, y))
                    walls.append(single_wall)
                x += self.wall_thikness
            y += self.wall_thikness
            x = 0
        return walls

    def draw(self, screen):
        for wall in self.walls:
            pygame.draw.rect(screen, self.color, wall.rect)


flat_1_data = [
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
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
"w                                   w            w                                   w",
"w                                   w            w                                   w",
"w                                   p            w                                   w",
"w                                   p            w                                   w",
"w                                   w            w                                   w",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww            w                                   w",
                                     "w"         "w                                   w",
                                     "w"         "w                                   w",
                                     "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
]