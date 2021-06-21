from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations import visualise as vis
        
if __name__ == "__main__":

    # district = "1"

    # test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
     

    # --------------------------------- Random ------------------------------------------
    # random_algorithm = random.Random(10)
    # valid_grid = random_algorithm.run()

    # --------------------------------- Greedy UNCONSTRAINED--------------------------------------------
    # greed = greedy.Greedy(1)
    # valid_grid = greed.run_unconstrained()
    

    # --------------------------------- Greedy CONSTRAINED ----------------------------------------------
    # greed = greedy.Greedy(1000)
    # valid_grid = greed.run_constrained()

    # --------------------------------- Greedy SHARED UNCONSTRAINED ----------------------------------------------
    greed = greedy.Greedy(10000)
    valid_grid = greed.run_shared_con()
 

    # --------------------------------- Greedy SHARED CONSTRAINED ----------------------------------------------
    # greed = greedy.Greedy(1)
    # valid_grid = greed.run_shared_con()
 
    # --------------------------------- Hill Climber --------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # print(f"Running HillClimber...")
    # climber.run(100)

    # --------------------------------- Visualise --------------------------------------
    # vis.visualise(valid_grid)
    vis.visualise_shared(valid_grid)

    # output = valid_grid.output()
    # return output
    ## print de totale kosten TOTAL COST: $ ...! 
