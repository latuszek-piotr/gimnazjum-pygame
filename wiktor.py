
from character import *

class Player:
    def __init__(self,name, hp, str,int):
        character.__init__(self,name, hp)
        self.str = str
        self.int = int