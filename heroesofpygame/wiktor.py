import pygame
import os
from player import Player


class Wiktor(Player):
    happy_img = os.path.join('grafika', 'wiktor_wesoly.png')
    sad_img = os.path.join('grafika', 'wiktor_smutny.png')
    angry_img = os.path.join('grafika', 'wiktor_zly.png')
    surprised_img = os.path.join('grafika', 'wiktor_zdziwiony.png')
    scared_img = os.path.join('grafika', 'wiktor_przestraszony.png')

    def __init__(self, pos=(410, 100), size=50):
        super(Wiktor, self).__init__(pos, size)
        self.mood = 'sad'
        self.img = pygame.transform.scale(pygame.image.load(Wiktor.happy_img).convert_alpha(), (size, size+10))

    def draw(self, screen):
        super(Wiktor, self).draw(screen)
        # Copy image to screen:
        screen.blit(self.img, [self.rect.x, self.rect.y])

    def zmien_humor(self, mood):
        self.mood = mood
