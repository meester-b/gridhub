from code.algorithms import random, greedy, hillclimber, annealing, iterative
from code.classes import grid
from code.visualisations import visualise as vis

import sys


if __name__ == "__main__":
    
    # 1) Which district?
    # while True:
    #     district = int(input("Which district do you want to work with? (1/2/3) "))
    #     if district not in [1, 2, 3]:
    #         print("Please enter only the number 1, 2 or 3")
    #         continue
    #     else:
    #         break

    # 2) Cable sharing?
    # while True:
    #     sharing = input("Do you want to allow cable sharing? (Y/N) ")
    #     if sharing.lower() not in ('y', 'n'):
    #         print("Please enter only 'Y' or 'N'")
    #         continue
    #     else:
    #         break
    
    # if sharing == 'n' or sharing == 'N':

    #### NO SHARING
    # do you want to allow constraints?
    # y or n
    # NO (unconstrained)
    # Random, greedy

    # YES (constrained) 
    # loading valid solutions
    # random, greedy 
    # greedy --> local optimum reached
    # on random --> do you want to use Hillclimb or Annealing


    #### SHARING
   # do you want to allow constraints?
    # y or n
    # NO (unconstrained)
    # run greedy

    # YES (constrained) 
    # run greedy
    # do you want to use iterative?



    # if len(sys.argv) == 1:
    #     pass

    # --------------------------------------------- Random UNCONSTRAINED-------------------------------------------------------
    # random_algorithm = random.Random(10)
    # print(f"Running Random unconstrained...")
    # valid_grid = random_algorithm.run_unconstrained()

    # --------------------------------------------- Random CONSTRAINED-------------------------------------------------------
    # random_algorithm = random.Random(50)
    # print(f"Running Random constrained...")
    # valid_grid = random_algorithm.run_constrained()

    # ---------------------------------------------- Greedy UNCONSTRAINED-----------------------------------------
    # greed = greedy.Greedy(10)
    # print(f"Running Greedy unconstrained...")
    # valid_grid = greed.run_unconstrained()

    # --------------------------------------- Greedy CONSTRAINED ------------------------------------------------
    # greed = greedy.Greedy(30)
    # print(f"Running Greedy constrained...")
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
    # greed = greedy.Greedy(1)
    # print(f"Running Greedy shared unconstrained...")
    # valid_grid = greed.run_shared_unc()

    # --------------------------------- Greedy SHARED CONSTRAINED ----------------------------------------------
    greed = greedy.Greedy(15)
    # print(f"Running Greedy shared constrained...")
    valid_grid = greed.run_shared_con()
 
    # ---------------------------------- Iterative -------------------------------------------------------------
    iterate = iterative.Iterative(valid_grid)
    # print(f"Running Iterative...")
    valid_grid = iterate.run()
    
    # -------------------------------------- Visualise ----------------------------------------------------
    vis.visualise_shared(valid_grid)


    # output = valid_grid.output()
    # return output
    ## print de totale kosten TOTAL COST: $ ...! 
