import pygame
from pixel import Pixel


class Player(Pixel):
    def __init__(self, pos=(30, 30), size=4, color=(255,255,255)):
        super(Player, self).__init__(pos, size, color)

    def move_single_axis(self, dx, dy, walls):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom