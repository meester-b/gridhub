import copy
import random

from code.classes import grid
from .greedy import Greedy

class HillClimber(Greedy):
    """
    HillClimber class takes a valid grid as input and randomly changes one cable. Each improvement is saved and
    used as input for the next iteration.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
        self.distance = sum(grid.grid_distances)     # appenden we ergens waarden aan deze lijst?

    # 1) kies een random huis uit grid.houses, pick_random_list kan misschien niet gebruikt worden want lijst moet volledig blijven?
    ## ik denk een tweede lijst maken die we wel poppen en dan daarna met originele steps zetten
    def select_random_house(self, list):
        random.shuffle(list)
        return list[0]
    
    # 2) verbind dit huis met een batterij die beschikbaar is en waar het huis nu niet mee is verbonden
    def reconnect_house(self, new_grid):
        # pick random battery
        random_bat = new_grid.pick_random_bat()
        # pick random house from list of houses connected with that battery
        ## self. ervoor gezet
        random_house = self.select_random_house(random_bat.houses)

        # delete cable between battery and house
        new_grid.delete_cable(random_bat, random_house)     # delete kabel uit lijst en uit totale cable distance, functie werkt nog niet!

        # pick new battery to connect the house to
        new_battery = new_grid.pick_random_bat()            # nog checken of dit kan qua capacity

        # lay a new cable
        new_cable = new_grid.lay_cable(new_battery, random_house)       # voeg toe aan totale cable distance


    # 3) check de totale kabelafstand van de grid en sla op als new_distance korter is dan current_distance
    def check_solution(self, new_grid):
        old_value = self.distance
        new_value = sum(new_grid.grid_distances)

        if new_value <= old_value:
            self.grid = new_grid
            self.distances = new_value


    def run(self, iterations):
        """
        Runs HillClimber algorithm for given number of iterations
        """
        self.iterations = iterations
        
        for iteration in range(iterations):
            new_grid = copy.deepcopy(self.grid)
            self.reconnect_house(new_grid)
            self.check_solution(new_grid)