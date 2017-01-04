import pygame
import os
import random


class Flower(object):
    flowers_img = [  os.path.join('grafika', 'flower.png'),
                     os.path.join('grafika', 'kwiat.jpg'),
                     os.path.join('grafika', 'flower1.png'),
                     os.path.join('grafika', 'flower2.png'),
                     os.path.join('grafika', 'flower3.png'),
                     os.path.join('grafika', 'flower4.png'),
                     os.path.join('grafika', 'kwiat.jpg')]


    def __init__(self, pos=(410, 300), size=50):
        selected_img =random.choice(Flower.flowers_img)
        self.pos = pos
        self.img = pygame.transform.scale(pygame.image.load(selected_img).convert_alpha(), (size, size+10))
        self.rect = pygame.Rect(pos[0]+20, pos[1]+10, 10, 10)  # rect kolizji jest mniejszy od rect obrazka
        self.zjedzony = False

    def draw(self, screen):
        # Copy image to screen:
        screen.blit(self.img, self.pos)
        if self.zjedzony:
            img_rect = self.img.get_rect().move(self.pos)
            pygame.draw.lines(screen, (255,0,0), False, [img_rect.topleft, img_rect.bottomright], 4)
            pygame.draw.lines(screen, (255,0,0), False, [img_rect.bottomleft, img_rect.topright], 4)
