from code.algorithms import random, greedy, hillclimber
from code.classes import grid
from code.visualisations import visualise as vis
        
if __name__ == "__main__":

    # --------------------------------- Random ----------------------------------------------------------------
    # random_algorithm = random.Random(10)
    # valid_grid = random_algorithm.run()

    # --------------------------------- Greedy UNCONSTRAINED----------------------------------------------------
    # greed = greedy.Greedy(1)
    # valid_grid = greed.run_unconstrained()
    

    # ---------------------------------------- Greedy CONSTRAINED -----------------------------------------------
    # greed = greedy.Greedy(10)
    # valid_grid = greed.run_constrained()

    # ----------------------------------------- Hill Climber ----------------------------------------------------
    # greed = greedy.Greedy(10)
    # climber = hillclimber.HillClimber(valid_grid)
    # print(f"Running HillClimber...")
    # climber.run(100)

    # --------------------------------------- Visualise ---------------------------------------------------------
    # vis.visualise(valid_grid)

    ##############################################################################################################
    ############################################# SHARED CABLES ##################################################
    ##############################################################################################################

    # --------------------------------- Greedy SHARED UNCONSTRAINED ----------------------------------------------
    # greed = greedy.Greedy(1)
    # valid_grid = greed.run_shared_unc()
 

    # --------------------------------- Greedy SHARED CONSTRAINED ----------------------------------------------
    greed = greedy.Greedy(1000)
    valid_grid = greed.run_shared_con()
 
    # -------------------------------------- Visualise ----------------------------------------------------
    vis.visualise_shared(valid_grid)



    # output = valid_grid.output()
    # return output
    ## print de totale kosten TOTAL COST: $ ...! 
