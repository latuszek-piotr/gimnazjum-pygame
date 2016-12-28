import pygame
import os
from heroesofpygame.okno_wyboru import OknoWyboru


class Zakonczenie(OknoWyboru):
    pygame_logo = os.path.join('grafika', 'pygame_logo.png')

    def __init__(self, szerokosc, wysokosc):
        super(Zakonczenie, self).__init__(szerokosc, wysokosc, "Heroes of", button_ok=False, button_play_text1="Start", button_play_text2="")
        self.rect_tytulu.left = 0.05 * self.szerokosc
        self.rect_logo = self.wylicz_rect_logo()
        self.pygame_logo_img = pygame.transform.scale(pygame.image.load(Zakonczenie.pygame_logo).convert_alpha(),
                                                                        (self.rect_logo.width, self.rect_logo.height))

    def wylicz_rect_logo(self):
        szerokosc = 0.4 * self.szerokosc
        wysokosc = 0.3 * self.wysokosc
        pos_x = 0.5 * self.szerokosc
        pos_y = 0.05 * self.wysokosc
        return pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)

    def draw(self, screen):
        super(Zakonczenie, self).draw(screen)
        screen.blit(self.pygame_logo_img, self.rect_logo.topleft)

        text = self.font.render(" Autorzy:", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 0])

        text = self.font.render("    Wiktor Powroznik", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 50])

        text = self.font.render("    Piotr Latuszek", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 100])

        text = self.font.render("    Dawid Puka", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 150])

        text = self.font.render("    Dominik Matula", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 200])

        text = self.font.render(" Opieka programistyczna:", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 300])

        text = self.font.render("    mgr inz Grzegorz Latuszek", False, (255,255,255))
        screen.blit(text, [self.rect_rozgrywka.left + 50, self.rect_rozgrywka.top + 350])
