# -*- coding: UTF-8 -*-
from heroesofpygame.sala import ClassRoom

class Pietro(object):
    def __init__(self, wall_width=3, color=(49, 9, 5)):
        self.klasa_bio = ClassRoom(nazwa="sala biologiczna", pos=(600,300), room_width=59, room_length=87, drzwi={'location':'right', 'door_delta': 20})
        self.kantorek_chem = ClassRoom(nazwa="kantorek chemiczny", pos=(600,387), room_width=30, room_length=38, drzwi={'location':'up', 'door_delta': 20})
        self.kantorek_fiz = ClassRoom(nazwa="kantorek fizyczny", pos=(629,387), room_width=30, room_length=38, drzwi={'location':'up', 'door_delta': 20})
        self.swietlica_gorna = ClassRoom(nazwa=u"świetlica górna", pos=(659,365), room_width=40, room_length=60, drzwi={'location':'up', 'door_delta': 20})
        self.pedagog = ClassRoom(nazwa="sala pedagoga", pos=(659,300), room_width=25, room_length=28, drzwi={'location':'bottom', 'door_delta': 20})
        self.pokoj_nauczycieli = ClassRoom(nazwa=u"pokój nauczycielski", pos=(684,300), room_width=55, room_length=28, drzwi={'location':'bottom', 'door_delta': 20})
        self.klasa_info = ClassRoom(nazwa="sala informatyczna", pos=(699,365), room_width=72, room_length=60, drzwi={'location':'up', 'door_delta': 20})
        self.klasa_hist = ClassRoom(nazwa="sala historyczna", pos=(770,365), room_width=72, room_length=60, drzwi={'location':'up', 'door_delta': 20})

    def draw(self, screen):
        self.klasa_bio.draw(screen)
