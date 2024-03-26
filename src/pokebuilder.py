import pandas as pd
import numpy as np
import pokemon as pk
import team as tm

class pokeBuilder:
    def __init__(self, gen_file) -> None:
        self.poke_list = self.load_pokemon(gen_file)
        starter = pk.pokemon(list(self.poke_list.iloc[0]))
        self.team = tm.team(starter)
        self.team.add_pokemon(pk.pokemon(list(self.poke_list.iloc[4])))
        self.team.add_pokemon(pk.pokemon(list(self.poke_list.iloc[9])))
        

    def load_pokemon(self, gen_file):
        df = pd.read_csv(gen_file)
        return df
    
    def init_team(self):
        pass
    
    def print_team(self):
        i = 1
        currTeam = self.team.get_team()

        print("# Pokemon    HP ATK DEF spATK spDEF SPD")
        for pokeName in currTeam:
            poke = currTeam[pokeName]
            print(i, pokeName, poke.get_hp(), poke.get_atk(), poke.get_def(), poke.get_spAtk(), poke.get_spDef(), poke.get_spd())
            i += 1

        print("Totals:", self.team.get_hp(), self.team.get_atk(), self.team.get_def(), self.team.get_spAtk(), self.team.get_spDef(), self.team.get_spd())
    
    def get_poke_list(self):
        return self.poke_list
    
    def get_team(self):
        return self.team

    def recommened(self):
        pass




if __name__ == "__main__":
    pkB = pokeBuilder("src/data/all_poke_data.csv")
    pkB.print_team()