import random
import copy
import matplotlib.pyplot as plt

from code.classes import battery, house, cable, grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

def unconstrained_baseline(tries):
    current_distances = []

    for x in range(tries):
        deepcopy = copy.deepcopy(test_grid)
        # deepcopy.houses = copy.deepcopy(test_grid.houses)
        current_distance = 0
        id = 0
        connected_houses = []

        while deepcopy.houses:
            random.shuffle(deepcopy.houses)
            connecting_house = deepcopy.houses.pop()
            
            x_house = int(connecting_house.x_coordinate)
            y_house = int(connecting_house.y_coordinate)
        
            random_bat = random.choice(deepcopy.batteries)

            x_bat = int(random_bat.x_coordinate)
            y_bat = int(random_bat.y_coordinate)

            random_bat.houses.append(connecting_house)
            new_cable = cable.Cable(x_house, y_house, x_bat, y_bat, id)
            connecting_house.cables.append(new_cable)

            # segment_distance = abs(x_bat - x_house) + abs(y_bat - y_house)
            # current_distance += segment_distance
            current_distance += new_cable.length

            connected_houses.append(connecting_house)

        current_distances.append(current_distance)
        id += 1

        total_cables = 0

        for house in connected_houses:
            total_cables += 1
            # print(len(house.cables))
            
            # for cables in house.cables:
                # print(cables.path)
        
        # print(total_cables)
        
    
    shortest_dist = current_distances[0]
    sum_dist = 0

    for dist in current_distances:
        sum_dist += dist

        if dist < shortest_dist:
            shortest_dist = dist

    avg_dist = sum_dist / len(current_distances)

    print(f"The shortest distance is {shortest_dist}")
    print(f"The average distance is {avg_dist}\n")

def constrained_baseline(tries):
    current_distances = []
    failed_attempts = 0

    for x in range(tries):
        deepcopy_grid = copy.deepcopy(test_grid)
        current_distance = 0
        sum_output = 0
        is_valid = True

        while deepcopy_grid.houses:
            random.shuffle(deepcopy_grid.houses)
            connecting_house = deepcopy_grid.houses.pop()
            sum_output += float(connecting_house.output)
            
            x_house = int(connecting_house.x_coordinate)
            y_house = int(connecting_house.y_coordinate)
        
            random_bat = random.choice(deepcopy_grid.batteries)

            x_bat = int(random_bat.x_coordinate)
            y_bat = int(random_bat.y_coordinate)

            teller = 0

            for bat in deepcopy_grid.batteries:
                if float(connecting_house.output) > float(bat.capacity_left):
                    teller += 1

            if teller == len(deepcopy_grid.batteries):
                is_valid = False
                failed_attempts += 1
                break

            while float(connecting_house.output) > random_bat.capacity_left:
                random_bat = random.choice(deepcopy_grid.batteries)

            random_bat.capacity_left -= float(connecting_house.output)

            random_bat.houses.append(connecting_house)


            segment_distance = abs(x_bat - x_house) + abs(y_bat - y_house)
            current_distance += segment_distance

            # for bat in deepcopy_grid.batteries:
            #     print(bat.capacity_left)

            # print(f"\n")
            # print(len(deepcopy_grid.houses))
        print(x)
        if is_valid:
            current_distances.append(current_distance)

        # print(len(deepcopy_grid.houses))
        # print(f"This tries' distance is {current_distance}\n")



    
    shortest_dist = current_distances[0]
    sum_dist = 0

    for dist in current_distances:
        sum_dist += dist

        if dist < shortest_dist:
            shortest_dist = dist

    avg_dist = sum_dist / len(current_distances)

        
    # print(f"Sum of output is {sum_output}\n")
    
    print(f"\nThe shortest distance is {shortest_dist}")
    print(f"The average distance is {avg_dist}\n")
    print(f"The amount of failed attempts is {failed_attempts}")
    print(f"The amount of passed attempts is {len(current_distances)}\n")
    # print(f"The list of valid outcomes of the length of the cables is {current_distances}")
  