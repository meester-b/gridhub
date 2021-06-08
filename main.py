from code.classes import battery, house, cable, grid
# from code.visualisations import visualise as vis       
        
if __name__ == "__main__":
    grid_name = "district 1"

    test_grid = grid.Grid("data/district_1/district-1_houses.csv", "data/district_1/district-1_batteries.csv")

    test_grid.print_grid()