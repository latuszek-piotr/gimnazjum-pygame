import pygame
import sys
from pygame.locals import QUIT
import time

# utworzenie okna
window = pygame.display.set_mode((1000, 660))
# ustawiamy tytul okna
pygame.display.set_caption('menu gry')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()
pygame.display.flip()
def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)
