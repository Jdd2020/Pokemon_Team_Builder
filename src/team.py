import pokemon
from typing import Dict

class team:
    def __init__(self, monster):
        self.team = dict()
        starter = pokemon(monster)
        self.team[starter.get_name()] = starter

    def add_pokemon(self, monster):
        pass

    def del_pokemon(self, monster):
        pass

    
