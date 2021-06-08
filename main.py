from code.algorithms import baseline
from code.classes import battery, house, cable, grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
    
    # call algorithm 
    # baseline.unconstrained_baseline(1000)
    baseline.constrained_baseline(1)

    
