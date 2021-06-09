import copy
import random

from code.classes import grid

district = "1"

test_grid = grid.Grid(f"data/district_{district}/district-{district}_houses.csv", f"data/district_{district}/district-{district}_batteries.csv")

def unconstrained_greedy():
    """
    Sums up all minimum distances from houses to batteries, without constraints.
    """
    min_sum_cables = 0

    for house in test_grid.houses:
        distances = []

        for battery in test_grid.batteries:
            dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
            distances.append(dist)

        shortest_dist = distances[0]

        for dist in distances:
            if dist < shortest_dist:
                shortest_dist = dist

        for bat in test_grid.batteries:
            if shortest_dist == abs(int(house.y_coordinate) - int(bat.y_coordinate)) + abs(int(house.x_coordinate) - int(bat.x_coordinate)):
                bat.houses.append(house)

        min_sum_cables += shortest_dist

    # print(min_sum_cables)

    # for battery in test_grid.batteries:
        # print(battery.houses)
        # print(len(battery.houses))

def constrained_greedy(tries):
    """
    Sums up all minimum distances from houses to batteries, without constraints.
    """
    # min_sum_cables = 0
    failed_attempts = 0
    # sum_cables = 0
    valid_attempts = 0 
    total_dist = 0

    for x in range(tries):
        is_valid = True
        deepcopy = copy.deepcopy(test_grid)
        random.shuffle(deepcopy.houses)
        sum_cables = 0

        for house in deepcopy.houses:
            distances = []
            available_bat = []

            for bat in deepcopy.batteries:
                if float(house.output) < float(bat.capacity_left):
                    available_bat.append(bat)

            # print(len(available_bat))

            if not available_bat:
                is_valid = False
                failed_attempts += 1
                # print("break")
                break

            for battery in available_bat:
                dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
                distances.append(dist)

            shortest_dist = min(distances)
            shortest_index = distances.index(min(distances))

            # shortest_dist = distances[0]
            # shortest_index = 0

            # for i in range(0, len(distances)):
            #     if distances[i] < shortest_dist:
            #         shortest_index = i

            available_bat[shortest_index].houses.append(shortest_dist)
            available_bat[shortest_index].capacity_left -= float(house.output)

            # for bat in available_bat:
            #     if shortest_dist == abs(int(house.y_coordinate) - int(bat.y_coordinate)) + abs(int(house.x_coordinate) - int(bat.x_coordinate)):
            #         bat.houses.append(house)
            #         bat.capacity_left -= float(house.output)

            sum_cables += shortest_dist

        if is_valid:
            valid_attempts +=1 

        if is_valid:
            if valid_attempts == 1:
                min_sum_cables = sum_cables
        
            if sum_cables < min_sum_cables:
                min_sum_cables = sum_cables

            total_dist += sum_cables

            # print(f"\nThe distance is {sum_cables}")

        sum_houses = 0 

        for battery in deepcopy.batteries:
            # print(battery.houses)
            # print(len(battery.houses))
            # print(f"Capacity left: {battery.capacity_left}")
            # print(f"Houses connected: {len(battery.houses)}\n")
            sum_houses += len(battery.houses)
        
        # print(is_valid)
        # print(f"Total houses connected is: {sum_houses}")
        # print("\n")

    print(f"\nThe shortest distance is {min_sum_cables}")
    print(f"The average distance is {total_dist / valid_attempts}\n")
    print(f"The amount of valid attempts is {valid_attempts}")
    print(f"The amount of failed attempts is {failed_attempts}")


