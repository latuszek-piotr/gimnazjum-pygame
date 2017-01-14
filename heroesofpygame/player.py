import pygame
import math
import time
from pixel import Pixel
from strzal import Strzal
from obliczenia import przesuniecie_w_kierunku
from heroesofpygame.door import Door
from heroesofpygame.wall import NewWall
from heroesofpygame.userevents import USEREVENT_PASS_DOOR


class Player(Pixel):
    def __init__(self, pos=(30, 30), size=4, color=(255,255,255)):
        super(Player, self).__init__(pos, size, color)
        self.pos_teren = pos
        self.nazwa = self.__class__.__name__
        self.direction = 0  # in degrees
        self.direction_color = (255, 0, 0)
        self.real_x = pos[0] * 1.0
        self.real_y = pos[1] * 1.0
        self.last_door_pass_time = time.time()

    def __str__(self):
        return "%s(x=%.2f, y=%.2f, dir=%s)" % (self.nazwa, self.real_x, self.real_y, self.direction)

    def move_at_direction(self, distance, all_objects_thay_may_colide):
        dx, dy = przesuniecie_w_kierunku(distance, self.direction)
        self.move(dx, dy, all_objects_thay_may_colide)
        print self

    def move_to(self, pos):
        # Move the rect
        self.real_x = pos[0]
        self.real_y = pos[1]
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def move_single_axis(self, dx, dy, all_objects_thay_may_colide):
        # Move the rect
        self.real_x += dx
        self.real_y += dy
        self.rect.x = self.real_x
        self.rect.y = self.real_y
        # If you collide with a wall, move out based on velocity
        for scene_object in all_objects_thay_may_colide:
            if scene_object is self:
                continue
            if self.collides(scene_object):
                if isinstance(scene_object, Strzal):  # gracze nie maja kolizji ze swoimi wlasnymi stralami
                    continue
                ### print "kolizja: ja:{} on:{}".format(self.rect, scene_object.rect)
                # I have collision with him
                self.collision(dx, dy, scene_object)

    def collides(self, other_scene_object):
        return self.rect.colliderect(other_scene_object.rect)

    def collision(self, last_move_dx, last_move_dy, other_scene_object):
        """what is impact of collision on me (self)"""
        if isinstance(other_scene_object, Door):
            door = other_scene_object
            now = time.time()
            czas_od_ostatniego_przejscia = now - self.last_door_pass_time
            if door.sala_1 and door.sala_2 and (czas_od_ostatniego_przejscia > 0.5):
                self.last_door_pass_time = now
                if door.sa_pionowe():
                    if door.rect.left < self.rect.left:
                        move_direction = 'left'
                    else:
                        move_direction = 'right'
                else:
                    if door.rect.top < self.rect.top:
                        move_direction = 'top'
                    else:
                        move_direction = 'bottom'
                pygame.event.post(pygame.event.Event(USEREVENT_PASS_DOOR, {'door': door, 'move_direction': move_direction}))
        elif isinstance(other_scene_object, NewWall):
            self._step_outside_colission(last_move_dx, last_move_dy, other_scene_object)

    def _step_outside_colission(self, last_move_dx, last_move_dy, other_scene_object):
        if last_move_dx > 0: # Moving right; Hit the left side of other_scene_object
            self.rect.right = other_scene_object.rect.left
            self.real_x = self.rect.x
        if last_move_dx < 0: # Moving left; Hit the right side of other_scene_object
            self.rect.left = other_scene_object.rect.right
            self.real_x = self.rect.x
        if last_move_dy > 0: # Moving down; Hit the top side of other_scene_object
            self.rect.bottom = other_scene_object.rect.top
            self.real_y = self.rect.y
        if last_move_dy < 0: # Moving up; Hit the bottom side of other_scene_object
            self.rect.top = other_scene_object.rect.bottom
            self.real_y = self.rect.y

    def draw(self, screen):
        self._draw_moving_direction(screen)

    def _draw_moving_direction(self, screen):
        direction_length = self.rect.right - self.rect.left
        dx, dy = przesuniecie_w_kierunku(direction_length, self.direction)
        arrow_dx1, arrow_dy1 = przesuniecie_w_kierunku(7, self.direction+150)
        arrow_dx2, arrow_dy2 = przesuniecie_w_kierunku(7, self.direction-150)
        koniec_strzaly = (self.rect.centerx + dx, self.rect.centery + dy)
        grot_punkt1 = (koniec_strzaly[0] + arrow_dx1, koniec_strzaly[1] + arrow_dy1)
        grot_punkt2 = (koniec_strzaly[0] + arrow_dx2, koniec_strzaly[1] + arrow_dy2)
        pygame.draw.lines(screen, self.direction_color, False, [self.rect.center, koniec_strzaly, grot_punkt1, koniec_strzaly, grot_punkt2], 1)
