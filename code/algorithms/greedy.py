import copy
import random

from code.classes import grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

# TODO: run function    

class Greedy():
    def unconstrained_greedy():
        """
        Sums up all minimum distances from houses to batteries, without constraints.
        """

        # to summarize cable lenghts
        min_sum_cables = 0

        # for every house an empty list
        for house in test_grid.houses:
            distances = []

            # calc all distances to batteries from houses and append to list
            for battery in test_grid.batteries:
                dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
                distances.append(dist)

            # look for the shortest distance in list
            shortest_dist = distances[0]

            # look for the shortest distance in list
            for dist in distances:
                if dist < shortest_dist:
                    shortest_dist = dist

            # look for the house that has this distance and append it to battery object
            for bat in test_grid.batteries:
                if shortest_dist == abs(int(house.y_coordinate) - int(bat.y_coordinate)) + abs(int(house.x_coordinate) - int(bat.x_coordinate)):
                    bat.houses.append(house)
            
            # summarize cable lengths
            min_sum_cables += shortest_dist

    def constrained_greedy(tries):
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
        for x in range(tries):
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


