from code.algorithms import baseline, greedy
from code.classes import grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
    
    ## call algorithms
    # baseline
    # baseline.unconstrained_baseline(100000)
    # baseline.constrained_baseline(100000)  

    # greedy
    greedy.unconstrained_greedy()
    greedy.constrained_greedy(1000)
