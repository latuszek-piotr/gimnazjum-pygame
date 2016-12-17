import pygame


class Przegrana(object):
    def __init__(self, szerokosc, wysokosc):
        self.szerokosc = szerokosc
        self.wysokosc = wysokosc
        self.rect = pygame.Rect(0,0, self.szerokosc, self.wysokosc)
        self.rect_wyniku = self.wylicz_rect_wyniku()
        self.rect_rozgrywka = self.wylicz_button_rozgrywki()
        self.rect_gameover = self.wylicz_button_gameover()
        self.font = pygame.font.SysFont("comic sans MS", 45, bold=True) #ustawienie czcionki
        self.font_wyniku = pygame.font.SysFont("comic sans MS", 95, bold=True) #ustawienie czcionki

    def wylicz_rect_wyniku(self):
        szerokosc = 0.6 * self.szerokosc
        wysokosc = 0.4 * self.wysokosc
        pos_x = 0.2 * self.szerokosc
        pos_y = 0.05 * self.wysokosc
        return pygame.Rect(pos_x, pos_y, szerokosc, wysokosc)

    def wylicz_button_rozgrywki(self):
        szerokosc_buttonu = 0.35 * self.szerokosc
        wysokosc_buttonu = 0.4 * self.wysokosc
        pos_x_buttonu = 0.1 * self.szerokosc
        pos_y_buttonu = 0.5 * self.wysokosc
        return pygame.Rect(pos_x_buttonu, pos_y_buttonu, szerokosc_buttonu, wysokosc_buttonu)

    def wylicz_button_gameover(self):
        szerokosc_buttonu = 0.35 * self.szerokosc
        wysokosc_buttonu = 0.4 * self.wysokosc
        pos_x_buttonu = 0.55 * self.szerokosc
        pos_y_buttonu = 0.5 * self.wysokosc
        return pygame.Rect(pos_x_buttonu, pos_y_buttonu, szerokosc_buttonu, wysokosc_buttonu)

    def grac_ponownie(self, event):
        LEFT = 1
        if event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
            pos = pygame.mouse.get_pos()
            if self.rect_rozgrywka.collidepoint(pos):
                return "TAK"
            elif self.rect_gameover.collidepoint(pos):
                return "NIE"
        return None

    def draw(self, screen):
        text = self.font_wyniku.render("Przegrales ;-(", False, (255,0,0))
        screen.blit(text, [self.rect_wyniku.x + 20, self.rect_wyniku.y + 20])

        pygame.draw.rect(screen, (0,255,0), self.rect_rozgrywka)
        text = self.font.render("Ponowna rozgrywka", False, (0,0,0))
        screen.blit(text, [self.rect_rozgrywka.x + 20, self.rect_rozgrywka.y + 20])

        pygame.draw.rect(screen, (255,0,0), self.rect_gameover)
        text = self.font.render("Wyjdz z gry", False, (0,0,0))
        screen.blit(text, [self.rect_gameover.x + 20, self.rect_gameover.y + 20])

