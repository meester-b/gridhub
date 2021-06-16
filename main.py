from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations import visualise as vis
<<<<<<< HEAD

=======
>>>>>>> 961fd40b9a55beb8260a760eb795ebb7ec12527d
        
if __name__ == "__main__":
    district = "1"

    test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     
    # print(test_grid)
    # print(visualise())
    # test_grid.print_grid()

    ## call algorithms
    # --------------------------------- Random ------------------------------------------
<<<<<<< HEAD
# <<<<<<< HEAD
    # random = random.Random(10)
    # random.run()
    

    # --------------------------------- Greedy --------------------------------------------
#     valid_grid = greedy.Greedy.constrained_greedy(10)
# # =======
# <<<<<<< HEAD
#     # random = random.Random(1000)
    # random_grid = random.run()
    

    # --------------------------------- Greedy --------------------------------------------
#     greedy.Greedy.constrained_greedy(100000)
# >>>>>>> 394ccb98857370e6c68e16e4a8470d207541e23c
#     # valid_grid.print_grid()
# =======
#     # rando = random.Random(1000)
    # rando.run()

    # --------------------------------- Greedy --------------------------------------------
#     greed = greedy.Greedy(10)
#     greed.run()
# >>>>>>> d3c6c3c292a0f64f48afab54a87d7f3a98f8c100
=======
    rando = random.Random(100)
    valid_grid = rando.run()
    # print(valid_grid)s

    # --------------------------------- Greedy --------------------------------------------
    # greed = greedy.Greedy(10)
    # greed.run()
>>>>>>> 961fd40b9a55beb8260a760eb795ebb7ec12527d

    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # print(f"Running Hillclimber...")
    # climber.run(100)

    # --------------------------------- Visualise --------------------------------------
    vis.visualise(valid_grid)
