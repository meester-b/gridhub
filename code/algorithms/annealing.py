import copy
import random

from .hillclimber import HillClimber

class Annealing(HillClimber):
    """
    Simulated Annealing algorithm allows for some flexibility in the HillClimbing method.
    """
    def __init__(self, grid):
        self.grid = grid