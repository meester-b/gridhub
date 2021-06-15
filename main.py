from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations.visualise import visualise as vis
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     
    # print(test_grid)
    # print(visualise())
    # test_grid.print_grid()

    ## call algorithms
    # --------------------------------- Random ------------------------------------------
    random = random.Random(1000)
    random.run()
    

    # --------------------------------- Greedy --------------------------------------------
    # valid_grid = greedy.Greedy.constrained_greedy(10)
    # valid_grid.print_grid()

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # climber.run(50)

    # --------------------------------- Visualise --------------------------------------
    # vis.visualise(valid_grid, test_grid)
