import pygame
import os
import time
from heroesofpygame.okno_wyboru import OknoWyboru


class Rozpoczecie(OknoWyboru):
    pygame_logo = os.path.join('grafika', 'pygame_logo.png')
    prognoza_szaranczy = os.path.join('film', 'prognoza_szaranczy.mpg')

    def __init__(self, szerokosc, wysokosc):
        super(Rozpoczecie, self).__init__(szerokosc, wysokosc, "Heroes of",
                                          button_ok=True, button_quit=False,
                                          button_play_text1="Start", button_play_text2="")
        self.rect_tytulu.left = 0.05 * self.szerokosc
        self.rect_logo = self.wylicz_rect_logo()
        self.pygame_logo_img = pygame.transform.scale(pygame.image.load(Rozpoczecie.pygame_logo).convert_alpha(),
                                                                        (self.rect_logo.width, self.rect_logo.height))
        self.prognoza_video = pygame.movie.Movie(Rozpoczecie.prognoza_szaranczy)
        self.czas_startu_video = None
        self.dlugosc_video = self.prognoza_video.get_length()
        self.film_wystartowany = False

    def wylicz_rect_logo(self):
        szerokosc = 0.4 * self.szerokosc
        wysokosc = 0.3 * self.wysokosc
        pos_x = 0.5 * self.szerokosc
        pos_y = 0.05 * self.wysokosc
        return pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)

    def draw(self, screen):
        self.draw_title(screen)
        screen.blit(self.pygame_logo_img, self.rect_logo.topleft)
        if not self.film_wystartowany:
            self.czas_startu_video = time.time()
            self.prognoza_video.set_display(screen, self.rect_gameover)
            self.prognoza_video.play()
            self.film_wystartowany = True
        elif time.time() - self.czas_startu_video > self.dlugosc_video:
            self.draw_button_ok(screen)
