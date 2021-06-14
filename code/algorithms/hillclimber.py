import copy
import random

from code.classes import grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

class HillClimber():
    """
    HillClimber class takes a valid grid as input and randomly changes one cable. Each improvement is saved and
    used as input for the next iteration.
    """
    def __init__(self, grid):
        self.grid = copy.deepcopy(grid)
