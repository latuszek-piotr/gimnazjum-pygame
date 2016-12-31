import pygame
import os
import time

class Strzal(object):
    strzal_img = []
    for nr in range(1,10):
        strzal_img.append(os.path.join('grafika', 'strzal', 'strzal_%s.png' % nr))

    def __init__(self, pos=(910, 150), size=50):
        current_img = Strzal.strzal_img[0]
        self.images = [
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[0]).convert_alpha(), (50, 20)), (-20, 100)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[1]).convert_alpha(), (100, 100)),(0, 20)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[2]).convert_alpha(), (100, 120)),(20, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[3]).convert_alpha(), (200, 120)),(40, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[4]).convert_alpha(), (180, 120)),(80, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[5]).convert_alpha(), (90, 120)),(110, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[6]).convert_alpha(), (80, 120)),(110, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[7]).convert_alpha(), (70, 120)),(110, 0)),
                       (pygame.transform.scale(pygame.image.load(Strzal.strzal_img[8]).convert_alpha(), (60, 120)),(110, 0)),
                       ]
        self.dzwiek_strzalu = pygame.mixer.Sound('dzwiek/dzwiek_walki/strzal.wav')
        self.pos = list(pos)
        self.size = size
        self.ustaw_pozycje(pos[0], pos[1])
        self.start_time = None
        self.skok_czasu = 0.07
        self.skok_pozycji = 0

    def ustaw_pozycje(self, x, y):
        self.pos[0] = x
        self.pos[1] = y
        self.ustaw_rect_do_kolizji(x, y)

    def ustaw_rect_do_kolizji(self, x, y):
        self.rect = pygame.Rect(x, y, self.size, self.size)

    def is_running(self):
        return self.start_time is not None

    def start(self):
        self.start_time = time.time()
        self.dzwiek_strzalu.play()

    def draw(self, screen):
        if self.start_time:
            image_index = self.ktory_obraz()
            if image_index >= len(self.images):
                self.start_time = None  # koniec strzalu
            else:
                # Copy image to screen:
                (image, (delta_x, delta_y)) = self.images[image_index]
                pos = (self.pos[0] - delta_x, self.pos[1] + delta_y)
                self.ustaw_rect_do_kolizji(pos[0], pos[1])
                screen.blit(image, pos)

    def ktory_obraz(self):
        now = time.time()
        time_delta = now - self.start_time
        ktory = int(time_delta / self.skok_czasu)
        return ktory
