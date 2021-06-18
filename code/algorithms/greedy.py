import copy
import random

from code.classes import grid
from .random import Random

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")
  

class Greedy(Random):
    """
    Greedy inherits the functions of Random
    """
    def __init__(self, tries):
        """
        Initialialize Greedy
        """
        super().__init__(tries)
        self.best_greedy_unc = None
        self.best_greedy_con = None
        self.best_try = None

    def unconstrained_greedy(self):
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """

        grid = copy.deepcopy(test_grid)

        # for every house an empty list
        for house in grid.houses:
            bat = grid.pick_closest_battery(house)
            house.add_bat(bat)
            grid.lay_cable(bat, house)

        grid.calc_dist()
        self.keep_track_greedy_unc(grid)

        # return self.best_greedy_unc

    def constrained_greedy(self):
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """
        
        # keep track of try valid ratio
        failed_attempts = 0
        valid_attempts = 0 

        # keep track of variables across tries
        min_sum_cables = 0
        total_dist = 0

        # loop through the number of tries
        for x in range(self.tries):
            
            # make deepcopy
            grid = copy.deepcopy(test_grid)
            
            # shuffle the houses in the grid
            random.shuffle(grid.houses)
            
            # each try starts as valid
            is_valid = True
            
            # keep track of the cable length in the current try
            sum_cables = 0

            # c1 = 0
            # c2 = 0
            # c3 = 0
            # c4 = 0
            # c5 = 0

            # loop through the houses on the grid
            for house in grid.houses:

                # check which batteries are still available for this house and append to list
                for bat in grid.batteries:
                    dist = abs(house.y_coordinate - bat.y_coordinate) + abs(house.x_coordinate - bat.x_coordinate)
                    if house.output < bat.capacity_left:
                        house.available_bats[bat] = dist
                    else:
                        house.unavailable_bats[bat] = dist
                
                # save the number of options the house had to connect
                # house.bat_options = len(available_bats)
                # print(house.bat_options)
                # if house.bat_options == 5:
                #     c5 += 1
                # elif house.bat_options == 4:
                #     c4 += 1
                # elif house.bat_options == 3:
                #     c3 += 1
                # elif house.bat_options == 2:
                #     c2 += 1
                # elif house.bat_options == 1:
                #     c1 += 1


                # break out of the loop if there are no available batteries left
                if not grid.bat_available(house):
                    self.false_try(grid)
                    is_valid = False
                    failed_attempts += 1
                    break

                # get closest battery and its distance and lay cable from battery to the house
                closest_battery = min(house.available_bats, key=house.available_bats.get)
                shortest_dist = house.available_bats.get(closest_battery)
                house.bats.append(closest_battery)
                grid.lay_cable(closest_battery, house)

                # subtract the output of the house from the remaining capacity of the battery
                closest_battery.capacity_left -= float(house.output)             

                # keep track of cable length per house and add to cable length of the try
                sum_cables += shortest_dist

            # count valid tries
            if is_valid:
                valid_attempts +=1 

            # count minimum and sum across tries
            if is_valid:
                
                # first valid try is minimum and automatically the best try
                if valid_attempts == 1:
                    min_sum_cables = sum_cables
                    self.best_try = grid
                    self.best_try.score = sum_cables

                # update if new try is better
                if sum_cables < min_sum_cables:
                    min_sum_cables = sum_cables
                    self.best_try = grid
                    self.best_try.score = sum_cables

                # add all cables to the total cable distance of the grid
                total_dist += sum_cables

        # print statistics
        self.print_stats_greedy(total_dist, min_sum_cables, valid_attempts, failed_attempts)

        # return best try
        return self.best_try

    def keep_track_greedy_unc(self, grid):
        """
        Function that keeps track of 
        """
        if self.best_greedy_unc is None:
            self.best_greedy_unc = grid

    def keep_track_greedy_con(self, new_grid, best_grid):
        """
        
        """
        if self.best_greedy_con is None:
            self.best_greedy_con = new_grid
        elif new_grid.score < best_grid.score:
            self.best_greedy_con = new_grid
    
    def print_stats_greedy(self, total_dist, min_sum_cables, valid_attempts, failed_attempts):
        """
        Function that prints the statistics
        """
        if valid_attempts > 0:
            avg_dist = total_dist / valid_attempts
        else:
            avg_dist = 0
        print(f"\nThe shortest distance is {min_sum_cables}")
        print(f"The average distance is {avg_dist}\n")
        print(f"The number of valid attempts is {valid_attempts}")
        print(f"The number of failed attempts is {failed_attempts}")

    def run_unconstrained(self):
        """
        This function runs our unconstrained greedy algorithm
        """
        self.unconstrained_greedy()
        print(self.best_greedy_unc.score)
        return self.best_greedy_unc

    def run_constrained(self):
        """
        This function runs our constrained greedy algorithm
        """
        self.constrained_greedy()
        print(self.best_try.score)
        return self.best_try
        


    