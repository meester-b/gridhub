# Import matplotlib as plt
from matplotlib import pyplot as plt

def visualise(grid_input):
    """
    Visualise the grid result we got. 
    """
    # Load visualisations
    print("Loading visualisation...")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Create a grid with x and y axes -5 to -55 and every interval of 1 for each x and y
    plt.axis([-5, 55, -5, 55])
    plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
    plt.yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
    plt.title('GridHub')
    plt.grid(True)

    # From our grid_input take the list of houses and batteries
    grid = grid_input
    houses = grid.houses
    batteries = grid.batteries
    
    
    # For each house plot the house with x and y coordinates
    for house in houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate
        plt.plot(x_house, y_house, '^', color='red')


        # For each cable plot each cable segment line
        for cable in house.cables:
            for i in range(len(cable.path)-1): 
                x_begin = cable.path[i][0]
                y_begin = cable.path[i][1]
                x_end = cable.path[i+1][0]
                y_end = cable.path[i+1][1]
                x_line = [x_begin, x_end]
                y_line = [y_begin, y_end]

                plt.plot(x_line, y_line, color='blue')

    # For each battery plot the battery with x and y coordinates
    for battery in batteries:
        x_bat = battery.x_coordinate
        y_bat = battery.y_coordinate
        plt.plot(x_bat, y_bat, 'o', color='green')
    
    # Show this with matplotlib
    plt.savefig(f"results/not shared/grid_{grid.district}.png")
    print("Visualisation loaded")


def visualise_shared(grid_input):
    """
    Visualise the grid we foud
    """
    # Load visualisations
    print("Loading visualisation...")
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Create a grid with x and y axes -5 to -55 and every interval of 1 for each x and y
    plt.axis([-5, 55, -5, 55])
    plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
    plt.yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
    plt.title('GridHub')
    plt.grid(True)

    # From our grid_input take the list of houses and batteries.
    grid = grid_input
    houses = grid.houses
    batteries = grid.batteries
    
    # For each cable plot each cable segment line.
    for path in grid.paths:
        for i in range(len(path)-1): 
            x_begin = path[i][0]
            y_begin = path[i][1]
            x_end = path[i+1][0]
            y_end = path[i+1][1]
            x_line = [x_begin, x_end]
            y_line = [y_begin, y_end]
               
            coord1 = grid.coordinates[grid.rows * grid.cols + x_begin - grid.rows * (y_begin + 1)]
            coord2 = grid.coordinates[grid.rows * grid.cols + x_end - grid.rows * (y_end + 1)]

            # Print different colours for every battery
            if grid.batteries[0] in coord1.batteries and grid.batteries[0] in coord2.batteries:
                plt.plot(x_line, y_line, color='blue')
            elif grid.batteries[1] in coord1.batteries and grid.batteries[1] in coord2.batteries:
                plt.plot(x_line, y_line, color='green')
            elif grid.batteries[2] in coord1.batteries and grid.batteries[2] in coord2.batteries:
                plt.plot(x_line, y_line, color='pink')
            elif grid.batteries[3] in coord1.batteries and grid.batteries[3] in coord2.batteries:
                plt.plot(x_line, y_line, color='yellow')
            elif grid.batteries[4] in coord1.batteries and grid.batteries[4] in coord2.batteries:
                plt.plot(x_line, y_line, color='purple')
    
    if len(coord1.batteries) != 1:
        if len(coord2.batteries) != 1:
            plt.plot(x_line, y_line, color='black')
    else:
        plt.plot(x_begin, y_begin, '.', color='black')

    for house in houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate
        plt.plot(x_house, y_house, '^', color='red')

    for battery in batteries:
        x_bat = battery.x_coordinate
        y_bat = battery.y_coordinate
        plt.plot(x_bat, y_bat, 'o', color='green')

    plt.savefig(f"results/shared cables/grid_shared_{grid.district}.png")
    print("Visualisation loaded")
