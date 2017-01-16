# -*- coding: UTF-8 -*-
import pygame


class Mapa(object):
    def __init__(self, sale):
        self.skala_podgladu = 2.5
        self.skala_terenu = 10.0
        self.obrysy_podgladu_sal = self.daj_obrysy_sal(sale, self.skala_podgladu)
        self.obszary_sal = self.daj_obszary_sal(sale, self.skala_terenu)
        self.indeksy_sal = {sala.nazwa: idx for (idx, sala) in enumerate(sale)}
        self.obszar_mapy = self.obszar_obejmujacy_wszystkie_sale(self.obszary_sal)
        self.obrys_aktywnej_sali = None
        self.dict_pos_szaranczy = {}
        self.pos_kwiatow = []
        self.pos_graczy = []

    def daj_obszary_sal(self, sale, skala):
        obszary = []
        for sala in sale:
            obszar = pygame.Rect(sala.pos[0]*skala, sala.pos[1]*skala, sala.room_width*skala, sala.room_length*skala)
            obszary.append(obszar)
        return obszary

    def daj_obrysy_sal(self, sale, skala):
        obrysy = []
        for sala in sale:
            obrys = sala.daj_obrys_sali(skala)
            obrysy.append(obrys)
        return obrysy

    def ustaw_aktywna_sale(self, sala):
        idx_sali = self.indeksy_sal[sala.nazwa]
        self.obrys_aktywnej_sali = self.obrysy_podgladu_sal[idx_sali]

    def ustaw_szarancze(self, wszystkie_szarancze):
        self.dict_pos_szaranczy = {id(szarancza): None for szarancza in wszystkie_szarancze}

    def ustaw_ilosc_kwiatow(self, ilosc_wszystkich_kwiatow):
        self.pos_kwiatow = [None for kwiaty in range(ilosc_wszystkich_kwiatow)]

    def ustaw_ilosc_graczy(self, ilosc_wszystkich_graczy):
        self.pos_graczy = [None for gracz in range(ilosc_wszystkich_graczy)]

    def update_pozycji_szaranczy(self, szarancza):
        if not self.obrys_aktywnej_sali:
            return
        if (szarancza.stan == "martwa") or (szarancza.stan == "anihilowana"):
            self.dict_pos_szaranczy[id(szarancza)] = None
            return
        rect = self.oblicz_rect_pozycji_w_terenie(game_object=szarancza)
        self.dict_pos_szaranczy[id(szarancza)] = rect

    def update_pozycji_kwiatu(self, idx_kwiatu, kwiat, sala):
        if kwiat.zjedzony:
            self.pos_kwiatow[idx_kwiatu] = None
            return
        rect = self.oblicz_rect_pozycji_w_terenie(game_object=kwiat)
        self.pos_kwiatow[idx_kwiatu] = rect

    def update_pozycji_gracza(self, idx_gracza, gracz):
        rect = self.oblicz_rect_pozycji_w_terenie(game_object=gracz)
        self.pos_graczy[idx_gracza] = rect

    def oblicz_rect_pozycji_w_terenie(self, game_object):
        (x, y) = game_object.pos_teren
        x = (x / 10.0 ) * self.skala_podgladu
        y = (y / 10.0 ) * self.skala_podgladu
        rect = pygame.Rect(x - 2, y - 2, 4, 4)
        return rect

    def obszar_obejmujacy_wszystkie_sale(self, obszary_sal):
        min_left = min([rect.left for rect in obszary_sal])
        min_top = min([rect.top for rect in obszary_sal])
        max_right = max([rect.right for rect in obszary_sal])
        max_bottom = max([rect.bottom for rect in obszary_sal])
        obszar = pygame.Rect(min_left, min_top, max_right - min_left, max_bottom - min_top)
        return obszar

    def draw_obrys(self, screen, punkty_obrysu, color=(255,255,255), grubosc_linii=1):
        pygame.draw.lines(screen, color, True, punkty_obrysu, grubosc_linii)

    def draw_pozycje_obiektow(self, screen, color, game_objects):
        for rect_obiektu in game_objects:
            if rect_obiektu is not None:
                pygame.draw.rect(screen, color, rect_obiektu)

    def draw(self, screen):
        for sala_obrys in self.obrysy_podgladu_sal:
            self.draw_obrys(screen, sala_obrys)
        if self.obrys_aktywnej_sali:
            self.draw_obrys(screen, self.obrys_aktywnej_sali, color=(255,255,0), grubosc_linii=2)
        self.draw_pozycje_obiektow(screen, color=(255,0,0), game_objects=self.dict_pos_szaranczy.values())
        self.draw_pozycje_obiektow(screen, color=(0,255,0), game_objects=self.pos_kwiatow)
        self.draw_pozycje_obiektow(screen, color=(255,255,0), game_objects=self.pos_graczy)
