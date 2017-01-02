from heroesofpygame.sala import ClassRoom

class Pietro(object):
    def __init__(self, wall_width=3, color=(49, 9, 5)):
        self.klasa_bio = ClassRoom(pos=(73,22), room_width=126, room_length=113)

    def draw(self, screen):
        self.klasa_bio.draw(screen)
