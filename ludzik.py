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
window = pygame.display.set_mode((1100, 1600))
# ustawiamy tytul okna
pygame.display.set_caption('animacja ludzika')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()
pygame.display.flip()

for powturzenia in range(50):
    for numer_ludzika in range(7):
        nazwa_pliku = 'grafika/ludzik%s.png' % (numer_ludzika+1)
        grafika_ludzik = pygame.image.load(nazwa_pliku)
        screen.blit(grafika_ludzik, (0,0))
        pygame.display.flip()
        time.sleep(0.76)

def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiiiiiiri"
            sys.exit(0)

while True:
    input(pygame.event.get())
    import numpy

    def sound_data(frequency, length, amplitude=1, sample_rate=44100):
        time_points = numpy.linspace(0, length, length*sample_rate)    # lista kolejnych punktow czasowych

    data = numpy.sin(2*numpy.pi*frequency*time_points)             # lista wartosci sin dla kolejnych czasow
    data = amplitude*data

    'return'(data)