import pygame
import os
import time
from obliczenia import przesuniecie_w_kierunku, odleglosc


class Strzal(object):
    strzal_img = []
    for nr in range(1,10):
        strzal_img.append(os.path.join('grafika', 'strzal', 'strzal_%s.png' % nr))

    def __init__(self, pos=(910, 150), size=50):
        current_img = Strzal.strzal_img[0]
        self.images = [
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[0]).convert_alpha(), (50, 20)), True, False), (20, 100)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[1]).convert_alpha(), (100, 100)), True, False),(0, 20)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[2]).convert_alpha(), (100, 120)), True, False),(20, 0)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[3]).convert_alpha(), (200, 120)), True, False),(-30, 0)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[4]).convert_alpha(), (180, 120)), True, False),(50, 0)),
                       (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[5]).convert_alpha(), (90, 120)), True, False),(180, -20)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[6]).convert_alpha(), (80, 120)), True, False),(190, 0)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[7]).convert_alpha(), (70, 120)), True, False),(200, 0)),
                       # (pygame.transform.flip(pygame.transform.scale(pygame.image.load(Strzal.strzal_img[8]).convert_alpha(), (60, 120)), True, False),(210, 0)),
                       ]
        self.dzwiek_strzalu = pygame.mixer.Sound('dzwiek/dzwiek_walki/strzal.wav')
        self.pos = list(pos)
        self.size = size
        self.ustaw_pozycje(pos[0], pos[1])
        self.start_time = None
        self.skok_czasu = 1.07
        self.skok_pozycji = 0
        self.direction = 0  # in degrees

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
                pos = (self.pos[0] + delta_x, self.pos[1] + delta_y)
                pygame.draw.lines(screen, (255, 0, 255), False, [self.pos, pos], 1)
                self.ustaw_rect_do_kolizji(pos[0], pos[1])
                screen.blit(image, pos)
                img_rect = image.get_rect().move(pos)
                pygame.draw.lines(screen, (0, 255, image_index*30), False, [img_rect.topleft, img_rect.bottomleft, img_rect.bottomright, img_rect.topright, img_rect.topleft], 1)

                self.obroc_obraz(image, self.pos, pos, screen)
                # final_image, nowa_pozycja_obrazu = self.obroc_obraz(image, self.pos, pos, screen)
                # img_rect = final_image.get_rect().move(nowa_pozycja_obrazu)
                # pygame.draw.lines(screen, (0, 255, image_index*30), False, [img_rect.topleft, img_rect.bottomleft, img_rect.bottomright, img_rect.topright, img_rect.topleft], 1)
                # screen.blit(final_image, nowa_pozycja_obrazu)

    def ktory_obraz(self):
        now = time.time()
        time_delta = now - self.start_time
        ktory = int(time_delta / self.skok_czasu)
        return ktory

    def obroc_obraz(self, image, os_obrotu, pozycja_obrazu, screen):
        # "%s(x=%.2f, y=%.2f, dir=%s)" % (self.nazwa, self.real_x, self.real_y, self.direction)
        srodek_obrazu = (pozycja_obrazu[0] + image.get_rect().centerx,  pozycja_obrazu[1] + image.get_rect().centery)
        pygame.draw.lines(screen, (255, 200, 255), False, [os_obrotu, srodek_obrazu], 1)
        distance = odleglosc(os_obrotu, srodek_obrazu)
        print "odleglosc = %s" % distance
        dx, dy = przesuniecie_w_kierunku(distance, self.direction)
        # wspolrzedne y w pygame rosna w inna strone niz w ukladzie wsp. kartezjanskich
        nowa_pozycja_srodka_obrazu = (os_obrotu[0] + dx, os_obrotu[1] - dy)
        pygame.draw.lines(screen, (255, 200, 255), False, [os_obrotu, nowa_pozycja_srodka_obrazu], 1)
        obrocony_obraz = pygame.transform.rotate(image, self.direction)
        dx2 = obrocony_obraz.get_rect().centerx - obrocony_obraz.get_rect().left
        dy2 = obrocony_obraz.get_rect().centery - obrocony_obraz.get_rect().top
        nowa_pozycja_obrazu = (nowa_pozycja_srodka_obrazu[0] - dx2, nowa_pozycja_srodka_obrazu[1] - dy2)
        pygame.draw.lines(screen, (255, 200, 255), False, [os_obrotu, nowa_pozycja_obrazu], 1)
        # screen.blit(obrocony_obraz, obrocony_obraz.get_rect().topleft)

        screen.blit(obrocony_obraz, nowa_pozycja_obrazu)
        # return (obrocony_obraz, nowa_pozycja_obrazu)
