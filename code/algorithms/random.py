# Import copy, random and statistics.
import copy

# Import grid from classes.
from code.classes import grid

class Random():
    """
    Baseline algorithm randomly connects houses to batteries. Unconstrained version does not take max capacity into account,
    constrained version does.
    """

    def __init__(self, tries, district):
        self.score_list = []
        self.best_random_unc = None
        self.best_random_con = None
        self.tries = tries
        self.false_tries = 0
        self.district = district
        self.test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
        self.test_grid.district = district

    def unconstrained_random(self):
        """
        Randomly connects houses to batteries.
        """ 

        # Loop for a given number of tries to create a new grid.
        for x in range(self.tries):
            # Make a deepcopy.
            grid = copy.deepcopy(self.test_grid)

            # Loop for each grid through all available houses.
            for i in range(len(grid.houses)):
                # Select a random house from the list of houses.
                house = grid.pick_random_house(grid.houses, i)

                # Select a random battery from the list of batteries.
                random_bat = grid.pick_random_bat(grid.batteries)

                # Connect the house to the battery.
                house.add_bat(random_bat)

                # Create a cable between house and battery.
                grid.lay_cable(random_bat, house)

            # Calculate the total length of cable for this try.
            grid.calc_dist()

            # Remember if its the best try.
            self.keep_track_random_unc(grid, self.best_random_unc)

    def constrained_random(self):
        """
        Randomly connects houses to batteries, with battery capacity constraints.
        """
        # Loop through the number of tries.
        for x in range(self.tries):
            # Make a deepcopy and shuffle the list
            grid = copy.deepcopy(self.test_grid)
            grid.shuffle_list(grid.houses)
            
            # For every house.
            for i in range(len(grid.houses)):
                # Select a random house and a random bat.
                house = grid.pick_random_house(grid.houses, i)
                random_bat = grid.pick_random_bat(grid.batteries)
                
                # Break if there is no battery available, else connect house to a battery.
                if not grid.bat_available(house):
                    self.false_try(grid)
                    break
                else:
                    grid.connect_house_random_con(house, random_bat)

            # If this grid is valid, calculate the distance and keep track of random.     
            if grid.is_valid:
                grid.calc_dist()
                self.keep_track_random_con(grid, self.best_random_con)

    def keep_track_random_unc(self, new_grid, best_grid):
        """
        Function that keeps track of the best grid score in the unconstrained version.
        """

        if self.best_random_unc is None:
            self.best_random_unc = new_grid
        elif new_grid.score < best_grid.score:
            self.best_random_unc = new_grid

    def keep_track_random_con(self, new_grid, best_grid):
        """
        Function that keeps track of the best grid score in the constrained version.
        """

        if self.best_random_con is None:
            self.best_random_con = new_grid
        elif new_grid.score < best_grid.score:
            self.best_random_con = new_grid

    def print_stats_random_unc(self):
        """
        Function that prints the statistics of the random unconstrained version.
        """

        min_dist = self.best_random_unc.score
        print(f"The best try has a distance of {min_dist}")

    def print_stats_random_con(self):
        """
        Function that prints the statistics of the random constrained version.
        """

        min_dist = self.best_random_con.score
        print(f"The best try has a distance of {min_dist}")

    def false_try(self, grid):
        """
        Function that keeps track of false tries.
        """

        grid.is_valid = False
        self.false_tries += 1

    def run_unconstrained(self):
        """
        Function to run Random uncontrained.
        """

        self.unconstrained_random()
        self.print_stats_random_unc()
        return self.best_random_unc
    
    def run_constrained(self):
        """
        Function to run Random contrained.
        """
        
        self.constrained_random()
        if self.best_random_con is not None:
            self.print_stats_random_con()
            return self.best_random_con
        else:
            print("No valid result found")