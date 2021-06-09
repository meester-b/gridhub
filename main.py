from code.algorithms import baseline, greedy
from code.classes import grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
    
    ## call algorithms
    # baseline

    baseline.Baseline.unconstrained_baseline(10)
    baseline.constrained_baseline(10)  

    # greedy
    greedy.unconstrained_greedy()
    greedy.constrained_greedy(10)

    # test_grid.run()
