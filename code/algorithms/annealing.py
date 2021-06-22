import random
import numpy as np

from .hillclimber import HillClimber

class Annealing(HillClimber):
    """
    Simulated Annealing algorithm allows for some flexibility in the HillClimbing method.
    """
    def __init__(self, grid, temperature=1):
        super().__init__(grid)
        # volgens mag deze hieronder weg
        self.grid = grid


        self.T0 = temperature
        self.T = temperature
    
    def update_temperature(self):
        """

        """
        self.T = self.T - (self.T0 / self.iterations)
        
        # Exponential would look like this:
        
        # alpha = 0.99
        # self.T = self.T * alpha
    
    def check_solution(self, new_grid):
        """

        """
        new_grid.calc_dist()
        new_score = new_grid.score
        old_score = self.grid.score
        delta = new_score - old_score
        
        # try except to prevent RuntimeWarning and OverflowError
        try:
            probability = np.exp(-delta / self.T)
            if random.random() < probability:
                self.grid = new_grid
        except:
            pass

        self.update_temperature()
    
    