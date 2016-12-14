import pygame
import sys
from pygame.locals import QUIT
import os
import time
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

for powturzenia in range(50):
    for numer_mur in range(5):
        nazwa_pliku = 'grafika/mur%s.jpg' % (numer_mur+1)
        grafika_mur = pygame.image.load(nazwa_pliku)
        screen.blit(grafika_mur, (0,0))
        pygame.display.flip()
        time.sleep(0.25)

def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)

while True:
    input(pygame.event.get())