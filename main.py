from code.algorithms import random, greedy, hillclimber, annealing, iterative
from code.classes import grid
from code.visualisations import visualise as vis

import sys


if __name__ == "__main__":

    if len(sys.argv) == 1:
        pass

    # --------------------------------------------- Random UNCONSTRAINED-------------------------------------------------------
    # random_algorithm = random.Random(10)
    # valid_grid = random_algorithm.run_unconstrained()

    # --------------------------------------------- Random CONSTRAINED-------------------------------------------------------
    # random_algorithm = random.Random(50)
    # valid_grid = random_algorithm.run_constrained()

    # ---------------------------------------------- Greedy UNCONSTRAINED-----------------------------------------
    # greed = greedy.Greedy(10)
    # valid_grid = greed.run_unconstrained()

    # --------------------------------------- Greedy CONSTRAINED ------------------------------------------------
    # greed = greedy.Greedy(30)
    # valid_grid = greed.run_constrained()

    # ----------------------------------------- Hill Climber ----------------------------------------------------
    # climber = hillclimber.HillClimber(valid_grid)
    # print(f"Running HillClimber...")
    # climber.run(1000)

    # ------------------------------------------ Simulated Annealing -------------------------------------------
    # annealing = annealing.Annealing(valid_grid)
    # print(f"Running Simulated Annealing...")
    # annealing.run(1000)

    # --------------------------------------- Visualise ---------------------------------------------------------
    # vis.visualise(valid_grid)

    ##############################################################################################################
    ############################################# SHARED CABLES ##################################################
    ##############################################################################################################

    # --------------------------------- Greedy SHARED UNCONSTRAINED ----------------------------------------------
    greed = greedy.Greedy(1)
    valid_grid = greed.run_shared_unc()

    # --------------------------------- Greedy SHARED CONSTRAINED ----------------------------------------------
    # greed = greedy.Greedy(100)
    # valid_grid = greed.run_shared_con()
 
    # ---------------------------------- Iterative -------------------------------------------------------------
    # iterate = iterative.Iterative(valid_grid)
    # valid_grid = iterate.run()
    
    # -------------------------------------- Visualise ----------------------------------------------------
    # vis.visualise_shared(valid_grid)


    # output = valid_grid.output()
    # return output
    ## print de totale kosten TOTAL COST: $ ...! 
