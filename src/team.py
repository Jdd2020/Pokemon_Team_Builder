import pokemon
from typing import Dict

class team:
    def __init__(self, starter):
        self.team = dict()
        self.team_types = list()
        self.team[starter.get_name()] = starter
        self.team_hp = starter.get_hp()
        self.team_atk = starter.get_atk()
        self.team_def = starter.get_def()
        self.team_spAtk = starter.get_spAtk()
        self.team_spDef = starter.get_spDef()
        self.team_spd = starter.get_spd()
        self.team_types.append(starter.get_type1())
        if starter.get_type2() != "":
            self.team_types.append(starter.get_type2())



    def add_pokemon(self, monster) -> bool:
        if len(self.get_team()) < 6:
            self.get_team()[monster.get_name()] = monster
            self.team_hp += monster.get_hp()
            self.team_atk += monster.get_atk()
            self.team_def += monster.get_def()
            self.team_spAtk += monster.get_spAtk()
            self.team_spDef += monster.get_spDef()
            self.team_spd += monster.get_spd()
            return True
        return False

    def del_pokemon(self, monster) -> bool:
        if len(self.get_team()) > 1 and monster.get_name() in self.get_team():
            self.get_team().pop(monster.get_name())
            return True
        return False

    def get_team(self):
        return self.team
    
    def get_hp(self):
        return self.team_hp
    
    def get_atk(self):
        return self.team_atk
    
    def get_def(self):
        return self.team_def
    
    def get_spAtk(self):
        return self.team_spAtk
    
    def get_spDef(self):
        return self.team_spDef
    
    def get_spd(self):
        return self.team_spd

    
