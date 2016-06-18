import pygame
def draw_pietro(screen):
    grubosc =15
    grubosc1 = 10
    black = (0,0,0)
    noga_pl = [(0,0),(0,660)]
    noga_pg = [(0,0),(1000,0)]
    noga_pd = [(0,660),(1000,660)]
    noga_pp = [(1000,660),(1000,0)]
    sciana_1 = [(0,460),(400,460)]
    sciana_2 = [(400,460),(400,600)]
    sciana_3 = [(500,0),(500,220)]
    sciana_4 = [(500,220),(400,220)]
    sciana_5 = [(0,220),(340,220)]
    sciana_6 = [(1000,480),(500,480)]
    sciana_7 = [(500,480),(500,520)]
    sciana_8 = [(500,660),(500,580)]

    pygame.draw.lines(screen, black, False, noga_pg, grubosc )
    pygame.draw.lines(screen, black, False, noga_pl, grubosc )
    pygame.draw.lines(screen, black, False, noga_pd, grubosc )
    pygame.draw.lines(screen, black, False, noga_pp, grubosc )
    pygame.draw.lines(screen, black, False, sciana_1, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_2, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_3, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_4, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_5, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_6, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_7, grubosc1 )
    pygame.draw.lines(screen, black, False, sciana_8, grubosc1 )

