import copy
import random

from code.classes import battery, house, cable, grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

# TODO: run function

class Baseline():
    '''
    Baseline algorithm randomly connects houses to batteries. Unconstrained version does not take max capacity into account,
    constrained version does.
    '''
    
    def unconstrained_baseline(tries):
        '''
        Randomly connects houses to batteries.
        '''    

        # loop for a given number of tries to create a new grid
        for x in range(tries):

            grid = copy.deepcopy(test_grid)

            # connected_houses = []

            # loop for each grid through all available houses
            while grid.houses:
                
                # select a random house from the list of houses
                connecting_house = grid.pick_random_house(grid.houses)
                
                # select a random battery from the list of batteries
                random_bat = grid.pick_random_bat(grid.batteries)

                # connect the house to the battery
                random_bat.add_house(connecting_house)

                # create a cable between house and battery
                # new_cable = cable.Cable(connecting_house, random_bat, id)
                # random_bat.cables.append(new_cable)

                grid.lay_cable(random_bat, connecting_house)
                
                
                # add cable length to total grid cable length
                # current_distance += new_cable.length
                

                # make sure the current house can't be connected again
                # connected_houses.append(connecting_house)

            # add total grid cable length to list of all grid cable lengths
            # grid_distances.append(current_distance)
            grid.calc_dist()

        # pick the shortest total distance of all tries 
        # shortest_dist = grid_distances[0]
        # sum_dist = 0

        grid.print_stats()


        # for dist in grid_distances:
        #     sum_dist += dist
        #     if dist < shortest_dist:
        #         shortest_dist = dist

        # calculate average distance
        # avg_dist = sum_dist / len(grid_distances)

        # print output
        # print(f"The shortest distance is {shortest_dist}")
        # print(f"The average distance is {avg_dist}\n")

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