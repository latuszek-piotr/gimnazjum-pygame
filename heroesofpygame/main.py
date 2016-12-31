import os
import sys
from pygame.locals import *
import pygame

from heroesofpygame.rozpoczecie import Rozpoczecie
from heroesofpygame.rozgrywka import Rozgrywka
from heroesofpygame.przegrana import Przegrana
from heroesofpygame.wygrana import Wygrana
from heroesofpygame.zakonczenie import Zakonczenie

from heroesofpygame import Pietro

from heroesofpygame.szarancza import Szarancza

clock = pygame.time.Clock()

os.environ["SDL_VIDEO_CENTERED"] = "1"

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("szkola_1_pietro")
srodek_ekranu = (650, 325)

########################### zmienne globalne
active_player_name = sys.argv[1]

szerokosc_ekranu = 1300
wysokosc_ekranu = 650
screen = pygame.display.set_mode((szerokosc_ekranu, wysokosc_ekranu))

stan_gry = "rozpoczecie"
stan_gry = "rozgrywka"  #mozliwe : "rozpoczecie", "rozgrywka", "przegrana", "wygrana", "zakonczenie"
# stan_gry = "przegrana"
# stan_gry = "wygrana"
# stan_gry = "zakonczenie"

rozpoczecie = Rozpoczecie(szerokosc_ekranu, wysokosc_ekranu)
rozgrywka = Rozgrywka(szerokosc_ekranu, wysokosc_ekranu, active_player_name)
przegrana = Przegrana(szerokosc_ekranu, wysokosc_ekranu)
wygrana = Wygrana(szerokosc_ekranu, wysokosc_ekranu)
zakonczenie = Zakonczenie(szerokosc_ekranu, wysokosc_ekranu)


######################################## inicjalizacja


def is_game_finished(event):
    running = True
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        running = False
    return running


# ---------------------------- glowna petla zdarzen pygame

rozgrywka.active_player.move_to(srodek_ekranu)  # TODO do on_entry() stanu rozgrywka
# rozgrywka.broadcast_active_player(active_player, rozgrywka.net_connection, action='join', await_confirmation=True)

running = True
screen.fill((0, 0, 0))

while running:

    clock.tick(60)

    for event in pygame.event.get():
        print event

        running = is_game_finished(event)

        ################################### Akcje na planszy gry zalezne od eventow pygame
        if stan_gry == "rozpoczecie":
            decyzja = rozpoczecie.grac_ponownie(event)
            if decyzja == "TAK":
                stan_gry = "rozgrywka"

        elif stan_gry == "wygrana":
            decyzja = wygrana.grac_ponownie(event)
            if decyzja == "TAK":
                stan_gry = "rozgrywka"
            elif decyzja == "NIE":
                stan_gry = "zakonczenie"

        elif stan_gry == "przegrana":
            decyzja = przegrana.grac_ponownie(event)
            if decyzja == "TAK":
                stan_gry = "rozgrywka"
            elif decyzja == "NIE":
                stan_gry = "zakonczenie"

        elif stan_gry == "zakonczenie":
            decyzja = zakonczenie.grac_ponownie(event)
            if decyzja == "NIE":
                running = False
                break

    ################################### Akcje na planszy gry niezalezne od eventow pygame
    if stan_gry == "rozgrywka":
        stan_gry = rozgrywka.handle_clock_tick()

    ################################### Rysowanie planszy gry

    if stan_gry == "rozpoczecie":
        rozpoczecie.draw(screen)
    elif stan_gry == "rozgrywka":
        screen.fill((0, 0, 0))
        # flower_1.draw(screen)   # to ma sie narysowac w sali
        # flower_2.draw(screen)
        # player1.draw(screen)
        # player2.draw(screen)
        # player3.draw(screen)
        # player4.draw(screen)
        rozgrywka.draw(screen)
    elif stan_gry == "wygrana":
        screen.fill((0, 0, 0))
        wygrana.draw(screen)
    elif stan_gry == "przegrana":
        screen.fill((0, 0, 0))
        przegrana.draw(screen)
    elif stan_gry == "zakonczenie":
        screen.fill((0, 0, 0))
        zakonczenie.draw(screen)

    pygame.display.flip()

#rozgrywka.broadcast_active_player(rozgrywka.active_player, rozgrywka.net_connection, action='leave')
