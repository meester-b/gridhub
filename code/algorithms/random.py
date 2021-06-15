import copy
import random
import statistics

from code.classes import grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

class Random():
    '''
    Baseline algorithm randomly connects houses to batteries. Unconstrained version does not take max capacity into account,
    constrained version does.
    '''
    def __init__(self, tries):
        self.score_list = []
        self.best_try_unc = None
        self.best_try_con = None
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
            self.keep_track_unc(grid, self.best_try_unc)

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
                self.keep_track_con(grid, self.best_try_con)

    def keep_track_unc(self, new_grid, best_grid):
        if self.best_try_unc is None:
            self.best_try_unc = new_grid
        elif new_grid.score < best_grid.score:
            self.best_try_unc = new_grid

    def keep_track_con(self, new_grid, best_grid):
        if self.best_try_con is None:
            self.best_try_con = new_grid
        elif new_grid.score < best_grid.score:
            self.best_try_con = new_grid

    def print_stats(self):
        min_dist_unc = self.best_try_unc.score
        min_dist_con = self.best_try_con.score
        print(f"The best try has a distance of {min_dist_unc} \n The best valid try has a dist of {min_dist_con}")

    def false_try(self, grid):
        grid.is_valid = False
        self.false_tries += 1

    def run(self):
        self.unconstrained_random()
        self.constrained_random()  
        self.print_stats()
