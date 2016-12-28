# -*- coding: UTF-8 -*-
import pygame
import os

class OknoWyboru(object):
    green_depressed = os.path.join('grafika', 'button', 'green_depressed.png')
    green_pressed = os.path.join('grafika', 'button', 'green_pressed.png')
    red_depressed = os.path.join('grafika', 'button', 'red_depressed.png')
    red_pressed = os.path.join('grafika', 'button', 'red_pressed.png')

    def __init__(self, szerokosc, wysokosc, tytul_okna, button_ok=True, button_quit=True, button_play_text1="Ponowna", button_play_text2="rozgrywka"):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.tytul_okna = tytul_okna
        self.button_ok = button_ok
        self.button_quit = button_quit
        self.button_play_text1 = button_play_text1
        self.button_play_text2 = button_play_text2
        self.rect = pygame.Rect(0,0, self.szerokosc, self.wysokosc)
        self.rect_tytulu = self.wylicz_rect_tytulu()
        self.rect_rozgrywka = self.wylicz_button_rozgrywki()
        self.button_green_depressed = pygame.transform.scale(pygame.image.load(OknoWyboru.green_depressed).convert_alpha(),
                                                                               (self.rect_rozgrywka.width, self.rect_rozgrywka.height))
        self.button_green_pressed = pygame.transform.scale(pygame.image.load(OknoWyboru.green_pressed).convert_alpha(),
                                                                             (self.rect_rozgrywka.width, self.rect_rozgrywka.height))
        self.button_rozgrywka = self.button_green_depressed
        self.rect_gameover = self.wylicz_button_gameover()
        self.button_red_depressed = pygame.transform.scale(pygame.image.load(OknoWyboru.red_depressed).convert_alpha(),
                                                                             (self.rect_rozgrywka.width, self.rect_rozgrywka.height))
        self.button_red_pressed = pygame.transform.scale(pygame.image.load(OknoWyboru.red_pressed).convert_alpha(),
                                                                           (self.rect_rozgrywka.width, self.rect_rozgrywka.height))
        self.button_gameover = self.button_red_depressed
        self.pressed_button = ''
        self.font = pygame.font.SysFont("comic sans MS", 45, bold=True) #ustawienie czcionki
        self.font_wyniku = pygame.font.SysFont("comic sans MS", 95, bold=True) #ustawienie czcionki

    def wylicz_rect_tytulu(self):
        szerokosc = 0.6 * self.szerokosc
        wysokosc = 0.4 * self.wysokosc
        pos_x = 0.2 * self.szerokosc
        pos_y = 0.05 * self.wysokosc
        return pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)

    def wylicz_button_rozgrywki(self):
        szerokosc_buttonu = 0.5 * self.szerokosc
        wysokosc_buttonu = 0.7 * self.wysokosc
        pos_x_buttonu = 0.0 * self.szerokosc
        pos_y_buttonu = 0.3 * self.wysokosc
        return pygame.Rect(pos_x_buttonu, pos_y_buttonu, szerokosc_buttonu, wysokosc_buttonu)

    def wylicz_button_gameover(self):
        szerokosc_buttonu = 0.5 * self.szerokosc
        wysokosc_buttonu = 0.7 * self.wysokosc
        pos_x_buttonu = 0.5 * self.szerokosc
        pos_y_buttonu = 0.3 * self.wysokosc
        return pygame.Rect(pos_x_buttonu, pos_y_buttonu, szerokosc_buttonu, wysokosc_buttonu)

    def grac_ponownie(self, event):
        LEFT = 1
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            if (self.pressed_button == 'rozgrywka') and (not self.rect_rozgrywka.collidepoint(pos)):
                self.button_rozgrywka = self.button_green_depressed
                self.pressed_button = ''
            elif (self.pressed_button == 'gameover') and (not self.rect_gameover.collidepoint(pos)):
                self.button_gameover = self.button_red_depressed
                self.pressed_button = ''
        elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            if (self.pressed_button == 'rozgrywka'):
                self.button_rozgrywka = self.button_green_depressed
                self.pressed_button = ''
                return "TAK"
            elif (self.pressed_button == 'gameover'):
                self.button_gameover = self.button_red_depressed
                self.pressed_button = ''
                return "NIE"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            pos = pygame.mouse.get_pos()
            if self.button_ok and self.rect_rozgrywka.collidepoint(pos):
                self.button_rozgrywka = self.button_green_pressed
                self.pressed_button = 'rozgrywka'
            elif self.button_quit and self.rect_gameover.collidepoint(pos):
                self.button_gameover = self.button_red_pressed
                self.pressed_button = 'gameover'
        return None

    def draw(self, screen):
        text = self.font_wyniku.render(self.tytul_okna, False, (255,0,0))
        screen.blit(text, [self.rect_tytulu.x + 20, self.rect_tytulu.y + 20])

        if self.button_ok:
            screen.blit(self.button_rozgrywka, self.rect_rozgrywka.topleft)
            text = self.font.render(self.button_play_text1, False, (0,0,0))
            screen.blit(text, [self.rect_rozgrywka.centerx - 100, self.rect_rozgrywka.centery - 70])
            text = self.font.render(self.button_play_text2, False, (0,0,0))
            screen.blit(text, [self.rect_rozgrywka.centerx - 100, self.rect_rozgrywka.centery + 10])

        if self.button_quit:
            screen.blit(self.button_gameover, self.rect_gameover.topleft)
            text = self.font.render(u"Wyjdź", False, (0,0,0))
            screen.blit(text, [self.rect_gameover.centerx - 100, self.rect_gameover.centery - 70])
            text = self.font.render("z gry", False, (0,0,0))
            screen.blit(text, [self.rect_gameover.centerx - 100, self.rect_gameover.centery + 10])

