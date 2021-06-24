# Import matplotlib as plt
from matplotlib import pyplot as plt

def visualise(grid):
    """
    Visualise the grid result we got. 
    """

    # Load visualisations
    print("Loading visualisation...")

    # create figure and enable windows export
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # Create a grid with x and y axes -5 to -55 and every interval of 1 for each x and y
    plt.axis([-5, 55, -5, 55])

    # Name the plot and add lines in the figure
    plt.title('GridHub')
    plt.grid(True)

    # For each battery plot the battery with x and y coordinates
    for battery in grid.batteries:
        x_bat = battery.x_coordinate
        y_bat = battery.y_coordinate

        # plot a green circle
        plt.plot(x_bat, y_bat, 'o', color='green')
    
    # For each house plot the house with x and y coordinates
    for house in grid.houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate

        # plot a red triangle
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

                # plot a blue line
                plt.plot(x_line, y_line, color='blue')
    
    # Show this with matplotlib and inform completion
    plt.savefig("results/not shared/grid.png")
    print("Visualisation loaded")


def visualise_shared(grid):
    """
    Visualise the grid we foud
    """

    # Load visualisations
    print("Loading visualisation...")

    # create figure and enable windows export
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Create a grid with x and y axes -5 to -55 and every interval of 1 for each x and y
    plt.axis([-5, 55, -5, 55])

    # add title and lines in graph
    plt.title('GridHub')
    plt.grid(True)
    
    # For each cable plot each cable segment line.
    for path in grid.paths:
        for i in range(len(path)-1):
            # calculate lines 
            x_begin = path[i][0]
            y_begin = path[i][1]
            x_end = path[i+1][0]
            y_end = path[i+1][1]
            x_line = [x_begin, x_end]
            y_line = [y_begin, y_end]

            # determine coordinate object at begin and end of cable   
            coord1 = grid.coordinates[grid.rows * grid.cols + x_begin - grid.rows * (y_begin + 1)]
            coord2 = grid.coordinates[grid.rows * grid.cols + x_end - grid.rows * (y_end + 1)]

            # Print different colours for cables from each battery.
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
    
    # Print black for shared cables
    if len(coord1.batteries) != 1:
        # If two points have multiple cables, draw a black line
        if len(coord2.batteries) != 1:
            plt.plot(x_line, y_line, color='black')
        # If only a point has multiple cables (cables cross), draw a black dot
        else:
            plt.plot(x_begin, y_begin, '.', color='black')

    # Print red triangles for houses
    for house in grid.houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate
        plt.plot(x_house, y_house, '^', color='red')

    # Print green circles for batteries
    for battery in grid.batteries:
        x_bat = battery.x_coordinate
        y_bat = battery.y_coordinate
        plt.plot(x_bat, y_bat, 'o', color='green')

    # Save cables
    plt.savefig("results/shared cables/grid_shared.png")
    print("Visualisation loaded")
