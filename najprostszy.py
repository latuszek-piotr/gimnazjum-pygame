__author__ = 'programista'
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
# utworzenie okna
window = pygame.display.set_mode((1500, 660))
# ustawiamy tytul okna
pygame.display.set_caption('najprostszy')

# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()

# ladujemy pliki graficzne
grafika_slonca = pygame.image.load('sun.jpg')
grafika_jablko = pygame.image.load('jablko.jpg')
# przypisanie grafiki do okreslonego miejsca ekranu
screen.blit(grafika_slonca, (0,0))
screen.blit(grafika_jablko, (1000,100))
# pokaz grafike, odswiez zawartosc ekranu
pygame.display.flip()

def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            print event
            sys.exit(0)
        else:
            print event
            # dzialaj az do przerwania
# x = 10
while True:
    input(pygame.event.get())
    # print x
    # x = x - 1
