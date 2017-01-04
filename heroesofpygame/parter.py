from heroesofpygame.sala import ClassRoom


class Parter(object): #TODO bottom i up nie dziela!(niewyswietla drzwi)
    def __init__(self, wall_width=3, color=(75, 5, 205)):
        self.sala_gimn = ClassRoom(pos=(73,22), room_width=126, room_length=113, drzwi={'location':'bottom', 'door_delta': 20})
        self.szatnia_duza = ClassRoom(pos=(73,135), room_width=95, room_length=18, drzwi={'location':'right', 'door_delta': 20})# todo sa 2 drzwi dol dol
        self.korytarz_szatni = ClassRoom(pos=(73,153), room_width=95, room_length=10, drzwi={'location':'right', 'door_delta': 20})#TODO sa 2 drzwi lewo prawo
        self.szatnia_mala = ClassRoom(pos=(73,163), room_width=76, room_length=18, drzwi={'location':'up', 'door_delta': 20})
        self.osiem_a = ClassRoom(pos=(10,181), room_width=30, room_length=69, drzwi={'location':'right', 'door_delta': 20})
        self.osiem = ClassRoom(pos=(40,181), room_width=46, room_length=36, drzwi={'location':'right', 'door_delta': 20})
        self.archiwum = ClassRoom(pos=(40,214), room_width=20, room_length=36, drzwi={'location':'left', 'door_delta': 20})
        self.siodemka = ClassRoom(pos=(60,214), room_width=50, room_length=36, drzwi={'location':'up', 'door_delta': 20})
        self.szostka = ClassRoom(pos=(110,214), room_width=50, room_length=36, drzwi={'location':'up', 'door_delta': 20})
        self.korytarz_do_sali_siedem = ClassRoom(pos=(83,197), room_width=77, room_length=20, drzwi={'location':'right', 'door_delta': 20}) # TODO jest kilka wyjsc z korytarza
        self.kantorek_wf = ClassRoom(pos=(149,163), room_width=19, room_length=18, drzwi={'location':'up', 'door_delta': 20})
        self.korytarz_do_szatni = ClassRoom(pos=(168,134), room_width=73, room_length=47, drzwi={'location':'bottom', 'door_delta': 20})
        self.stolowka = ClassRoom(pos=(241,179), room_width=60, room_length=40, drzwi={'location':'right', 'door_delta': 20})
        self.lazienka_dziewczyn = ClassRoom(pos=(85,180), room_width=36, room_length=20, drzwi={'location':'bottom', 'door_delta': 20})
        self.klasa_bio = ClassRoom(pos=(600,300), room_width=59, room_length=87, drzwi={'location':'right', 'door_delta': 20})
        self.kantorek_chem = ClassRoom(pos=(600,387), room_width=30, room_length=38, drzwi={'location':'up', 'door_delta': 20})
        self.kantorek_fiz = ClassRoom(pos=(629,387), room_width=30, room_length=38, drzwi={'location':'up', 'door_delta': 20})
        self.swietlica_gorna = ClassRoom(pos=(659,365), room_width=40, room_length=60, drzwi={'location':'up', 'door_delta': 20})
        self.pedagog = ClassRoom(pos=(659,300), room_width=25, room_length=28, drzwi={'location':'bottom', 'door_delta': 20})
        self.pokoj_nauczycieli = ClassRoom(pos=(684,300), room_width=55, room_length=28, drzwi={'location':'bottom', 'door_delta': 20})
        self.klasa_info = ClassRoom(pos=(699,365), room_width=72, room_length=60, drzwi={'location':'up', 'door_delta': 20})
        self.klasa_hist = ClassRoom(pos=(770,365), room_width=72, room_length=60, drzwi={'location':'up', 'door_delta': 20})

    def sale(self):
        return [self.sala_gimn,
                self.szatnia_duza,
                self.korytarz_szatni,
                self.szatnia_mala,
                self.osiem_a,
                self.osiem,
                self.archiwum,
                self.siodemka,
                self.szostka,
                self.korytarz_do_sali_siedem,
                self.kantorek_wf,
                self.korytarz_do_szatni,
                self.stolowka,
                self.lazienka_dziewczyn,
                self.klasa_bio,
                self.kantorek_chem,
                self.kantorek_fiz,
                self.swietlica_gorna,
                self.pedagog,
                self.pokoj_nauczycieli,
                self.klasa_info,
                self.klasa_hist]

    def walls(self):
        sciany = []
        for sala in self.sale():
            sciany.extend(sala.walls())
        return sciany

    def draw(self, screen):
        for sala in self.sale():
            sala.draw(screen)
