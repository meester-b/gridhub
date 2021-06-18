from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations import visualise as vis
        
if __name__ == "__main__":
    district = "2"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     
    # print(test_grid)
    # print(visualise())
    # test_grid.print_grid()

    ## call algorithms
    # --------------------------------- Random ------------------------------------------
    rando = random.Random(50000)
    valid_grid = rando.run()
    print(valid_grid)

    # --------------------------------- Greedy --------------------------------------------
    # greed = greedy.Greedy(10)
    # greed.run()
    # valid_grid = greedy.Greedy.constrained_greedy(test_grid)
    # print(valid_grid)

    # --------------------------------- Hill Climber --------------------------------------
    climber = hillclimber.HillClimber(valid_grid)
    print(f"Running Hillclimber...")
    climber.run(100)

    # --------------------------------- Visualise --------------------------------------
    #vis.visualise(valid_grid)
