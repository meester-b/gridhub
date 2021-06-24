from code.algorithms import random, greedy, hillclimber, annealing
from code.classes import grid
from code.visualisations import visualise as vis


if __name__ == "__main__":
    
    # 1) Which district?
    while True:
        district = int(input("Which district do you want to work with? (1/2/3) "))
        if district not in [1, 2, 3]:
            print("Please enter only the number 1, 2 or 3")
            continue
        else:
            break

    # 2) Cable sharing?
    while True:
        sharing = input("Do you want to allow cable sharing? (Y/N) ")
        if sharing.lower() not in ('y', 'n'):
            print("Please enter only 'Y' or 'N'")
            continue
        else:
            break

    # 3) Constraints?
    while True:
        constraints = input("Do you want to respect the constraints? (Y/N) ")
        if constraints.lower() not in ('y', 'n'):
            print("Please enter only 'Y' or 'N'")
            continue
        else:
            break
    
    # 4) Number of tries?
    while True:
        tries = int(input("How many times do you want to run your chosen algorithm(s)? "))
        if tries < 1:
            print("Number of tries must be above 0")
            continue
        else:
            break

    # No cable sharing algorithms
    if sharing.lower() == 'n':
        
        if constraints.lower() == 'n':
            while True:
                greedy_random_unc = input("Do you want to run the RANDOM (R) or GREEDY (G) algorithm? (R/G) ")
                if greedy_random_unc.lower() not in ('r', 'g'):
                    print("Please pick either 'R' or 'G'!")
                    continue
                else:
                    break
            
            if greedy_random_unc.lower() == 'r':
                random_algorithm = random.Random(tries, district)
                print(f"Running Random unconstrained...")
                grid = random_algorithm.run_unconstrained()
                vis.visualise(grid)
                print("Open results/not shared/grid.png to see the results!")

            elif greedy_random_unc.lower() == 'g':
                greed = greedy.Greedy(tries, district)
                print(f"Running Greedy unconstrained...")
                grid = greed.run_unconstrained()
                vis.visualise(grid)
                print("Open results/not shared/grid.png to see the results!")
        
        elif constraints.lower() == 'y':
            while True:
                greedy_random_con = input("Do you want to run the RANDOM (R) or GREEDY (G) algorithm? (R/G) ")
                if greedy_random_con.lower() not in ('r', 'g'):
                    print("Please pick either 'R' or 'G'!")
                    continue
                else:
                    break

            if greedy_random_con.lower() == 'r':
                random_algorithm = random.Random(tries, district)
                print(f"Running Random constrained...")
                valid_grid = random_algorithm.run_constrained()
                if valid_grid is not None:
                    vis.visualise(valid_grid)
                    print("Open results/not shared/grid.png to see the results!")
                    
                    while True:
                        hill_sim = input("Would you like to improve your grid with a HILLCLIMBER (H) or SIMULATED ANNEALING (S) algorithm or NOT (N)? ")
                        if hill_sim.lower() not in ('h', 's', 'n'):
                            print("Please pick an improvement algorithm with 'H' or 'S' or answer 'N' if you're done!")
                            continue
                        else:
                            break
                
                    if hill_sim.lower() == 'h':
                        climber = hillclimber.HillClimber(valid_grid)
                        print(f"Running HillClimber...")
                        climber.run(tries)
                        vis.visualise(valid_grid)
                        print("Open results/not shared/grid.png to see the results!")
                    
                    elif hill_sim.lower() == 's':
                        annealing = annealing.Annealing(valid_grid)
                        print(f"Running Simulated Annealing...")
                        annealing.run(tries)
                        vis.visualise(valid_grid)
                        print("Open results/not shared/grid.png to see the results!")

            elif greedy_random_con.lower() == 'g':
                greed = greedy.Greedy(tries, district)
                print(f"Running Greedy constrained...")
                valid_grid = greed.run_constrained()
                if valid_grid is not None:
                    vis.visualise(valid_grid)
                    print("Open results/not shared/grid.png to see the results!")


    # Cable sharing algorithms
    elif sharing.lower() == 'y':
        
        if constraints.lower() == 'n':
            greed = greedy.Greedy(tries, district)
            print(f"Running Greedy shared unconstrained...")
            valid_grid = greed.run_shared_unc()
            vis.visualise_shared(valid_grid)
            print("Open results/shared cables/grid_shared.png to see the results!")
        
        elif constraints.lower() == 'y':
            greed = greedy.Greedy(tries, district)
            print(f"Running Greedy shared constrained...")
            valid_grid = greed.run_shared_con()
            if valid_grid is not None:
                vis.visualise_shared(valid_grid)
                print("Open results/shared cables/grid_shared.png to see the results!")