import copy
import random

# from code.classes import grid
from .greedy import Greedy

class HillClimber(Greedy):
    """
    HillClimber class takes a valid grid as input and randomly changes one cable. Each improvement is saved and
    used as input for the next iteration.
    """
    def __init__(self, grid):
        self.grid = grid
        # self.dc_grid = copy.deepcopy(grid)
        # self.distance = sum(grid.grid_distances)     # appenden we ergens waarden aan deze lijst?

    # 1) kies een random huis uit grid.houses, pick_random_list kan misschien niet gebruikt worden want lijst moet volledig blijven?
    ## ik denk een tweede lijst maken die we wel poppen en dan daarna met originele steps zetten
    # def select_random_house(self, list):
    #     random.shuffle(list)
    #     return list[0]
    
    # 2) verbind dit huis met een batterij die beschikbaar is en waar het huis nu niet mee is verbonden
    def reconnect_house(self, new_grid):
        new_grid.shuffle_list(new_grid.houses)
        random_house_1 = new_grid.pick_random_house(new_grid.houses, 0)
        current_bat_1 = random_house_1.bats[0]
        random_house_2 = new_grid.pick_random_house(new_grid.houses, 1)
        current_bat_2 = random_house_2.bats[0]

        current_bat_1.capacity_left += random_house_1.output
        current_bat_2.capacity_left += random_house_2.output

        if random_house_1.output < current_bat_2.capacity_left:
            if random_house_2.output < current_bat_1.capacity_left:
                new_grid.reconnect_constraint(random_house_2, current_bat_1)
                new_grid.reconnect_constraint(random_house_1, current_bat_2)
        else:
            current_bat_1.capacity_left += random_house_1.output
            current_bat_2.capacity_left += random_house_2.output

    


    # 3) check de totale kabelafstand van de grid en sla op als new_distance korter is dan current_distance
    def check_solution(self, new_grid):
        """

        """
        # old_value = self.grid.score
        new_grid.calc_dist()

        if new_grid.score < self.grid.score:
            self.grid = new_grid
            # new_grid.score = new_value

    def print_stats(self):
        """

        """
        print(f"The HillClimbed improved version has a distance of {self.grid.score}")

    def run(self, iterations):
        """
        Runs HillClimber algorithm for given number of iterations
        """
        self.iterations = iterations
        
        for iteration in range(iterations):
            new_grid = copy.deepcopy(self.grid)
            # print(self.grid)
            # print(len(new_grid.houses))
            self.reconnect_house(new_grid)
            self.check_solution(new_grid)
            # print(self.grid.score)
        
        self.print_stats()

        return self.grid
