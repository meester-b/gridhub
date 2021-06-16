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
        self.best_random_unc = None
        self.best_random_con = None
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
                house = grid.pick_random_house(grid.houses)
                
                # select a random battery from the list of batteries
                random_bat = grid.pick_random_bat(grid.batteries)

                # connect the house to the battery
                random_bat.add_house(house)

                # create a cable between house and battery
                grid.lay_cable(random_bat, house)

            # calc the total length of cable for this try
            grid.calc_dist()

            # remember if its the best try
            self.keep_track_random_unc(grid, self.best_random_unc)

    def constrained_random(self):
        '''
        Randomly connects houses to batteries, with battery constraints.
        '''

        for x in range(self.tries):
            grid = copy.deepcopy(test_grid)

            while grid.houses:
                house = grid.pick_random_house(grid.houses)
                random_bat = grid.pick_random_bat(grid.batteries)

                if not grid.bat_available(house):
                    self.false_try(grid)
                    break
                else:
                    grid.connect_house_random_con(house, random_bat)
                    
            if grid.is_valid:
                grid.calc_dist()
                self.keep_track_random_con(grid, self.best_random_con)

    def keep_track_random_unc(self, new_grid, best_grid):
        if self.best_random_unc is None:
            self.best_random_unc = new_grid
        elif new_grid.score < best_grid.score:
            self.best_random_unc = new_grid

    def keep_track_random_con(self, new_grid, best_grid):
        if self.best_random_con is None:
            self.best_random_con = new_grid
        elif new_grid.score < best_grid.score:
            self.best_random_con = new_grid

    def print_stats_random(self):
        min_dist_unc = self.best_random_unc.score
        min_dist_con = self.best_random_con.score
        print(f"The best try has a distance of {min_dist_unc} \nThe best valid try has a dist of {min_dist_con}")

    def false_try(self, grid):
        grid.is_valid = False
        self.false_tries += 1

    def run(self):
        self.unconstrained_random()
        self.constrained_random()  
        self.print_stats_random()
        return self.best_random_con
