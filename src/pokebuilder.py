import pandas as pd
import numpy as np

class pokeBuilder:
    def __init__(self, gen_file) -> None:
        self.poke_list = self.load_pokemon(gen_file)
        #self.team = self.init_team()

    def load_pokemon(self, gen_file):
        df = pd.read_csv(gen_file)
        return df
    
    def init_team(self):
        poke = self.get_poke_list()

        print("Starters:")
        print("1.", poke['Pokemon'][0])
        print("2.", poke['Pokemon'][3])
        print("3.", poke['Pokemon'][6])

        start = input("Enter the number of the starter selected: ")

        while not start.isnumeric() or int(start) not in [1,2,3]:
            print("Invalid Input")
            start = input("Enter the number of the starter selected: ")

        pIndex = 0
        match int(start):
            case 1:
                pIndex = 0
            case 2:
                pIndex = 3
            case 3:
                pIndex = 6


        select = list(poke.iloc[pIndex + 2]) 

        team = {}
        team[select[1]]  = select  
        
        return team
    
    def print_team(self):
        team = self.get_team()
        i = 1
        print("Pokemon, HP, Attack, Defense, Speed, Special, Total, Average")
        for poke in team:
            print(str(i) + ". " + str(team[poke][2]) + " " + str(team[poke][3]) + " " + 
                  str(team[poke][4]) + " " + str(team[poke][5]) + " " + 
                  str(team[poke][6]) + " " + str(team[poke][7]) + " " + 
                  str(team[poke][8]))
    
    def get_poke_list(self):
        return self.poke_list
    
    def get_team(self):
        return self.team





if __name__ == "__main__":
    pkB = pokeBuilder("data/all_poke_data.csv")
    #pkB.print_team()
    print(pkB.get_poke_list().head(20))