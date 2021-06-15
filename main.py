from code.algorithms import baseline, greedy, hillclimber
from code.classes import grid
from code.visualisations.visualise import visualise as vis
        
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
    valid_grid = greedy.Greedy.constrained_greedy(10)
    #valid_grid.print_grid()

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # climber.run(50)

    # --------------------------------- Visualise --------------------------------------
    vis.visualise(valid_grid, test_grid)
