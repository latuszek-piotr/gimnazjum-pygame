import pygame
import os
from player import Player


class Dominik(Player):
    happy_img = os.path.join('grafika', 'dominik_wesoly.png')
    sad_img = os.path.join('grafika', 'dominik_smutny.png')
    angry_img = os.path.join('grafika', 'dominik_zly.png')
    surprised_img = os.path.join('grafika', 'dominik_zdziwiony.png')
    scared_img = os.path.join('grafika', 'dominik_przestraszony.png')

    def __init__(self, pos=(380, 70), size=50):
        super(Dominik, self).__init__(pos, size)
        self.mood = 'happy'
        self.images = {'happy': pygame.transform.scale(pygame.image.load(Dominik.happy_img).convert_alpha(), (size, size+10)),
                       'sad': pygame.transform.scale(pygame.image.load(Dominik.sad_img).convert_alpha(), (size, size+10)),
                       'angry': pygame.transform.scale(pygame.image.load(Dominik.angry_img).convert_alpha(), (size, size+10)),
                       'suprised': pygame.transform.scale(pygame.image.load(Dominik.surprised_img).convert_alpha(), (size, size+10)),
                       'scared': pygame.transform.scale(pygame.image.load(Dominik.scared_img).convert_alpha(), (size, size+10))}

    def draw(self, screen):
        super(Dominik, self).draw(screen)
        # Copy image to screen:
        img = self.images[self.mood]
        screen.blit(img, [self.rect.x, self.rect.y])

    def zmien_humor(self, mood):
        self.mood = mood
