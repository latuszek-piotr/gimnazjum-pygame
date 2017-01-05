# -*- coding: UTF-8 -*-
import pygame


class Mapa(object):
    def __init__(self, sale):
        self.obszary_sal = self.daj_obszary_sal(sale, skala=1.5)
        self.obszar_mapy = self.obszar_obejmujacy_wszystkie_sale()

    def daj_obszary_sal(self, sale, skala=1):
        obszary = []
        for sala in sale:
            obszar = pygame.Rect(sala.pos[0]*skala, sala.pos[1]*skala, sala.room_width*skala, sala.room_length*skala)
            obszary.append(obszar)
        return obszary

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
        pygame.draw.rect(screen, (80,80,80), self.obszar_mapy)
        for sala_rect in self.obszary_sal:
            self.draw_obrys(screen, sala_rect)
        self.draw_obrys(screen, self.obszar_mapy, color=(255,255,0))
