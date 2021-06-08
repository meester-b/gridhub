import random
import copy
from code.algorithms import baseline
from code.classes import battery, house, cable, grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    dist = "1"

    test_grid = grid.Grid(f"data/district_{dist}/district-{dist}_houses.csv", f"data/district_{dist}/district-{dist}_batteries.csv")
    
    # call algorithm from file
    baseline.baseline()
