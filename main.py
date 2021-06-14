from code.algorithms import baseline, greedy
from code.classes import grid
#from code.visualisations.grid_plot import visualise
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     
    #print(test_grid)
    # print(visualise())

    ## call algorithms
    # baseline
    # run = baseline.Baseline()
    # run.unconstrained_baseline(1000)
    # baseline.Baseline.constrained_baseline(10)  

    # greedy
    # greedy.Greedy.unconstrained_greedy()
    greedy.Greedy.constrained_greedy(10)

    # test_grid.print_grid()
