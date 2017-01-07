# -*- coding: UTF-8 -*-
import pygame


class Mapa(object):
    def __init__(self, sale):
        self.skala=1.2
        self.obszary_sal = self.daj_obszary_sal(sale)
        self.obszar_mapy = self.obszar_obejmujacy_wszystkie_sale()
        self.obszar_aktywnej_sali = None
        self.aktywna_sala_skala_x = 1
        self.aktywna_sala_skala_y = 1
        self.pos_szaranczy = []
        self.pos_kwiatow = []
        self.pos_graczy = []

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
        (x_start, y_start) = sala.daj_naroznik(ktory='lewy-gorny')
        (x_end, y_end) = sala.daj_naroznik(ktory='prawy-dolny')
        self.aktywna_sala_skala_x = self.obszar_aktywnej_sali.width / (x_end - x_start)
        self.aktywna_sala_skala_y = self.obszar_aktywnej_sali.height / (y_end - y_start)
        self.aktywna_sala_pos = (x_start, y_start)

    def ustaw_ilosc_szaranczy(self, ilosc_wszystkich_szaranczy):
        self.pos_szaranczy = [None for szarancza in range(ilosc_wszystkich_szaranczy)]

    def ustaw_ilosc_kwiatow(self, ilosc_wszystkich_kwiatow):
        self.pos_kwiatow = [None for kwiaty in range(ilosc_wszystkich_kwiatow)]

    def ustaw_ilosc_graczy(self, ilosc_wszystkich_graczy):
        self.pos_graczy = [None for gracz in range(ilosc_wszystkich_graczy)]

    def update_pozycji_szaranczy(self, idx_szaranczy, szarancza):
        if not self.obszar_aktywnej_sali:
            return
        if (szarancza.stan == "martwa") or (szarancza.stan == "anihilowana"):
            self.pos_szaranczy[idx_szaranczy] = None
            return
        rect = self.oblicz_rect_pozycji_obiektu(game_object=szarancza)
        self.pos_szaranczy[idx_szaranczy] = rect

    def update_pozycji_kwiatu(self, idx_kwiatu, kwiat):
        if kwiat.zjedzony:
            self.pos_kwiatow[idx_kwiatu] = None
            return
        rect = self.oblicz_rect_pozycji_obiektu(game_object=kwiat)
        self.pos_kwiatow[idx_kwiatu] = rect

    def update_pozycji_gracza(self, idx_gracza, gracz):
        rect = self.oblicz_rect_pozycji_obiektu(game_object=gracz)
        self.pos_graczy[idx_gracza] = rect

    def oblicz_rect_pozycji_obiektu(self, game_object):
        dx_obiektu_w_aktywnej_sali = game_object.rect.centerx - self.aktywna_sala_pos[0]
        dy_obiektu_w_aktywnej_sali = game_object.rect.centery - self.aktywna_sala_pos[1]
        dx_obiektu = dx_obiektu_w_aktywnej_sali * self.aktywna_sala_skala_x
        dy_obiektu = dy_obiektu_w_aktywnej_sali * self.aktywna_sala_skala_y
        rect = pygame.Rect(self.obszar_aktywnej_sali.left + dx_obiektu, self.obszar_aktywnej_sali.top + dy_obiektu, 2, 2)
        return rect

    def obszar_obejmujacy_wszystkie_sale(self):
        min_left = min([rect.left for rect in self.obszary_sal])
        min_top = min([rect.top for rect in self.obszary_sal])
        max_right = max([rect.right for rect in self.obszary_sal])
        max_bottom = max([rect.bottom for rect in self.obszary_sal])
        obszar = pygame.Rect(min_left, min_top, max_right - min_left, max_bottom - min_top)
        return obszar

    def draw_obrys(self, screen, rect, color=(255,255,255), grubosc_linii=1):
        pygame.draw.lines(screen, color, True, [rect.topleft, rect.bottomleft, rect.bottomright, rect.topright], grubosc_linii)

    def draw_pozycje_obiektow(self, screen, color, game_objects):
        for rect_obiektu in game_objects:
            if rect_obiektu is not None:
                pygame.draw.rect(screen, color, rect_obiektu)

    def draw(self, screen):
        # pygame.draw.rect(screen, (0,0,0), self.obszar_mapy)
        self.draw_obrys(screen, self.obszar_mapy, color=(255,255,0))
        for sala_rect in self.obszary_sal:
            self.draw_obrys(screen, sala_rect)
        if self.obszar_aktywnej_sali:
            self.draw_obrys(screen, self.obszar_aktywnej_sali, color=(75, 5, 205), grubosc_linii=2)
        self.draw_pozycje_obiektow(screen, color=(255,0,0), game_objects=self.pos_szaranczy)
        self.draw_pozycje_obiektow(screen, color=(0,255,0), game_objects=self.pos_kwiatow)
        self.draw_pozycje_obiektow(screen, color=(255,255,0), game_objects=self.pos_graczy)
