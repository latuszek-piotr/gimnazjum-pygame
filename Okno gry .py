import pygame
import sys
from pygame.locals import QUIT
import time
# utworzenie okna
window = pygame.display.set_mode((1000, 660))
# ustawiamy tytul okna
pygame.display.set_caption('Niebywale trudny')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()
pygame.display.flip()
input(pygame.event.get)()
    grafika_lanckorony_menu = pygame.load.image(lanckorona_menu_glowne.jpg)()