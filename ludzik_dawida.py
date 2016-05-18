import pygame
import sys
from pygame.locals import QUIT
import time


ostatnio_x = 0
ostatnio_y = 0
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
grafika_wody = pygame.image.load('grafika/woda.jpg')

def pobierz_wspolrzedne(event, x, y):
    if event.type == pygame.KEYDOWN:
        delta_x = 0
        delta_y = 0
        if event.key == pygame.K_LEFT:
            delta_x = -20
        if event.key == pygame.K_RIGHT:
            delta_x = 20
        if event.key == pygame.K_UP:
            delta_y = -20
        if event.key == pygame.K_DOWN:
            delta_y = 20
        x = x + delta_x
        y = y + delta_y
    elif event.type == pygame.MOUSEMOTION:
        x, y = pygame.mouse.get_pos()
    return x, y


def draw_ludek(screen, x, y):
    grubosc=7
    kolor_ludka = red
    pygame.draw.circle(screen, kolor_ludka, (x,y-60), 20, 20)
    points=[(x-30,y+60), (x-40,y+50), (x-10, y+30), (x,y), (x, y-40), (x+10, y-20), (x+30, y-10), (x+30, y-20)]
    pygame.draw.lines(screen, kolor_ludka,  False, points, grubosc)
    points=[(x,y), (x+10, y+40), (x, y+70), (x+15,y+70)]
    pygame.draw.lines(screen, kolor_ludka, False, points, grubosc)
    points=[(x,y),(x, y-40), (x+40, y-40)]
    pygame.draw.lines(screen, kolor_ludka, False, points, grubosc)
    pygame.draw.circle(screen, kolor_ludka, (x+40,y-40), 10, 10)


def input(events):
    global ostatnio_x
    global ostatnio_y
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)

        else:
            screen.fill((blue))
            x, y = pobierz_wspolrzedne(event, ostatnio_x, ostatnio_y)
            screen.blit(grafika_wody, (0, 0))

            # draw_figure(event, screen, x, y)
            draw_ludek(screen, x, y)
            ostatnio_x, ostatnio_y = x, y

            pygame.display.flip()

##################################################################
# start programu
##################################################################

window = pygame.display.set_mode((1000, 660))
# ustawiamy tytul okna
pygame.display.set_caption('animacja luku')
# pobieramy informacje o ekranie - tle
screen = pygame.display.get_surface()
pygame.display.flip()

while True:
    input(pygame.event.get())
x,y = pygame.mouse.get_pos()





