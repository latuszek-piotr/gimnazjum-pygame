from heroesofpygame.sala import ClassRoom


class Parter(object):
    def __init__(self, wall_width=3, color=(75, 5, 205)):
        self.sala_gimn = ClassRoom(pos=(73,22), room_width=126, room_length=113)
        self.szatnia_duza = ClassRoom(pos=(73,135), room_width=95, room_length=18)
        self.korytarz_szatni = ClassRoom(pos=(73,153), room_width=95, room_length=10)
        self.szatnia_mala = ClassRoom(pos=(73,163), room_width=76, room_length=18)
        self.osiem_a = ClassRoom(pos=(10,181), room_width=30, room_length=72)
        self.osiem = ClassRoom(pos=(40,181), room_width=46, room_length=36)
        self.archiwum = ClassRoom(pos=(40,214), room_width=20, room_length=36)
        self.siudemka = ClassRoom(pos=(60,214), room_width=50, room_length=36)
        self.szostka = ClassRoom(pos=(110,214), room_width=50, room_length=36)
        self.lazienka_dziewczyn = ClassRoom(pos=(110,214), room_width=50, room_length=36)


    def draw(self, screen):
        self.sala_gimn.draw(screen)
        self.szatnia_duza.draw(screen)
        self.korytarz_szatni.draw(screen)
        self.szatnia_mala.draw(screen)
        self.osiem_a.draw(screen)
        self.osiem.draw(screen)
        self.archiwum.draw(screen)
        self.siudemka.draw(screen)
        self.szostka.draw(screen)

