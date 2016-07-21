
class character:
    def __init__(self,name, hp):
        self.name = name
        self.hp = hp

    def attack(self, other):
        pass

    def update(self):
        if self.hp < 0:
            self.dead = True
            self.hp = 0