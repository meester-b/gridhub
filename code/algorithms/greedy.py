import copy

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

    for battery in test_grid.batteries:
        # print(battery.houses)
        print(len(battery.houses))

def constrained_greedy(tries):
    """
    Sums up all minimum distances from houses to batteries, without constraints.
    """
    min_sum_cables = 0
    deepcopy = copy.deepcopy(test_grid)
    failed_attempts = 0

    for x in range(tries):
        is_valid = True

        while deepcopy.houses:
            for house in deepcopy.houses:
                distances = []
                teller = 0

                for bat in deepcopy.batteries:
                    if float(house.output) > float(bat.capacity_left):
                        teller += 1

                if teller == len(deepcopy.batteries):
                    # if len(deepcopy_grid.houses) != 0:
                    is_valid = False
                    failed_attempts += 1
                    break

                for battery in deepcopy.batteries:
                    dist = abs(int(house.y_coordinate) - int(battery.y_coordinate)) + abs(int(house.x_coordinate) - int(battery.x_coordinate))
                    distances.append(dist)

                shortest_dist = distances[0]

                for dist in distances:
                    if dist < shortest_dist:
                        shortest_dist = dist

                for bat in deepcopy.batteries:
                    if shortest_dist == abs(int(house.y_coordinate) - int(bat.y_coordinate)) + abs(int(house.x_coordinate) - int(bat.x_coordinate)):
                        bat.houses.append(house)

                min_sum_cables += shortest_dist

            # print(min_sum_cables)

            for battery in deepcopy.batteries:
                # print(battery.houses)
                print(len(battery.houses))

    print(f"\nThe shortest distance is {shortest_dist}")
    print(f"The average distance is {avg_dist}\n")
    print(f"The amount of failed attempts is {failed_attempts}")
    print(f"The amount of passed attempts is {len(current_distances)}\n")


