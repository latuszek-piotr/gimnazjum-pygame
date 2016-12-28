import pygame
import os
from heroesofpygame.okno_wyboru import OknoWyboru


class Rozpoczecie(OknoWyboru):
    pygame_logo = os.path.join('grafika', 'pygame_logo.png')

    def __init__(self, szerokosc, wysokosc):
        super(Rozpoczecie, self).__init__(szerokosc, wysokosc, "Heroes of", button_play_text1="Start", button_play_text2="")
        self.rect_tytulu.left = 0.05 * self.szerokosc
        self.rect_logo = self.wylicz_rect_logo()
        self.pygame_logo_img = pygame.transform.scale(pygame.image.load(Rozpoczecie.pygame_logo).convert_alpha(),
                                                                        (self.rect_logo.width, self.rect_logo.height))

    def wylicz_rect_logo(self):
        szerokosc = 0.4 * self.szerokosc
        wysokosc = 0.3 * self.wysokosc
        pos_x = 0.5 * self.szerokosc
        pos_y = 0.05 * self.wysokosc
        return pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)

    def draw(self, screen):
        super(Rozpoczecie, self).draw(screen)
        screen.blit(self.pygame_logo_img, self.rect_logo.topleft)
