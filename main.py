from code.classes import battery, house, cable, grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    grid_name = "district 1"

    test_grid = grid.Grid()

    
    houses = test_grid.load_houses("data/district_1/district-1_houses.csv")
    batteries = test_grid.load_batteries("data/district_1/district-1_batteries.csv")
    # print(batteries)

    # test_grid = test_grid.add_houses(houses)
    test_grid = test_grid.add_batteries(batteries)
    
    
print(test_grid.grid)