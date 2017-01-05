# -*- coding: UTF-8 -*-
import pygame


class Mapa(object):
    def __init__(self, sale):
        self.skala=1.2
        self.obszary_sal = self.daj_obszary_sal(sale)
        self.obszar_mapy = self.obszar_obejmujacy_wszystkie_sale()
        self.obszar_aktywnej_sali = None

    def daj_obszary_sal(self, sale):
        obszary = []
        skala = self.skala
        for sala in sale:
            obszar = pygame.Rect(sala.pos[0]*skala, sala.pos[1]*skala, sala.room_width*skala, sala.room_length*skala)
            obszary.append(obszar)
        return obszary

    def ustaw_aktywna_sale(self, sala):
        skala = self.skala
        self.obszar_aktywnej_sali = pygame.Rect(sala.pos[0]*skala, sala.pos[1]*skala, sala.room_width*skala, sala.room_length*skala)

    def obszar_obejmujacy_wszystkie_sale(self):
        min_left = min([rect.left for rect in self.obszary_sal])
        min_top = min([rect.top for rect in self.obszary_sal])
        max_right = max([rect.right for rect in self.obszary_sal])
        max_bottom = max([rect.bottom for rect in self.obszary_sal])
        obszar = pygame.Rect(min_left, min_top, max_right - min_left, max_bottom - min_top)
        return obszar

    def draw_obrys(self, screen, rect, color=(255,255,255), grubosc_linii=1):
        pygame.draw.lines(screen, color, True, [rect.topleft, rect.bottomleft, rect.bottomright, rect.topright], grubosc_linii)

    def draw(self, screen):
        # pygame.draw.rect(screen, (0,0,0), self.obszar_mapy)
        self.draw_obrys(screen, self.obszar_mapy, color=(255,255,0))
        for sala_rect in self.obszary_sal:
            self.draw_obrys(screen, sala_rect)
        if self.obszar_aktywnej_sali:
            self.draw_obrys(screen, self.obszar_aktywnej_sali, color=(75, 5, 205), grubosc_linii=2)
