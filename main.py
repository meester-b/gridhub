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
    # rando = random.Random(1000)
    # rando.run()

    # --------------------------------- Greedy --------------------------------------------
    greed = greedy.Greedy(10)
    greed.run()

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # climber.run(50)

    # --------------------------------- Visualise --------------------------------------
    # vis.visualise(valid_grid, test_grid)
