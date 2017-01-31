import pygame
import os
import time
from heroesofpygame.okno_wyboru import OknoWyboru


class Rozpoczecie(OknoWyboru):
    pygame_logo = os.path.join('grafika', 'pygame_logo.png')
    sluchawka = os.path.join('grafika', 'sluchawka.png')
    prognoza_szaranczy = os.path.join('film', 'prognoza_szaranczy.mpg')
    ratujcie_kwiaty_nagranie = os.path.join('dzwiek', 'pani_kowalska_ratujcie_kwiaty.wav')

    def __init__(self, szerokosc, wysokosc):
        super(Rozpoczecie, self).__init__(szerokosc, wysokosc, "Heroes of",
                                          button_ok=True, button_quit=False,
                                          button_play_text1="Start", button_play_text2="")
        self.rect_tytulu.left = 0.05 * self.szerokosc
        self.rect_logo = self.wylicz_rect_logo()
        self.pygame_logo_img = pygame.transform.scale(pygame.image.load(Rozpoczecie.pygame_logo).convert_alpha(),
                                                                        (self.rect_logo.width, self.rect_logo.height))
        self.rect_sluchawki = self.rect_rozgrywka.inflate(-50, -50)
        self.sluchawka_img = pygame.transform.scale(pygame.image.load(Rozpoczecie.sluchawka).convert_alpha(),
                                                                      (self.rect_sluchawki.width,
                                                                       self.rect_sluchawki.height))
        self.prognoza_video = pygame.movie.Movie(Rozpoczecie.prognoza_szaranczy)
        self.prognoza_soundtrack = pygame.mixer.Sound(os.path.join('film', 'prognoza_szaranczy.wav'))
        self.dzwiek_ratujcie_kwiaty = pygame.mixer.Sound(Rozpoczecie.ratujcie_kwiaty_nagranie)
        self.dlugosc_dzwieku = self.dzwiek_ratujcie_kwiaty.get_length()
        oryginalna_glosnosc = self.dzwiek_ratujcie_kwiaty.get_volume()
        self.dzwiek_ratujcie_kwiaty.set_volume(oryginalna_glosnosc * 0.2)
        self.dzwiek_wystartowany = False
        self.dzwiek_zakonczony = False
        self.czas_startu_video = None
        self.czas_startu_audio = None
        self.dlugosc_video = self.prognoza_video.get_length()
        self.film_wystartowany = False
        self.film_zakonczony = False
        self.soundtrack_wystartowany = False

    def wylicz_rect_logo(self):
        szerokosc = 0.4 * self.szerokosc
        wysokosc = 0.3 * self.wysokosc
        pos_x = 0.5 * self.szerokosc
        pos_y = 0.05 * self.wysokosc
        return pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)

    def on_entry(self):
        super(Rozpoczecie, self).on_entry()

    def on_exit(self):
        super(Rozpoczecie, self).on_exit()

    def on_clock_tick(self):
        if self.film_zakonczony:
            if not self.dzwiek_wystartowany:
                self.dzwiek_wystartowany = True
                self.dzwiek_ratujcie_kwiaty.play()
        return "rozpoczecie"

    def on_event(self, event):
        if self.film_zakonczony:
            decyzja = self.grac_ponownie(event)
            if decyzja == "TAK":
                return "wybor_pogromcy"
        return "rozpoczecie"

    def draw_sluchawka(self, screen):
        screen.blit(self.sluchawka_img, self.rect_sluchawki.topleft)

    def draw(self, screen):
        self.draw_title(screen)
        screen.blit(self.pygame_logo_img, self.rect_logo.topleft)
        if not self.soundtrack_wystartowany:
            self.czas_startu_audio = time.time()
            self.prognoza_soundtrack.play()
            self.soundtrack_wystartowany = True
        elif (not self.film_wystartowany) and (time.time() - self.czas_startu_audio > 2.0):
            self.czas_startu_video = time.time()
            self.prognoza_video.set_display(screen, self.rect_gameover)
            self.prognoza_video.play()
            self.film_wystartowany = True
        elif self.czas_startu_video and (time.time() - self.czas_startu_video > self.dlugosc_video):
            self.film_zakonczony = True
            self.draw_button_ok(screen)
            self.draw_sluchawka(screen)
