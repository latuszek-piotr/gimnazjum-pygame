import pygame
import sys
from pygame.locals import QUIT
import time
pygame.init()
# utworzenie okna
window = pygame.display.set_mode((1000, 660))
# ustawiamy tytul okna
pygame.display.set_caption('Heroes of PyGame')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()
# ladujemy pliki graficzne
grafika_lanc_menu = pygame.image.load('grafika/lanckorona_menu_glowne.jpg')
# przypisanie grafiki do okreslonego miejsca ekranu
screen.blit(grafika_lanc_menu, (50,50))
# pokaz grafike, odswiez zawartosc ekranu
pygame.display.flip()

def input(events):
    for event in events:
        if event.type == QUIT:
            print event
            sys.exit(0)
        else:
            print event
while True:
    input(pygame.event.get())

