# -*- coding: UTF-8 -*-
from heroesofpygame.sala import ClassRoom


class Parter(object): #TODO bottom i up nie dziela!(niewyswietla drzwi)
    def __init__(self, wall_width=3, color=(75, 5, 205)):
        self.sala_gimn = ClassRoom(nazwa="sala gimnastyczna", pos=(73,22), room_width=126, room_length=113, drzwi={'location':'bottom', 'door_delta': 20})
        self.szatnia_duza = ClassRoom(nazwa=u"duża szatnia", pos=(73,135), room_width=95, room_length=18, drzwi={'location':'right', 'door_delta': 20})# todo sa 2 drzwi dol dol
        self.korytarz_szatni = ClassRoom(nazwa="korytarz szatni", pos=(73,153), room_width=95, room_length=10, drzwi={'location':'right', 'door_delta': 20})#TODO sa 2 drzwi lewo prawo
        self.szatnia_mala = ClassRoom(nazwa=u"mała szatnia", pos=(73,163), room_width=76, room_length=18, drzwi={'location':'up', 'door_delta': 20})
        self.kantorek_wf = ClassRoom(nazwa="kantorek W-F", pos=(149,163), room_width=19, room_length=18, drzwi={'location':'up', 'door_delta': 20})
        self.hall_glowny = ClassRoom(nazwa=u"hall główny", pos=(168,135), room_width=67, room_length=120, drzwi={'location':'bottom', 'door_delta': 20})

        self.osiem_a = ClassRoom(nazwa="sala 8a", pos=(10,181), room_width=30, room_length=74, drzwi={'location':'right', 'door_delta': 20})
        self.osiem = ClassRoom(nazwa="sala 8", pos=(40,181), room_width=46, room_length=37, drzwi={'location':'right', 'door_delta': 20})
        self.archiwum = ClassRoom(nazwa="archiwum", pos=(40,218), room_width=21, room_length=37, drzwi={'location':'left', 'door_delta': 20})
        self.siodemka = ClassRoom(nazwa="sala 7", pos=(61,218), room_width=52, room_length=37, drzwi={'location':'up', 'door_delta': 20})
        self.szostka = ClassRoom(nazwa="sala 6", pos=(113,218), room_width=55, room_length=37, drzwi={'location':'up', 'door_delta': 20})

        self.lazienka_damska = ClassRoom(nazwa=u"łazienka damska", pos=(86,181), room_width=36, room_length=18, drzwi={'location':'bottom', 'door_delta': 20})
        self.lazienka_meska = ClassRoom(nazwa=u"łazienka męska", pos=(122,181), room_width=46, room_length=18, drzwi={'location':'bottom', 'door_delta': 20})
        self.korytarz_parteru = ClassRoom(nazwa="korytarz parteru", pos=(86,199), room_width=82, room_length=19, drzwi={'location':'right', 'door_delta': 20}) # TODO jest kilka wyjsc z korytarza

        self.stolowka = ClassRoom(nazwa=u"stołówka", pos=(235,181), room_width=49, room_length=37, drzwi={'location':'right', 'door_delta': 20})
        self.sekretariat = ClassRoom(nazwa="sekretariat", pos=(235,218), room_width=18, room_length=37, drzwi={'location':'right', 'door_delta': 20})
        self.gabinet_zast_dyrektora = ClassRoom(nazwa="gabinet z-cy dyrektora", pos=(253,218), room_width=15, room_length=37, drzwi={'location':'right', 'door_delta': 20})
        self.gabinet_dyrektora = ClassRoom(nazwa="gabinet dyrektora", pos=(268,218), room_width=16, room_length=37, drzwi={'location':'right', 'door_delta': 20})


    def sale(self):
        return [self.sala_gimn,
                self.szatnia_duza,
                self.korytarz_szatni,
                self.szatnia_mala,
                # self.kantorek_wf,  # nie można wylosować bo tam nie ma okien --> mie może wlecieć szarańcza
                self.hall_glowny,
                self.osiem_a,
                self.osiem,
                self.archiwum,
                self.siodemka,
                self.szostka,
                self.lazienka_damska,
                self.lazienka_meska,
                self.korytarz_parteru,
                self.stolowka,
                self.sekretariat,
                self.gabinet_zast_dyrektora,
                self.gabinet_dyrektora]

    def walls(self):
        sciany = []
        for sala in self.sale():
            sciany.extend(sala.walls())
        return sciany

    def draw(self, screen):
        for sala in self.sale():
            sala.draw(screen)
