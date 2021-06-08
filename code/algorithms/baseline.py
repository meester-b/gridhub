import random
import copy
from code.classes import battery, house, cable, grid

dist = "1"

test_grid = grid.Grid(f"data/district_{dist}/district-{dist}_houses.csv", f"data/district_{dist}/district-{dist}_batteries.csv")

def baseline():
    shortest_distance = 0
    for x in range(3):
        #print(x)
        available_houses = copy.deepcopy(test_grid.houses)
        current_distance = 0
        while available_houses:
            
            random.shuffle(available_houses)
            connecting_house = available_houses.pop()
            
            x_house = int(connecting_house.x_coordinate)
            y_house = int(connecting_house.y_coordinate)
        
            random_bat = random.choice(test_grid.batteries)

            x_bat = int(random_bat.x_coordinate)
            y_bat = int(random_bat.y_coordinate)

            random_bat.houses.append(connecting_house)

            segment_distance = abs(x_bat - x_house) + abs(y_bat - y_house)
            current_distance += segment_distance

            # print(segment_distance)
        
        # print(f"The current distance is {current_distance}")

        if x == 0:
            shortest_distance = current_distance
        elif current_distance < shortest_distance:
            shortest_distance = current_distance

    print(f"The shortest distance is {shortest_distance}")


# test_grid.print_grid()

#for bat in test_grid.batteries:
    # print(bat.houses)
    # print(len(bat.houses))