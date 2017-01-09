import pygame
import os
from player import Player


class Wiktor(Player):
    happy_img = os.path.join('grafika', 'wiktor_wesoly.png')
    sad_img = os.path.join('grafika', 'wiktor_zly.png')  # brak 'wiktor_smutny.png'
    angry_img = os.path.join('grafika', 'wiktor_zly.png')
    surprised_img = os.path.join('grafika', 'wiktor_zdziwiony.png')
    scared_img = os.path.join('grafika', 'wiktor_przestraszony.png')

    def __init__(self, pos=(410, 100), size=50):
        super(Wiktor, self).__init__(pos, size)
        self.mood = 'happy'
        self.images = {'happy': pygame.transform.scale(pygame.image.load(Wiktor.happy_img).convert_alpha(), (size, size+10)),
                       'sad': pygame.transform.scale(pygame.image.load(Wiktor.sad_img).convert_alpha(), (size, size+10)),
                       'angry': pygame.transform.scale(pygame.image.load(Wiktor.angry_img).convert_alpha(), (size, size+10)),
                       'suprised': pygame.transform.scale(pygame.image.load(Wiktor.surprised_img).convert_alpha(), (size, size+10)),
                       'scared': pygame.transform.scale(pygame.image.load(Wiktor.scared_img).convert_alpha(), (size, size+10))}

    def draw(self, screen):
        super(Wiktor, self).draw(screen)
        # Copy image to screen:
        img = self.images[self.mood]
        screen.blit(img, [self.rect.x, self.rect.y])

    def zmien_humor(self, mood):
        self.mood = mood
