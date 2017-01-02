import pygame
import os
from player import Player


class Dawid(Player):
    happy_img = os.path.join('grafika', 'dawid_wesoly.png')
    sad_img = os.path.join('grafika', 'dawid_smutny.png')
    angry_img = os.path.join('grafika', 'dawid_zly.png')
    surprised_img = os.path.join('grafika', 'dawid_zdziwiony.png')
    scared_img = os.path.join('grafika', 'dawid_przestraszony.png')

    def __init__(self, pos=(440, 120), size=50):
        super(Dawid, self).__init__(pos, size)
        self.mood = 'happy'
        self.img = pygame.transform.scale(pygame.image.load(Dawid.happy_img).convert_alpha(), (size, size+10))

    def draw(self, screen):
        super(Dawid, self).draw(screen)
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])
