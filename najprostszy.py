__author__ = 'programista'
import pygame
import sys
from pygame.locals import QUIT

pygame.init()
# utworzenie okna
window = pygame.display.set_mode((999, 660))


def input(events):
    for event in events:
        if event.type == QUIT:
            print "harakiri"
            print event
            sys.exit(0)
        else:
            print event
            # dzialaj az do przerwania
# x = 10
while True:
    input(pygame.event.get())
    # print x
    # x = x - 1
