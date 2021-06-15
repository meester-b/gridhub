import copy
import random

from code.classes import grid
from .random import Random

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

# TODO: run function    

class Greedy(Random):
    def __init__(self, tries):
        super().__init__(tries)
        self.best_greedy_unc = None
        self.best_greedy_con = None

    def unconstrained_greedy(self):
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """

        grid = copy.deepcopy(test_grid)

        # to summarize cable lenghts
        # min_sum_cables = 0

        # for every house an empty list
        for house in grid.houses:
            bat = grid.pick_closest_battery(house)
            bat.add_house(house)
            grid.lay_cable(bat, house)

        grid.calc_dist()
        self.keep_track_greedy_unc(grid)

    def constrained_greedy(self):
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """
        
        # keep track of try valid ratio
        failed_attempts = 0
        valid_attempts = 0 

        # keep track of vars acrros tries
        min_sum_cables = 0
        total_dist = 0

        # try x amount of times
        for x in range(self.tries):
            # make deepcopy
            grid = copy.deepcopy(test_grid)
            best_try = grid
            random.shuffle(grid.houses)
            # each try starts as valid
            is_valid = True
            # keep track of current try
            sum_cables = 0

            # empty list per house
            for house in grid.houses:
                distances = []
                available_bat = []

                # check which battery is still usable for this house
                for bat in grid.batteries:
                    if float(house.output) < float(bat.capacity_left):
                        available_bat.append(bat)

                # stop try if invalid and count 
                if not available_bat:
                    is_valid = False
                    failed_attempts += 1
                    break
                
                # calc all distances to batteries from houses and append to list
                for battery in available_bat:
                    dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
                    distances.append(dist)

                # get shortest distance and its index in list
                closest_house = min(distances)
                closest_house_index = distances.index(min(distances))


                # add house to closest valid battery if 
                available_bat[closest_house_index].houses.append(closest_house)
                available_bat[closest_house_index].capacity_left -= float(house.output)

                # keep track of length per try
                sum_cables += closest_house


            # count valid tries
            if is_valid:
                valid_attempts +=1 

            # count minimum and sum across tries
            if is_valid:
                # first valid try is minimum
                if valid_attempts == 1:
                    min_sum_cables = sum_cables

                # update if new try is better
                if sum_cables < min_sum_cables:
                    min_sum_cables = sum_cables
                    best_try = grid

                # sum total dist
                total_dist += sum_cables
        
        # calc average
        avg_dist = total_dist / valid_attempts

        # print statistics
        print(f"\nThe shortest distance is {min_sum_cables}")
        print(f"The average distance is {avg_dist}\n")
        print(f"The amount of valid attempts is {valid_attempts}")
        print(f"The amount of failed attempts is {failed_attempts}")
        # print(f"Best try is {best_try}")

        return best_try



    def keep_track_greedy_unc(self, grid):
        if self.best_greedy_con is None:
            self.best_greedy_unc = grid

    def keep_track_greedy_con(self, new_grid, best_grid):
        if self.best_greedy_con is None:
            self.best_greedy_unc = new_grid
        elif new_grid.score < best_grid.score:
            self.best_greedy_con = new_grid

    def print_stats_greedy(self):
        min_dist_unc = self.best_greedy_unc.score
        # min_dist_con = self.best_greedy_con.score
        print(f"The best try has a distance of {min_dist_unc}")
        # \nThe best valid try has a dist of {min_dist_con}")

    def run(self):
        self.unconstrained_greedy()
        # self.constrained_greedy()
        self.print_stats_greedy()
        # return super().run()
        

    