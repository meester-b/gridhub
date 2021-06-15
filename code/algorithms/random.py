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
        # tries meegeven met object 
        self.tries = tries

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

    def constrained_baseline(tries):
        '''
        Randomly connects houses to batteries, with battery constraints.
        '''
        grid_distances = []
        failed_attempts = 0

        for x in range(tries):
            grid = copy.deepcopy(test_grid)

            current_distance = 0
            sum_output = 0
            is_valid = True

            while grid.houses:
                #random.shuffle(grid.houses)
                #connecting_house = grid.houses.pop()
                connecting_house = grid.pick_random_house(grid.houses)
                sum_output += float(connecting_house.output)
                
                x_house = int(connecting_house.x_coordinate)
                y_house = int(connecting_house.y_coordinate)
            
                #random_bat = random.choice(grid.batteries)
                random_bat = grid.pick_random_bat(grid.batteries)

                x_bat = int(random_bat.x_coordinate)
                y_bat = int(random_bat.y_coordinate)

                teller = 0

                for bat in grid.batteries:
                    if float(connecting_house.output) > float(bat.capacity_left):
                        teller += 1

                if teller == len(grid.batteries):
                    is_valid = False
                    failed_attempts += 1
                    break

                while float(connecting_house.output) > random_bat.capacity_left:
                    random_bat = random.choice(grid.batteries)

                random_bat.capacity_left -= float(connecting_house.output)

                random_bat.houses.append(connecting_house)


                segment_distance = abs(x_bat - x_house) + abs(y_bat - y_house)
                current_distance += segment_distance

            if is_valid:
                grid_distances.append(current_distance)
        
        shortest_dist = grid_distances[0]
        sum_dist = 0

        for dist in grid_distances:
            sum_dist += dist

            if dist < shortest_dist:
                shortest_dist = dist

        avg_dist = sum_dist / len(grid_distances)

        # print output
        print(f"\nThe shortest distance is {shortest_dist}")
        print(f"The average distance is {avg_dist}\n")
        print(f"The amount of failed attempts is {failed_attempts}")
        print(f"The amount of valid attempts is {len(grid_distances)}\n")


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
