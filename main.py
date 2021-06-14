from code.algorithms import baseline, greedy, hillclimber
from code.classes import grid
#from code.visualisations.grid_plot import visualise
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     
    # print(test_grid)
    # print(visualise())
    # test_grid.print_grid()

    ## call algorithms
    # --------------------------------- Baseline ------------------------------------------
    # run = baseline.Baseline()
    # run.unconstrained_baseline(1000)
    # baseline.Baseline.constrained_baseline(10)  

    # --------------------------------- Greedy --------------------------------------------
    # greedy.Greedy.unconstrained_greedy()
    valid_graph = greedy.Greedy.constrained_greedy(10)
    # print(valid_graph)

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_graph)
    # climber.run(50)

