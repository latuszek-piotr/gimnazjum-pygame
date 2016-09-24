import pygame
from wall import Wall
from door import Door

class Flat(object):
    def __init__(self, flat_data, wall_thikness=16):
        self.flat_data = flat_data
        self.wall_thikness = wall_thikness
        self.wall_color = (255, 155, 105)
        self.door_color = (50, 50, 50)
        self.walls = self.create_walls()
        self.doors = self.create_doors()

    def create_walls(self):
        walls = []
        x = y = 0
        for row in self.flat_data:
            for col in row:
                if col == "w":
                    single_wall = Wall(pos=(x, y), color=self.wall_color)
                    walls.append(single_wall)
                x += self.wall_thikness
            y += self.wall_thikness
            x = 0
        return walls

    def create_doors(self):
        doors = []
        x = y = 0
        for row in self.flat_data:
            for col in row:
                if col == "d":
                    single_door = Door(pos=(x, y), color=self.door_color)
                    doors.append(single_door)
                x += self.wall_thikness
            y += self.wall_thikness
            x = 0
        return doors

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)
        for door in self.doors:
            door.draw(screen)


flat_1_data = [
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    d                                                          w",
"w                                    d                                                          w",
"w                                    w                                                          w","wwww""dd""wwwwwwwwwwwwwwwwwwwwwwwww"
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          w",
"w                                    w                                                          d",
"w                                    w                                                          d",
"w                                    w                                                          w",
"w                                   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww""dd""wwwww""dd""wwwwwwwwwwww",
"w                                   w            w                                   w",
"w                                   w            w                                   w",
"w                                   d            w                                   w",
"w                                   d            w                                   w",
"w                                   w            w                                   w",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww            w                                   w",
                                     "w"         "w                                   w",
                                     "w"         "w                                   w",
                                     "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
]