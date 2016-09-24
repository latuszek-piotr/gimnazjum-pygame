import pygame
from wall import Wall
from door import Door

class Flat(object):
    def __init__(self, flat_data):
        self.flat_data = flat_data
        self.wall_color = (255, 155, 105)
        self.door_color = (50, 50, 50)
        self.walls = self.create_walls()
        self.doors = self.create_doors()

    def create_walls(self):
        walls = []
        wall_thikness = Wall(pos=(0, 0)).size
        x = y = 0
        for row in self.flat_data:
            for col in row:
                if col == "w":
                    single_wall = Wall(pos=(x, y), color=self.wall_color)
                    walls.append(single_wall)
                x += wall_thikness
            y += wall_thikness
            x = 0
        return walls

    def create_doors(self):
        doors = []
        wall_thikness = Wall(pos=(0, 0)).size
        x = y = 0
        for row in self.flat_data:
            for col in row:
                if col == "d":
                    single_door = Door(pos=(x, y), color=self.door_color)
                    doors.append(single_door)
                x += wall_thikness
            y += wall_thikness
            x = 0
        return doors

    def draw(self, screen):
        for wall in self.walls:
            wall.draw(screen)
        for door in self.doors:
            door.draw(screen)


flat_1_data = [
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"                                                                            w                                                                                                                                   w",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"w                                    w                                                          w                  w                  w                  w              wsssssssssssssssswwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"w                                    w                                                          w                  w                 kwk                                wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                  w           wwwwwwwwwwwwwww                          wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                    kwk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                                     w                  w              wssssssssssssssssw                       d                                                                 w",
"w                                    w                                                          w                              wwwwwwwwwwwwwwwwwwwwwwwwwww              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w                  w                  w                  w              wssssssssssssssssw                       d                                                                 w",
"w                                    d                                                          w                  w                  wk                 w              wssssssssssssssssw                       w                                                                 w",
"w                                    d                                                          w                  w                  w                  w              wssssssssssssssssw                       w                                                                 w",
"w                                    w                                                          w""wwww""dd""wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwppwwwwwwwwwwwwwwwwwwww                w                       w                                                                 w",
"w                                    w                                                          w                                                                                                                d                                                                 w",
"w                                    w                                                          w                                                                                                                d                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                    w                                                          d                                                                                                                w                                                                 w",
"w                                    w                                                          d                                                                                                                w                                                                 w",
"w                                    w                                                          w                                                                                                                w                                                                 w",
"w                                   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww""dd""wwwww""dd""wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww                                        w                                                                 w",
"w                                   w            w                                                                w                                                     w                                        w                                                                 w",
"w                                   w            w                                                                w                                                     w                                        wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww",
"w                                   d            w                                                                w                                                     wssssssswsssssssw                        d          w          w          w",
"w                                   d            w                                                                w                                                     wssssssswsssssssw                        d          w          w          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"w                                   w            w                                                                w                                                     wssssssswwwwwwwww                        w          d          d          w",
"wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww            w                                                                w                                                     wssssssswsssssssw                        w          w          w          w",
"                                    w            w                                                                w                                                     wssssssswsssssssw                        w          w          w          w",
"                                    w            w                                                                w                                                     w               w                        w          w          w          w",
"                                    wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwdddddwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
]