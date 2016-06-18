import pygame

def draw_sale(screen, x, y):
    points=[(x,y),(x+100,y)]
    grubosc= 100
    kolor_ludka = (55,55,55)
    pygame.draw.lines(screen, kolor_ludka,  False, points, grubosc)
