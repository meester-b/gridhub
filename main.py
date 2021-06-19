from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations import visualise as vis
        
if __name__ == "__main__":

    district = "3"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     

    # --------------------------------- Random ------------------------------------------
    # random_algorithm = random.Random(100)
    # valid_grid = random_algorithm.run()

    # --------------------------------- Greedy UNCONSTRAINED--------------------------------------------
    greed = greedy.Greedy(1)
    valid_grid = greed.run_unconstrained()
    

    # --------------------------------- Greedy CONSTRAINED ----------------------------------------------
    # greed = greedy.Greedy(1000)
    # valid_grid = greed.run_constrained()

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # print(f"Running HillClimber...")
    # climber.run(1000)

    # --------------------------------- Visualise --------------------------------------
    # vis.visualise(valid_grid)
