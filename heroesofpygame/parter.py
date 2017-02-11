# -*- coding: UTF-8 -*-
from heroesofpygame.sala import ClassRoom
from heroesofpygame.door import Door
from heroesofpygame.hall import Hall


class Parter(object): #TODO bottom i up nie dziela!(niewyswietla drzwi)
    def __init__(self, wall_width=3, color=(75, 5, 205)):
        self.sala_gimn = ClassRoom(nazwa="sala gimnastyczna", pos=(73,22), room_width=116, room_length=113, tlo="sala_gimn_tlo.jpg")
        d_rect = self.sala_gimn.oblicz_rect_drzwi(door_location='right_wall', door_delta=10, skala=1, door_length = 10)
        drzwi_sala_gimn_korytarz_sali_gimn = Door(d_rect)
        self.sala_gimn.wstaw_drzwi(drzwi_sala_gimn_korytarz_sali_gimn, door_location='right_wall')
        d_rect = self.sala_gimn.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=100, skala=1, door_length = 10)
        drzwi_sala_gimn_hall = Door(d_rect)
        self.sala_gimn.wstaw_drzwi(drzwi_sala_gimn_hall, door_location='bottom_wall')

        self.korytarz_sali_gimn = ClassRoom(nazwa="korytarz obok sali gimnastycznej", pos=(189,22), room_width=18, room_length=113)
        d_rect = self.korytarz_sali_gimn.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=1, skala=1)
        drzwi_korytarz_sali_gimn_hall = Door(d_rect)
        self.korytarz_sali_gimn.wstaw_drzwi(drzwi_korytarz_sali_gimn_hall, door_location='bottom_wall')
        self.korytarz_sali_gimn.wstaw_drzwi(drzwi_sala_gimn_korytarz_sali_gimn, door_location='left_wall')

        self.sala_zabaw = ClassRoom(nazwa="sala zabaw", pos=(207,22), room_width=30, room_length=40)
        d_rect = self.sala_zabaw.oblicz_rect_drzwi(door_location='left_wall', door_delta=10, skala=1)
        drzwi_korytarz_sali_gimn_sala_zabaw = Door(d_rect)
        self.sala_zabaw.wstaw_drzwi(drzwi_korytarz_sali_gimn_sala_zabaw, door_location='left_wall')
        self.korytarz_sali_gimn.wstaw_drzwi(drzwi_korytarz_sali_gimn_sala_zabaw, door_location='right_wall')

        self.szatnia_gimn = ClassRoom(nazwa="szatnia gimnastyczna", pos=(207,62), room_width=30, room_length=33)
        d_rect = self.szatnia_gimn.oblicz_rect_drzwi(door_location='left_wall', door_delta=10, skala=1)
        drzwi_korytarz_sali_gimn_szatnia_gimn = Door(d_rect)
        self.szatnia_gimn.wstaw_drzwi(drzwi_korytarz_sali_gimn_szatnia_gimn, door_location='left_wall')
        self.korytarz_sali_gimn.wstaw_drzwi(drzwi_korytarz_sali_gimn_szatnia_gimn, door_location='right_wall')

        self.biblioteka = ClassRoom(nazwa="biblioteka", pos=(207,95), room_width=30, room_length=40)
        d_rect = self.biblioteka.oblicz_rect_drzwi(door_location='left_wall', door_delta=27, skala=1)
        drzwi_korytarz_sali_gimn_biblioteka = Door(d_rect)
        self.biblioteka.wstaw_drzwi(drzwi_korytarz_sali_gimn_biblioteka, door_location='left_wall')
        self.korytarz_sali_gimn.wstaw_drzwi(drzwi_korytarz_sali_gimn_biblioteka, door_location='right_wall')

        self.szatnia_duza = ClassRoom(nazwa=u"duża szatnia", pos=(73,135), room_width=95, room_length=18)
        d1_rect = self.szatnia_duza.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=15, skala=1)
        d2_rect = self.szatnia_duza.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=78, skala=1)
        drzwi_1_szatnia_duza = Door(d1_rect)
        drzwi_2_szatnia_duza = Door(d2_rect)
        self.szatnia_duza.wstaw_drzwi(drzwi_1_szatnia_duza, door_location='bottom_wall')
        self.szatnia_duza.wstaw_drzwi(drzwi_2_szatnia_duza, door_location='bottom_wall')

        self.korytarz_szatni = ClassRoom(nazwa="korytarz szatni", pos=(73,153), room_width=95, room_length=10)
        d_zewn_rect = self.korytarz_szatni.oblicz_rect_drzwi(door_location='left_wall', door_delta=2, skala=1)
        d_wewn_rect = self.korytarz_szatni.oblicz_rect_drzwi(door_location='right_wall', door_delta=2, skala=1)
        drzwi_z_szatni_na_zewnatrz = Door(d_zewn_rect)
        drzwi_korytarz_szatni_hall = Door(d_wewn_rect)
        self.korytarz_szatni.wstaw_drzwi(drzwi_1_szatnia_duza, door_location='top_wall')
        self.korytarz_szatni.wstaw_drzwi(drzwi_2_szatnia_duza, door_location='top_wall')
        self.korytarz_szatni.wstaw_drzwi(drzwi_z_szatni_na_zewnatrz, door_location='left_wall')
        self.korytarz_szatni.wstaw_drzwi(drzwi_korytarz_szatni_hall, door_location='right_wall')

        self.szatnia_mala = ClassRoom(nazwa=u"mała szatnia", pos=(73,163), room_width=76, room_length=18)
        d1_rect = self.szatnia_mala.oblicz_rect_drzwi(door_location='top_wall', door_delta=12, skala=1)
        d2_rect = self.szatnia_mala.oblicz_rect_drzwi(door_location='top_wall', door_delta=64, skala=1)
        drzwi_1_szatnia_mala = Door(d1_rect)
        drzwi_2_szatnia_mala = Door(d2_rect)
        self.szatnia_mala.wstaw_drzwi(drzwi_1_szatnia_mala, door_location='top_wall')
        self.szatnia_mala.wstaw_drzwi(drzwi_2_szatnia_mala, door_location='top_wall')
        self.korytarz_szatni.wstaw_drzwi(drzwi_1_szatnia_mala, door_location='bottom_wall')
        self.korytarz_szatni.wstaw_drzwi(drzwi_2_szatnia_mala, door_location='bottom_wall')

        self.kantorek_wf = ClassRoom(nazwa="kantorek W-F", pos=(149,163), room_width=19, room_length=18)
        d_rect = self.kantorek_wf.oblicz_rect_drzwi(door_location='top_wall', door_delta=2, skala=1)
        drzwi_kantorek_wf_korytarz_szatni = Door(d_rect)
        self.kantorek_wf.wstaw_drzwi(drzwi_kantorek_wf_korytarz_szatni, door_location='top_wall')
        self.korytarz_szatni.wstaw_drzwi(drzwi_kantorek_wf_korytarz_szatni, door_location='bottom_wall')

        self.hall_glowny = ClassRoom(nazwa=u"hall główny parteru", pos=(168,135), room_width=67, room_length=120)
        d_rect = self.hall_glowny.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=40, skala=1, door_length = 15)
        drzwi_zhallu_na_zewnatrz = Door(d_rect)

        self.osiem_a = ClassRoom(nazwa="sala 8a", pos=(10,181), room_width=30, room_length=74)
        d1_rect = self.osiem_a.oblicz_rect_drzwi(door_location='right_wall', door_delta=20, skala=1)
        d2_rect = self.osiem_a.oblicz_rect_drzwi(door_location='right_wall', door_delta=50, skala=1)
        drzwi_osiem_a_osiem = Door(d1_rect)
        drzwi_osiem_a_archiwum = Door(d2_rect)
        self.osiem_a.wstaw_drzwi(drzwi_osiem_a_osiem, door_location='right_wall')
        self.osiem_a.wstaw_drzwi(drzwi_osiem_a_archiwum, door_location='right_wall')

        self.osiem = ClassRoom(nazwa="sala 8", pos=(40,181), room_width=46, room_length=37, tlo="sala8_tlo.jpg")
        d_rect = self.osiem.oblicz_rect_drzwi(door_location='right_wall', door_delta=27, skala=1)
        drzwi_osiem_korytarz_parteru = Door(d_rect)
        self.osiem.wstaw_drzwi(drzwi_osiem_korytarz_parteru, door_location='right_wall')
        self.osiem.wstaw_drzwi(drzwi_osiem_a_osiem, door_location='left_wall')

        self.archiwum = ClassRoom(nazwa="archiwum", pos=(40,218), room_width=21, room_length=37)
        self.archiwum.wstaw_drzwi(drzwi_osiem_a_archiwum, door_location='left_wall')

        self.siodemka = ClassRoom(nazwa="sala 7", pos=(61,218), room_width=52, room_length=37)
        d_rect = self.siodemka.oblicz_rect_drzwi(door_location='top_wall', door_delta=42, skala=1)
        drzwi_siodemka_korytarz_parteru = Door(d_rect)
        self.siodemka.wstaw_drzwi(drzwi_siodemka_korytarz_parteru, door_location='top_wall')

        self.szostka = ClassRoom(nazwa="sala 6", pos=(113,218), room_width=55, room_length=37, tlo="sala6_tlo.jpg")
        d_rect = self.szostka.oblicz_rect_drzwi(door_location='top_wall', door_delta=7, skala=1)
        drzwi_szostka_korytarz_parteru = Door(d_rect)
        self.szostka.wstaw_drzwi(drzwi_szostka_korytarz_parteru, door_location='top_wall')

        self.lazienka_damska = ClassRoom(nazwa=u"łazienka damska", pos=(86,181), room_width=41, room_length=18)
        d_rect = self.lazienka_damska.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=4, skala=1)
        drzwi_lazienka_damska_korytarz_parteru = Door(d_rect)
        self.lazienka_damska.wstaw_drzwi(drzwi_lazienka_damska_korytarz_parteru, door_location='bottom_wall')

        self.lazienka_damska_pom_gospodarcze = ClassRoom(nazwa=u"pomieszczenie gospodarcze 1", pos=(104,194), room_width=23, room_length=5)

        self.lazienka_meska = ClassRoom(nazwa=u"łazienka męska", pos=(127,181), room_width=41, room_length=18)
        d_rect = self.lazienka_meska.oblicz_rect_drzwi(door_location='bottom_wall', door_delta=28, skala=1)
        drzwi_lazienka_meska_korytarz_parteru = Door(d_rect)
        self.lazienka_meska.wstaw_drzwi(drzwi_lazienka_meska_korytarz_parteru, door_location='bottom_wall')

        self.lazienka_meska_pom_gospodarcze = ClassRoom(nazwa=u"pomieszczenie gospodarcze 2", pos=(127,194), room_width=23, room_length=5)

        self.korytarz_parteru = ClassRoom(nazwa="korytarz parteru", pos=(86,199), room_width=82, room_length=19)
        d1_rect = self.korytarz_parteru.oblicz_rect_drzwi(door_location='top_wall', door_delta=21, skala=1)
        drzwi_lazienka_damska_pom_gospodarcze = Door(d1_rect)
        d2_rect = self.korytarz_parteru.oblicz_rect_drzwi(door_location='top_wall', door_delta=46, skala=1)
        drzwi_lazienka_meska_pom_gospodarcze = Door(d2_rect)

        self.stolowka = ClassRoom(nazwa=u"stołówka", pos=(235,181), room_width=49, room_length=37, tlo="stolowka_tlo.jpg")
        d_rect = self.stolowka.oblicz_rect_drzwi(door_location='left_wall', door_delta=9, skala=1)
        drzwi_stolowka_hall = Door(d_rect)
        self.stolowka.wstaw_drzwi(drzwi_stolowka_hall, door_location='left_wall')

        self.sekretariat = ClassRoom(nazwa="sekretariat", pos=(235,218), room_width=18, room_length=37)
        d_rect = self.sekretariat.oblicz_rect_drzwi(door_location='left_wall', door_delta=15, skala=1)
        drzwi_sekretariat_hall = Door(d_rect)
        self.sekretariat.wstaw_drzwi(drzwi_sekretariat_hall, door_location='left_wall')

        self.hall_parteru = Hall(self.hall_glowny, self.korytarz_parteru)
        self.korytarz_parteru.wstaw_drzwi(drzwi_osiem_korytarz_parteru, door_location='left_wall', w_sali=self.hall_parteru)
        self.korytarz_parteru.wstaw_drzwi(drzwi_siodemka_korytarz_parteru, door_location='bottom_wall', w_sali=self.hall_parteru)
        self.korytarz_parteru.wstaw_drzwi(drzwi_szostka_korytarz_parteru, door_location='bottom_wall', w_sali=self.hall_parteru)
        self.korytarz_parteru.wstaw_drzwi(drzwi_lazienka_damska_korytarz_parteru, door_location='top_wall', w_sali=self.hall_parteru)
        self.korytarz_parteru.wstaw_drzwi(drzwi_lazienka_damska_pom_gospodarcze, door_location='top_wall')
        self.korytarz_parteru.wstaw_drzwi(drzwi_lazienka_meska_korytarz_parteru, door_location='top_wall', w_sali=self.hall_parteru)
        self.korytarz_parteru.wstaw_drzwi(drzwi_lazienka_meska_pom_gospodarcze, door_location='top_wall')
        self.hall_glowny.wstaw_drzwi(drzwi_stolowka_hall, door_location='right_wall', w_sali=self.hall_parteru)
        self.hall_glowny.wstaw_drzwi(drzwi_sekretariat_hall, door_location='right_wall', w_sali=self.hall_parteru)
        self.hall_glowny.wstaw_drzwi(drzwi_zhallu_na_zewnatrz, door_location='bottom_wall', w_sali=self.hall_parteru)
        self.hall_glowny.wstaw_drzwi(drzwi_sala_gimn_hall, door_location='top_wall', w_sali=self.hall_parteru)
        self.hall_glowny.wstaw_drzwi(drzwi_korytarz_sali_gimn_hall, door_location='top_wall', w_sali=self.hall_parteru)
        self.hall_glowny.wstaw_drzwi(drzwi_korytarz_szatni_hall, door_location='left_wall', w_sali=self.hall_parteru)

        self.gabinet_zast_dyrektora = ClassRoom(nazwa="gabinet z-cy dyrektora", pos=(253,218), room_width=15, room_length=37)
        d_rect = self.gabinet_zast_dyrektora.oblicz_rect_drzwi(door_location='left_wall', door_delta=15, skala=1)
        drzwi_sekretariat_gabinet_zast_dyrektora = Door(d_rect)
        self.sekretariat.wstaw_drzwi(drzwi_sekretariat_gabinet_zast_dyrektora, door_location='right_wall')
        self.gabinet_zast_dyrektora.wstaw_drzwi(drzwi_sekretariat_gabinet_zast_dyrektora, door_location='left_wall')

        self.gabinet_dyrektora = ClassRoom(nazwa="gabinet dyrektora", pos=(268,218), room_width=16, room_length=37)
        d_rect = self.gabinet_dyrektora.oblicz_rect_drzwi(door_location='left_wall', door_delta=15, skala=1)
        drzwi_gabinet_zast_dyrektora_gabinet_dyrektora = Door(d_rect)
        self.gabinet_zast_dyrektora.wstaw_drzwi(drzwi_gabinet_zast_dyrektora_gabinet_dyrektora, door_location='right_wall')
        self.gabinet_dyrektora.wstaw_drzwi(drzwi_gabinet_zast_dyrektora_gabinet_dyrektora, door_location='left_wall')

    def sale(self):
        return [self.sala_gimn,
                self.korytarz_sali_gimn,
                self.sala_zabaw,
                self.szatnia_gimn,
                self.biblioteka,
                self.szatnia_duza,
                self.korytarz_szatni,
                self.szatnia_mala,
                self.kantorek_wf,
                # self.hall_glowny, ##
                self.osiem_a,
                self.osiem,
                self.archiwum,
                self.siodemka,
                self.szostka,
                self.lazienka_damska,
                self.lazienka_damska_pom_gospodarcze,
                self.lazienka_meska,
                self.lazienka_meska_pom_gospodarcze,
                # self.korytarz_parteru, ##
                self.hall_parteru,
                self.stolowka,
                self.sekretariat,
                self.gabinet_zast_dyrektora,
                self.gabinet_dyrektora
               ]

    def sale_do_losowania(self):
        '''Tylko te sale w ktorych chcemy rozlokowywac kwiaty i szarancze'''
        return [self.sala_gimn,
                # self.korytarz_sali_gimn,  # tam jest za wasko
                self.sala_zabaw,
                self.szatnia_gimn,
                self.biblioteka,
                self.szatnia_duza,
                # self.korytarz_szatni, # tam jest wasko
                self.szatnia_mala,
                # self.kantorek_wf,  # tam nie ma okien --> nie może wlecieć szarańcza
                # self.hall_glowny, # tam wchodzimy do szkoly, punkt startowy gracza, nie chcemy miec tu kwiatow - byloby za latwo
                self.osiem_a,
                self.osiem,
                self.archiwum,
                self.siodemka,
                self.szostka,
                # self.lazienka_damska,  # jestesmy gentelman-ami - nie wchodzimy do damskiej
                self.lazienka_meska,
                # self.korytarz_parteru,  # nie ma okien --> nie może wlecieć szarańcza
                self.stolowka,
                self.sekretariat,
                self.gabinet_zast_dyrektora,
                self.gabinet_dyrektora
               ]

    def walls(self):
        sciany = []
        for sala in self.sale():
            sciany.extend(sala.walls())
        return sciany

    def draw(self, screen):
        for sala in self.sale():
            sala.draw(screen)
