import pygame
from pixel import Pixel
from strzal import Strzal


class Player(Pixel):
    def __init__(self, pos=(30, 30), size=4, color=(255,255,255)):
        super(Player, self).__init__(pos, size, color)
        self.nazwa = self.__class__.__name__

    def serialize_for_network(self, action='move'):
        # Serialize only what is important to send over network.
        network_record = "x=%s, y=%s, name=%s, action=%s" % (self.rect.x, self.rect.y, self.nazwa, action)
        return network_record

    @staticmethod
    def unpack_network_record(network_record):
        parts = network_record.split(',')
        #print parts
        x = int(parts[0].split('=')[1])
        y = int(parts[1].split('=')[1])
        name = parts[2].split('=')[1]
        action = parts[3].split('=')[1]
        return ((x, y), name, action)

    def move_to(self, pos):
        # Move the rect
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move_single_axis(self, dx, dy, all_objects_thay_may_colide):
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy
        # If you collide with a wall, move out based on velocity
        for scene_object in all_objects_thay_may_colide:
            if scene_object is self:
                continue
            if self.collides(scene_object):
                if isinstance(scene_object, Strzal):
                    continue
                ### print "kolizja: ja:{} on:{}".format(self.rect, scene_object.rect)
                # I have collision with him
                self.collision(dx, dy, scene_object)
                # and he has collision with me
                #scene_object.collision(dx, dy, self)

    def collides(self, other_scene_object):
        return self.rect.colliderect(other_scene_object.rect)

    def collision(self, last_move_dx, last_move_dy, other_scene_object):
        """what is impact of collision on me (self)"""
        self._step_outside_colission(last_move_dx, last_move_dy, other_scene_object)

    def _step_outside_colission(self, last_move_dx, last_move_dy, other_scene_object):
        if last_move_dx > 0: # Moving right; Hit the left side of other_scene_object
            self.rect.right = other_scene_object.rect.left
        if last_move_dx < 0: # Moving left; Hit the right side of other_scene_object
            self.rect.left = other_scene_object.rect.right
        if last_move_dy > 0: # Moving down; Hit the top side of other_scene_object
            self.rect.bottom = other_scene_object.rect.top
        if last_move_dy < 0: # Moving up; Hit the bottom side of other_scene_object
            self.rect.top = other_scene_object.rect.bottom
