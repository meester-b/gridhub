from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations import visualise as vis
        
if __name__ == "__main__":

    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     

    # --------------------------------- Random ------------------------------------------
<<<<<<< HEAD
    rando = random.Random(50000)
    valid_grid = rando.run()
    print(valid_grid)

    # --------------------------------- Greedy --------------------------------------------
    # greed = greedy.Greedy(10)
    # greed.run()
    # valid_grid = greedy.Greedy.constrained_greedy(test_grid)
    # print(valid_grid)
=======
    # random_algorithm = random.Random(100)
    # valid_grid = random_algorithm.run()
    # print(valid_grid)

    # --------------------------------- Greedy UNCONSTRAINED--------------------------------------------
    greed = greedy.Greedy(100)
    # valid_grid = greed.run_unconstrained()
    valid_grid = greed.run_constrained()

    # --------------------------------- Greedy CONSTRAINED ----------------------------------------------
    # greed = greedy.Greedy(8)
    # valid_grid = greed.run_constrained()
    # print(valid_grid.score) 
>>>>>>> 8679b1024cb82c1bcd2285180e5c5a2471313a3d

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # print(f"Running HillClimber...")
    # climber.run(10000)

    # --------------------------------- Visualise --------------------------------------
    #vis.visualise(valid_grid)
