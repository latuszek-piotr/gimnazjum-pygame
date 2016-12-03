import pygame
import os
from player import Player


class Piotr(Player):
    happy_img = os.path.join('grafika', 'piotr_wesoly.png')
    sad_img = os.path.join('grafika', 'piotr_smutny.png')
    angry_img = os.path.join('grafika', 'piotr_zly.png')
    surprised_img = os.path.join('grafika', 'piotr_zdziwiony.png')
    scared_img = os.path.join('grafika', 'piotr_zdziwiony.png')  # TODO dorobic 'piotr_przestraszony.png')

    def __init__(self, pos=(350, 50), size=50):
        super(Piotr, self).__init__(pos, size)
        self.mood = 'happy'
        self.images = {'happy': pygame.transform.scale(pygame.image.load(Piotr.happy_img).convert_alpha(), (size, size+10)),
                       'sad': pygame.transform.scale(pygame.image.load(Piotr.sad_img).convert_alpha(), (size, size+10)),
                       'angry': pygame.transform.scale(pygame.image.load(Piotr.angry_img).convert_alpha(), (size, size+10)),
                       'suprised': pygame.transform.scale(pygame.image.load(Piotr.surprised_img).convert_alpha(), (size, size+10)),
                       'scared': pygame.transform.scale(pygame.image.load(Piotr.scared_img).convert_alpha(), (size, size+10))}

    def draw(self, screen):
        # Copy image to screen:
        img = self.images[self.mood]
        screen.blit(img, [self.rect.x, self.rect.y])
