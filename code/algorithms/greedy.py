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
            house.add_house(bat)
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

            c1 = 0
            c2 = 0
            c3 = 0
            c4 = 0
            c5 = 0

            # loop through the houses on the grid
            for house in grid.houses:
                available_bats = []
                battery_distances = []
                unavailable_bats = []
                unavailable_distances = []

                # check which batteries are still available for this house and append to list
                for bat in grid.batteries:
                    if float(house.output) < float(bat.capacity_left):
                        available_bats.append(bat)
                    else:
                        unavailable_bats.append(bat)
                
                # save the number of options the house had to connect
                house.bat_options = len(available_bats)
                # print(house.bat_options)
                if house.bat_options == 5:
                    c5 += 1
                elif house.bat_options == 4:
                    c4 += 1
                elif house.bat_options == 3:
                    c3 += 1
                elif house.bat_options == 2:
                    c2 += 1
                elif house.bat_options == 1:
                    c1 += 1

                # ik weet niet of dit nuttig gaat zijn maar wellicht 
                # calculate distances to unavailable batteries
                if unavailable_bats:
                    for battery in unavailable_bats:
                        dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
                        unavailable_distances.append(dist)

                # break out of the loop if there are no available batteries left
                if not grid.bat_available(house):
                    self.false_try(grid)
                    is_valid = False
                    failed_attempts += 1
                    break

                # calculate the distances from the house to all available batteries and append to list
                for battery in available_bats:
                    dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
                    battery_distances.append(dist)

                # get shortest distance to a battery and the battery's index in list
                shortest_dist = min(battery_distances)
                shortest_dist_index = battery_distances.index(min(battery_distances))

                # add the closest battery to the house and lay a cable
                closest_battery = available_bats[shortest_dist_index]
                house.bats.append(closest_battery)
                grid.lay_cable(closest_battery, house)

                # subtract the output of the house from the remaining capacity of the battery
                closest_battery.capacity_left -= float(house.output)             

                # keep track of cable length per house and add to cable length of the try
                sum_cables += shortest_dist

            c = c1 + c2 +c3 +c4 +c5

            print (c5, c4, c3, c2, c1, c)

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
        avg_dist = total_dist / valid_attempts
        print(f"\nThe shortest distance is {min_sum_cables}")
        print(f"The average distance is {avg_dist}\n")
        print(f"The number of valid attempts is {valid_attempts}")
        print(f"The number of failed attempts is {failed_attempts}")

    def run_unconstrained(self):
        """
        This function runs our unconstrained greedy algorithm
        """
        self.unconstrained_greedy()
        return super().run()

    def run_constrained(self):
        """
        This function runs our contrained greedy algorithm
        """
        self.constrained_greedy()
        return self.best_try
        


    