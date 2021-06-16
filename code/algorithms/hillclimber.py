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


    # def select_random_house(self, list):
    #     """ 
    #     Selects a random house from the list of houses.
    #     """
    #     random.shuffle(list)
    #     return list[0]
    
    def reconnect_house(self, new_grid):
        """
        Picks two houses and swaps their cables if it fits within the battery capacity constraints.
        """
        # shuffle the list of houses in the grid
        new_grid.shuffle_list(new_grid.houses)

        # select two houses from the shuffled list
        random_house_1 = new_grid.pick_random_house(new_grid.houses, 0)
        current_bat_1 = random_house_1.bats[0]
        random_house_2 = new_grid.pick_random_house(new_grid.houses, 1)
        current_bat_2 = random_house_2.bats[0]

        # add the selected houses' output to the remaining capacity of the battery
        current_bat_1.capacity_left += random_house_1.output
        current_bat_2.capacity_left += random_house_2.output

        # swap houses if possible within constraints, else go back to previous situation
        if random_house_1.output < current_bat_2.capacity_left:
            if random_house_2.output < current_bat_1.capacity_left:
                new_grid.reconnect_constraint(random_house_2, current_bat_1)
                new_grid.reconnect_constraint(random_house_1, current_bat_2)
        else:
            current_bat_1.capacity_left += random_house_1.output
            current_bat_2.capacity_left += random_house_2.output


    def check_solution(self, new_grid):
        """
        Saves the new grid if the total cable length is shorter after the swap.
        """
        new_grid.calc_dist()

        if new_grid.score < self.grid.score:
            self.grid = new_grid


    def print_stats(self):
        """
        Prints the result of the HillClimber algorithm.
        """
        print(f"The HillClimbed improved version has a distance of {self.grid.score}")


    def run(self, iterations):
        """
        Runs HillClimber algorithm for given number of iterations.
        """
        self.iterations = iterations
        
        for iteration in range(iterations):
            new_grid = copy.deepcopy(self.grid)
            self.reconnect_house(new_grid)
            self.check_solution(new_grid)
        
        self.print_stats()

        return self.grid
