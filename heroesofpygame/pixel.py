import pygame


class Pixel(object):
    def __init__(self, pos, size, color=(255, 255, 255)):
        self.size = size
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], self.size, self.size)

    def move(self, dx, dy, other_scene_object):
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, other_scene_object)
        if dy != 0:
            self.move_single_axis(0, dy, other_scene_object)

    def move_single_axis(self, dx, dy, other_scene_object):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

    def collides(self, other_scene_object):
        return self.rect.colliderect(other_scene_object.rect)

    def collision(self, last_move_dx, last_move_dy, other_scene_object):
        """what is impact of collision on me (self)"""
        # default is: I'm not moving since I'm not movable
        pass

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
