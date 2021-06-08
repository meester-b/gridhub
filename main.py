import random
from code.classes import battery, house, cable, grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    grid_name = "district 1"

    test_grid = grid.Grid("data/district_1/district-1_houses.csv", "data/district_1/district-1_batteries.csv")

    # amount_bat = 0
    # unconnected_houses = test_grid.houses

    # for battery in test_grid.batteries:
    #     amount_house = 0 

    #     for x in range(0, 30):

    for x in range(0,100):
        while test_grid.houses:
            random.shuffle(test_grid.houses)
            connecting_house = test_grid.houses.pop()
        
            random_bat = random.choice(test_grid.batteries)
            random_bat.houses.append(connecting_house)

            # randint = random.randint(0, 150 - amount_house + 30 * amount_bat)
            # connecting_house = unconnected_houses[randint]
            # battery.houses.append(connecting_house)
            # unconnected_houses
            # amount_house += 1

            # amount_bat += 1
        


            # do your stuff with p

        # test_grid.print_grid()

    for bat in test_grid.batteries:
        # print(bat.houses)
        print(len(bat.houses))