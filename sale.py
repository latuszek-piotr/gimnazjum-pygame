import pygame

def draw_mapa (screen):
    grubosc=10
    kolor_sciany= (0,0,0)
    gorna_sciana= [(10,10),(990,10)]
    lewa_sciana=  [(10,10),(10,650)]
    dolna_sciana= [(10,650),(990,650)]
    prawa_sciana= [(990,10),(990,650)]
    pierwsza_sala= [(10,450),(250,450),(250,550)]
    druga_sala= [(750,10),(750,250),(860,250)]
    wielka_sala1= [(10,250),(250,250)]
    wielka_sala2= [(380,250),(500,250),(500,10)]
    duza_sala1= [(450,650),(450,450), (700,450)]
    duza_sala2= [(810,450),(990,450)]

    pygame.draw.lines(screen, kolor_sciany, False, gorna_sciana, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, lewa_sciana, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False,dolna_sciana, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, prawa_sciana, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, pierwsza_sala, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, druga_sala, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, wielka_sala1, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, wielka_sala2, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, duza_sala1, grubosc)
    pygame.draw.lines(screen, kolor_sciany, False, duza_sala2, grubosc)

