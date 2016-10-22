import pygame
import os
import time

class Strzal(object):
    strzal_img = []
    for nr in range(1,6):
        strzal_img.append(os.path.join('grafika', 'strzal', 'strzal_%s.png' % nr))

    def __init__(self, pos=(910, 150), size=50):
        current_img = Strzal.strzal_img[0]
        self.images = [
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[0]).convert_alpha(), (50, 20)), (-20, 100)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[1]).convert_alpha(), (100, 100)),(0, 20)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[2]).convert_alpha(), (100, 120)),(20, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[3]).convert_alpha(), (200, 120)),(40, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[4]).convert_alpha(), (180, 120)),(70, 0)),
                       ]
        self.pos = pos
        self.start_time = None
        self.skok_czasu = 0.07
        self.skok_pozycji = 0

    def start(self):
        self.start_time = time.time()

    def draw(self, screen):
        if self.start_time:
            image_index = self.ktory_obraz()
            if image_index > 4:
                self.start_time = None  # koniec strzalu
            else:
                # Copy image to screen:
                (image, (delta_x, delta_y)) = self.images[image_index]
                pos = (self.pos[0] - delta_x, self.pos[1] + delta_y)
                screen.blit(image, pos)

    def ktory_obraz(self):
        now = time.time()
        time_delta = now - self.start_time
        ktory = int(time_delta / self.skok_czasu)
        return ktory
