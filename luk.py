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

# for (x, y) in [(0, 0), (15, 15), (30, 30), (45, 45), (60, 60)]:
#     for numer_luku in range(5):
#         nazwa_pliku = 'grafika/luk_%s.jpg' % (numer_luku+1)
#         grafika_luku = pygame.image.load(nazwa_pliku)
#         screen.blit(grafika_luku, (x, y))
#         pygame.display.flip()
#         time.sleep(0.1)

def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)

blue = (0,0,255)
red = (255,0,0)
nazwa_pliku = 'grafika/fugu.png'
grafika_ryby = pygame.image.load(nazwa_pliku).convert_alpha()
szerokosc_ryby = grafika_ryby.get_width()
wysokosc_ryby = grafika_ryby.get_height()

dz = open('dzwiek/jesterdie_03.wav')

pygame.mixer.init()
sound = pygame.mixer.Sound('dzwiek/jesterdie_03.wav')
sound.play()
while True:
    input(pygame.event.get())
    screen.fill((blue))
    x, y = pygame.mouse.get_pos()
    pygame.draw.rect(screen,red , (0,0,500,660))
    screen.blit(grafika_ryby, (x-szerokosc_ryby/2, y-wysokosc_ryby/2))
    pygame.display.flip()
    if x < 500 :
        sound.play()

