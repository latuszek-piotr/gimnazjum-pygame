# -*- coding: UTF-8 -*-
import pygame
import os
from heroesofpygame.stan_gry import StanGry
from heroesofpygame import statusbar


class WyborPogromcy(StanGry):
    piotr_wesoly = os.path.join('grafika', 'piotr_wesoly.png')
    piotr_smutny = os.path.join('grafika', 'piotr_smutny.png')
    wiktor_wesoly = os.path.join('grafika', 'wiktor_wesoly.png')
    wiktor_smutny = os.path.join('grafika', 'wiktor_zly.png')  # brak 'wiktor_smutny.png'
    dawid_wesoly = os.path.join('grafika', 'dawid_wesoly.png')
    dawid_smutny = os.path.join('grafika', 'dawid_smutny.png')
    dominik_wesoly = os.path.join('grafika', 'dominik_wesoly.png')
    dominik_smutny = os.path.join('grafika', 'dominik_smutny.png')
    tlo_pogromcy = os.path.join('grafika', 'tlo_pogromcy.png')
    tlo_pogromcy_h = os.path.join('grafika', 'tlo_pogromcy_highlighted.png')

    def __init__(self, szerokosc, wysokosc):
        super(WyborPogromcy, self).__init__()
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.tytul_okna = u"Wybierz pogromcę szarańczy"
        self.rect_tytulu = self.wylicz_rect_tytulu()
        self.rects_pogromcow = self.wylicz_rects_pogromcow()
        self.highlighted_rect = None
        self.font = pygame.font.SysFont("comic sans MS", 45, bold=True) #ustawienie czcionki
        self.font_tytulu = pygame.font.SysFont("comic sans MS", 80, bold=True) #ustawienie czcionki
        self.przesuniecie_zdjec = 15
        szerokosc_zdjec = int(0.5 * (self.rects_pogromcow[0].width - self.przesuniecie_zdjec*2))
        wysokosc_zdjec = int(0.5 * (self.rects_pogromcow[0].height - self.przesuniecie_zdjec*2))
        self.weseli = [pygame.transform.scale(pygame.image.load(WyborPogromcy.piotr_wesoly).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec)),
                       pygame.transform.scale(pygame.image.load(WyborPogromcy.wiktor_wesoly).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec)),
                       pygame.transform.scale(pygame.image.load(WyborPogromcy.dawid_wesoly).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec)),
                       pygame.transform.scale(pygame.image.load(WyborPogromcy.dominik_wesoly).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec))]
        self.smutni = [pygame.transform.scale(pygame.image.load(WyborPogromcy.piotr_smutny).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec)),
                       pygame.transform.scale(pygame.image.load(WyborPogromcy.wiktor_smutny).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec)),
                       pygame.transform.scale(pygame.image.load(WyborPogromcy.dawid_smutny).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec)),
                       pygame.transform.scale(pygame.image.load(WyborPogromcy.dominik_smutny).convert_alpha(), (szerokosc_zdjec, wysokosc_zdjec))]
        self.tlo = pygame.transform.scale(pygame.image.load(WyborPogromcy.tlo_pogromcy).convert_alpha(), (int(szerokosc_zdjec*2.4), wysokosc_zdjec*2))
        self.tlo_h = pygame.transform.scale(pygame.image.load(WyborPogromcy.tlo_pogromcy_h).convert_alpha(), (int(self.rects_pogromcow[0].width*1.15),
                                                                                                              self.rects_pogromcow[0].height))
        self.pogromcy = self.smutni[:]
        self.pogromcy_imiona = ["Piotr", "Wiktor", "Dawid", "Dominik"]
        self.wybrany_pogromca = ''

    def wylicz_rect_tytulu(self):
        return pygame.Rect(0, 0, self.szerokosc, 0.35 * self.wysokosc)

    def wylicz_rects_pogromcow(self):
        rects = []
        for idx_pogromcy in range(4):
            szerokosc = 0.25 * self.szerokosc
            wysokosc = self.wysokosc - self.rect_tytulu.height
            pos_x = idx_pogromcy * szerokosc
            pos_y = self.rect_tytulu.bottom
            rect = pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)
            rect.inflate_ip(-10,-10)
            rects.append(rect)
        return rects

    def on_entry(self):
        super(WyborPogromcy, self).on_entry()
        self.wybrany_pogromca = ''
        statusbar.daj_status().active_player_name = ''

    def on_exit(self):
        super(WyborPogromcy, self).on_exit()
        statusbar.daj_status().active_player_name = self.wybrany_pogromca

    def on_clock_tick(self):
        return "wybor_pogromcy"

    def on_event(self, event):
        self.wyroznij_wybieranego_pogromce(event)
        self.wybierz_pogromce(event)
        if self.wybrany_pogromca:
            return "rozgrywka"
        return "wybor_pogromcy"

    def wyroznij_wybieranego_pogromce(self, event):
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            self.highlighted_rect = None
            self.pogromcy = self.smutni[:]
            for idx, rect in enumerate(self.rects_pogromcow):
                if rect.collidepoint(pos):
                    self.highlighted_rect = rect
                    self.pogromcy[idx] = self.weseli[idx]

    def wybierz_pogromce(self, event):
        LEFT = 1
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            pos = pygame.mouse.get_pos()
            for idx, rect in enumerate(self.rects_pogromcow):
                if rect.collidepoint(pos):
                    self.wybrany_pogromca = self.pogromcy_imiona[idx]

    def draw_title(self, screen):
        text = self.font_tytulu.render(self.tytul_okna, False, (255,0,0))
        (width, height) = self.font_tytulu.size(self.tytul_okna)
        pozycja_napisu = (self.rect_tytulu.centerx - width/2, self.rect_tytulu.centery - height/2)
        screen.blit(text, pozycja_napisu)

    def draw_pogromcy(self, screen):
        # if self.highlighted_rect is not None:
        #     pygame.draw.rect(screen, (255,255,0), self.highlighted_rect)
        for idx, rect in enumerate(self.rects_pogromcow):
            if (self.highlighted_rect is not None) and (self.highlighted_rect == rect):
                tlo_img = self.tlo_h
                t_dx = 0
            else:
                tlo_img = self.tlo
                t_dx = self.przesuniecie_zdjec
            screen.blit(tlo_img, [rect.x + t_dx, rect.y + self.przesuniecie_zdjec])
            pogromca_img = self.pogromcy[idx]
            dx = (rect.width - pogromca_img.get_width()) / 2
            dy = (rect.height - pogromca_img.get_height()) / 2
            screen.blit(pogromca_img, [rect.x + dx, rect.y + dy])

    def draw(self, screen):
        screen.fill((0, 0, 0))
        self.draw_title(screen)
        self.draw_pogromcy(screen)

