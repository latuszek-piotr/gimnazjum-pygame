import os
import sys
from pygame.locals import *
import pygame

from heroesofpygame.rozpoczecie import Rozpoczecie
from heroesofpygame.rozgrywka import Rozgrywka
from heroesofpygame.przegrana import Przegrana
from heroesofpygame.wygrana import Wygrana
from heroesofpygame.zakonczenie import Zakonczenie

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("szkola_1_pietro")

########################### zmienne globalne
active_player_name = sys.argv[1]

szerokosc_ekranu = 1300
wysokosc_ekranu = 650
screen = pygame.display.set_mode((szerokosc_ekranu, wysokosc_ekranu))

rozpoczecie = Rozpoczecie(szerokosc_ekranu, wysokosc_ekranu)
rozgrywka = Rozgrywka(szerokosc_ekranu, wysokosc_ekranu, active_player_name)
przegrana = Przegrana(szerokosc_ekranu, wysokosc_ekranu)
wygrana = Wygrana(szerokosc_ekranu, wysokosc_ekranu)
zakonczenie = Zakonczenie(szerokosc_ekranu, wysokosc_ekranu)

mozliwe_stany_gry = {"rozpoczecie": rozpoczecie,
                     "rozgrywka": rozgrywka,
                     "przegrana": przegrana,
                     "wygrana": wygrana,
                     "zakonczenie": zakonczenie,
                     "the-end": zakonczenie}

######################################## inicjalizacja

def is_game_finished(event):
    finished = False
    if event.type == pygame.QUIT:
        finished = True
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        finished = True
    return finished


def zmien_stan_gry(obecny_stan, nowy_stan_gry):
    if obecny_stan and (not obecny_stan.zakonczony):
        obecny_stan.on_exit()
    nowy_stan = mozliwe_stany_gry[nowy_stan_gry]
    if nowy_stan and (not nowy_stan.zaczety):
        nowy_stan.on_entry()
    return nowy_stan

stan_gry = "rozgrywka" #"rozpoczecie"
obecny_stan = zmien_stan_gry(None, stan_gry)

# ---------------------------- glowna petla zdarzen pygame

running = True
screen.fill((0, 0, 0))

while running:

    clock.tick(60)

    for event in pygame.event.get():
        print event

        if is_game_finished(event):
            running = False
            break

        #--------------------------------------------- Akcje na planszy gry zalezne od eventow pygame
        nowy_stan_gry = obecny_stan.on_event(event)
        if nowy_stan_gry != stan_gry:
            obecny_stan = zmien_stan_gry(obecny_stan, nowy_stan_gry)
            stan_gry = nowy_stan_gry

    #------------------------------------------------- Akcje na planszy gry niezalezne od eventow pygame
    nowy_stan_gry = obecny_stan.on_clock_tick()
    if nowy_stan_gry != stan_gry:
        obecny_stan = zmien_stan_gry(obecny_stan, nowy_stan_gry)
        stan_gry = nowy_stan_gry


    ################################### Rysowanie planszy gry

    obecny_stan.draw(screen)
    pygame.display.flip()

#rozgrywka.broadcast_active_player(rozgrywka.active_player, rozgrywka.net_connection, action='leave')
