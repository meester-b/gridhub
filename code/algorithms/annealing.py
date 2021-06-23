# Import and numpy
import random
import numpy as np

# Annealing uses Hillclimb algorithm
from .hillclimber import HillClimber

class Annealing(HillClimber):
    """
    Simulated Annealing algorithm allows for some flexibility in the HillClimbing method.
    """
    def __init__(self, grid, temperature=1):
        super().__init__(grid)
        # volgens mag deze hieronder weg ----------
        self.grid = grid

        self.T0 = temperature
        self.T = temperature
    
    def update_temperature(self):
        """
        This function reduces the temperature linearly to zero when all iterations have passed.
        """
        self.T = self.T - (self.T0 / self.iterations)

    
    def check_solution(self, new_grid):
        """
        Checks the solution and saves when better than the previous solution.
        Depending on the temperature, this function sometimes also accepts worse solutions.
        """
        # Calculate the grid distance, and compare the difference between old an new score with delta.
        new_grid.calc_dist()
        new_score = new_grid.score
        old_score = self.grid.score
        delta = new_score - old_score
        
        # Prevent RuntimeWarning and OverflowError that may occur due to python properties.
        try:
            probability = np.exp(-delta / self.T)
            if random.random() < probability:
                self.grid = new_grid
        except:
            pass

        # Update the temperature.
        self.update_temperature()
    
    