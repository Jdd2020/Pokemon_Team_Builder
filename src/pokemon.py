from typing import Dict

class pokemon:
    def __init__(self, input):
        self.index = input[0]
        self.name = input[1]
        self.hp = input[31]
        self.atk = input[32]
        self.deff = input[33]
        self.spAtk = input[34]
        self.spDeff = input[35]
        self.spd = input[36]
        self.total = input[37]
        self.type1 = input[38]
        self.type2 = input[39]

    def get_name(self) -> str:
        return self.name
    
    def get_dex(self) -> int:
        return self.index
    
    def get_hp(self) -> int:
        return self.hp
    
    def get_atk(self) -> int:
        return self.atk
    
    def get_def(self) -> int:
        return self.deff
    
    def get_spAtk(self) -> int:
        return self.spAtk
    
    def get_spDef(self) -> int:
        return self.spDeff
    
    def get_spd(self) -> int:
        return self.spd
    
    def get_type1(self) -> str:
        return self.type1
    
    def get_type2(self) -> str:
        return self.type2

        