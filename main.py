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
<<<<<<< HEAD
    # random = random.Random(1000)
    # random_grid = random.run()
    

    # --------------------------------- Greedy --------------------------------------------
    greedy.Greedy.constrained_greedy(100000)
    # valid_grid.print_grid()
=======
    # rando = random.Random(1000)
    # rando.run()

    # --------------------------------- Greedy --------------------------------------------
    greed = greedy.Greedy(10)
    greed.run()
>>>>>>> d3c6c3c292a0f64f48afab54a87d7f3a98f8c100

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # climber.run(50)

    # --------------------------------- Visualise --------------------------------------
    # vis.visualise(valid_grid, test_grid)
