import pygame


class Pixel(object):
    def __init__(self, pos, size, color=(255, 255, 255)):
        self.size = size
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], self.size, self.size)

    def move(self, dx, dy, walls):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, walls)
        if dy != 0:
            self.move_single_axis(0, dy, walls)

    def move_single_axis(self, dx, dy, walls):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)