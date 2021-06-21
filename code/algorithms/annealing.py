import copy
import random

from .hillclimber import HillClimber

class Annealing(HillClimber):
    """
    Simulated Annealing algorithm allows for some flexibility in the HillClimbing method.
    """
    def __init__(self, grid):
        super().__init__()
        self.grid = grid
    
    def reconnect_annealing(self, new_grid):
        
        # shuffle the list of houses in the grid
        new_grid.shuffle_list(new_grid.houses)

        # grid input van Greedy

        # copy

        # repeat for i

        # reconnect huis to new coordinate (cable/house/battery)

        # check if input output is valid

        
    def check_solution_annealing(self, new_grid):
        pass


    def run_annealing(self, iterations):
        pass