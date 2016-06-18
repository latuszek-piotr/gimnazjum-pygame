import Mapa
import pygame
import sys
from pygame.locals import QUIT
import time
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

nazwa_pliku = 'grafika/fugu.png'

def draw_figure(event, screen, x, y):
    global nazwa_pliku
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_p:
            nazwa_pliku = 'grafika/piotrek fugu'
        if event.key == pygame.K_f:
            nazwa_pliku = 'grafika/fugu.png'

        elif event.key == pygame.K_l:
            nazwa_pliku = 'grafika/ludzik1.png'

    grafika = pygame.image.load(nazwa_pliku).convert_alpha()
    szerokosc = grafika.get_width()
    wysokosc = grafika.get_height()
    grubosc = 5
    # screen.blit(grafika, (x-szerokosc/2, y-wysokosc/2))
    noga_l = [(x-10,y+40),(x+10,y+20),(x,y),(x,y-30),(x+10,y-20),(x+40,y-30),]
    noga_p = [(x+60,y+10),(x+30,y-10),(x,y),(x,y-30),(x-20,y-20),(x-30,y+10)]
    srodek_glowy = (x,y-45)
    promien_g = 15
    pygame.draw.lines(screen, blue, False, noga_p, grubosc )
    pygame.draw.lines(screen, blue, False, noga_l, grubosc )
    pygame.draw.circle(screen, blue, srodek_glowy, promien_g, grubosc)

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
ostatnio_x = 0
ostatnio_y = 0

def input(events):
    global ostatnio_x
    global ostatnio_y
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            sys.exit(0)

        else:
            screen.fill((blue))
            #x, y = pygame.mouse.get_pos()
            x, y = pobierz_wspolrzedne(event, ostatnio_x, ostatnio_y)
            screen.blit(grafika_wody, (0, 0))
            # pygame.draw.rect(screen, red, (0,0,500,660))
            #screen.blit(grafika_ryby, (x-szerokosc_ryby/2, y-wysokosc_ryby/2))
            draw_figure(event, screen, x, y)
            ostatnio_x, ostatnio_y = x, y
            Mapa.draw_pietro(screen)



            pygame.display.flip()
            if x < 500 :
                sound.play()
            else:
                # screen.blit(grafika_ogien, (500,330))
                pygame.display.flip()


blue = (0,0,255)
red = (255,0,0)

grafika_wody = pygame.image.load('grafika/woda.jpg')
grafika_ogien = pygame.image.load('grafika/ogien.jpg')
dz = open('dzwiek/jesterdie_03.wav')

pygame.mixer.init()
sound = pygame.mixer.Sound('dzwiek/jesterdie_03.wav')

while True:
    input(pygame.event.get())
x,y = pygame.mouse.get_pos()





