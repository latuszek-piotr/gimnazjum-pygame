import pygame
import sys
from pygame.locals import QUIT
import time

# utworzenie okna
window = pygame.display.set_mode((1000, 660))
# ustawiamy tytul okna
pygame.display.set_caption('animacja luku')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()
pygame.display.flip()

for (x, y) in [(0, 0), (15, 15), (30, 30), (45, 45), (60, 60)]:
    for numer_luku in range(5):
        nazwa_pliku = 'grafika/luk_%s.jpg' % (numer_luku+1)
        grafika_luku = pygame.image.load(nazwa_pliku)
        screen.blit(grafika_luku, (x, y))
        pygame.display.flip()
        time.sleep(0.1)

def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)

while True:
    input(pygame.event.get())