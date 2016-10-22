import pygame


class ClassRoom(object):
    def __init__(self, pos, room_width, room_length, wall_width=3, color=(75, 5, 205)):
        self.room_width = room_width
        self.room_length = room_length
        self.pos = pos
        self.wall_width = wall_width
        self.color = color
        self.left_wall = pygame.Rect(pos[0], pos[1], self.wall_width, self.room_length)
        self.right_wall = pygame.Rect(pos[0]+room_width-wall_width, pos[1], self.wall_width, self.room_length)
        self.top_wall = pygame.Rect(pos[0]+wall_width, pos[1], room_width-2*wall_width, wall_width)
        self.bottom_wall = pygame.Rect(pos[0]+wall_width, pos[1]+room_length-wall_width, room_width-2*wall_width, wall_width)
        

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.left_wall)
        pygame.draw.rect(screen, self.color, self.right_wall)
        pygame.draw.rect(screen, self.color, self.top_wall)
        pygame.draw.rect(screen, self.color, self.bottom_wall)

