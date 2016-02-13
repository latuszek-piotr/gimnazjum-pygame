import pygame
import sys
from pygame.locals import QUIT
import os
cwd = os.getcwd()
print cwd
print "Current directory = %s" % cwd
print "Directory contains: %s" % os.listdir(cwd)
print "'grafika' subdirectory contains: %s" % os.listdir(cwd+'/grafika')
# utworzenie okna
window = pygame.display.set_mode((1000, 660))
# ustawiamy tytul okna
pygame.display.set_caption('animacja ludzika')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()

pygame.display.flip()
for numer_ludzika in [1, 2, 3, 4, 5]:
    nazwa_pliku = 'grafika/ludzik%s.png' % numer_ludzika
    grafika_ludzik = pygame.image.load(nazwa_pliku)
    screen.blit(grafika_ludzik, (0,0))
    pygame.display.flip()

def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)

while True:
    input(pygame.event.get())