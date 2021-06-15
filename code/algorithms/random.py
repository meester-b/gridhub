import copy
import random
import statistics

from code.classes import grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

# TODO: run function

class Random():
    '''
    Baseline algorithm randomly connects houses to batteries. Unconstrained version does not take max capacity into account,
    constrained version does.
    '''
    def __init__(self, tries):
        self.score_list = []
        self.best_try = None
        self.best_con_try = None
        # tries meegeven met object 
        self.tries = tries
        self.false_tries = 0

    def unconstrained_random(self):
        '''
        Randomly connects houses to batteries.
        '''    
        # loop for a given number of tries to create a new grid
        for x in range(self.tries):

            # make a deepcopy
            grid = copy.deepcopy(test_grid)

            # loop for each grid through all available houses
            while grid.houses:
                
                # select a random house from the list of houses
                connecting_house = grid.pick_random_house(grid.houses)
                
                # select a random battery from the list of batteries
                random_bat = grid.pick_random_bat(grid.batteries)

                # connect the house to the battery
                random_bat.add_house(connecting_house)

                # create a cable between house and battery
                grid.lay_cable(random_bat, connecting_house)

            # calc the total length of cable for this try
            grid.calc_dist()

            # remember if its the best try
            self.keep_track(grid, self.best_try)

        self.print_stats()

    def constrained_random(self):
        '''
        Randomly connects houses to batteries, with battery constraints.
        '''
        grid_distances = []

        for x in range(self.tries):
            grid = copy.deepcopy(test_grid)

            while grid.houses:
                connecting_house = grid.pick_random_house(grid.houses)
                random_bat = grid.pick_random_bat(grid.batteries)

                if not grid.bat_available(connecting_house):
                    self.false_try(grid)
                    break
                else:
                    grid.connect_house_con(connecting_house, random_bat)
                    
            if grid.is_valid:
                grid.calc_dist()
                self.keep_track(grid, self.best_try)

        self.print_stats()
        
        # shortest_dist = grid_distances[0]
        # sum_dist = 0

        # for dist in grid_distances:
        #     sum_dist += dist

        #     if dist < shortest_dist:
        #         shortest_dist = dist

        # avg_dist = sum_dist / len(grid_distances)

        # print output
        # print(f"\nThe shortest distance is {shortest_dist}")
        # print(f"The average distance is {avg_dist}\n")
        # print(f"The amount of failed attempts is {failed_attempts}")
        # print(f"The amount of valid attempts is {len(grid_distances)}\n")


    ## naar grid
    # def calc_dist(self, grid):
    #     sum = 0

    #     for bat in grid.batteries:
    #         for cable in bat.cables:
    #             sum += cable.length

        # self.score_list.append(sum)

    def keep_track(self, new_grid, best_grid):
        if self.best_try is None:
            self.best_try = new_grid
        elif new_grid.score < best_grid.score:
            self.best_try = new_grid

    



    def print_stats(self):
        min_dist = self.best_try.score
        # mean_dist = statistics.mean(self.score_list)

        print(f"The best try has a distance of {min_dist}")

    # \nThe average distance is {mean_dist}

    def false_try(self, grid):
        grid.is_valid = False
        self.false_tries += 1
