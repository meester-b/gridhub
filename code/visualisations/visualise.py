"""
Do not forget to install matplotlib on laptop
pip3 install matplotlib

"""
# import matplotlib
from matplotlib import pyplot as plt

# In de juiste mappen gaan
import sys, os
import numpy as np


sys.path.insert(0, os.path.abspath('../..'))
from code.classes import battery, house, cable, grid


def visualise(grid_input):
    """
    Visualise the grid we foud
    """
    # load visualisations
    print("Loading visualisation...")
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # create a grid with x and y axes -5 to -55 and every interval of 1 for each x and y
    plt.axis([-5, 55, -5, 55])
    plt.xticks = np.arange(-5, 55)
    plt.yticks = np.arange(-5, 55)
    # plt.xticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    # 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
    # plt.yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    # 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55])
    plt.title('GridHub')
    plt.grid(True)

    # from our grid_input take the list of houses and batteries
    grid = grid_input
    houses = grid.houses
    batteries = grid.batteries
    
    #rid.houses[12].print_house()
    # for cable in grid.houses[12].cables:
    #     print(cable.path)

    
    # for each house plot the house with x and y coordinates
    for house in houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate
        plt.plot(x_house, y_house, '^', color='red')


        # for each cable plot each cable segment line
        for cable in house.cables:
            for i in range(len(cable.path)-1): 
                x_begin = cable.path[i][0]
                y_begin = cable.path[i][1]
                x_end = cable.path[i+1][0]
                y_end = cable.path[i+1][1]
                x_line = [x_begin, x_end]
                y_line = [y_begin, y_end]
                plt.plot(x_line, y_line, color='blue')


                
                # if (x_begin == 38) & (y_begin == 12):
                #     plt.plot(x_line, y_line, color='blue')
                # elif (x_begin == 43) & (y_begin == 13):
                #     plt.plot(x_line, y_line, color='yellow')
                # elif (x_begin == 42) & (y_begin == 3):
                #     plt.plot(x_line, y_line, color='green')
                # elif (x_begin == 49) & (y_begin == 23):
                #     plt.plot(x_line, y_line, color='red')
                # elif (x_begin == 3) & (y_begin == 45):
                #     plt.plot(x_line, y_line, color='purple')
                # if i%2 == 0:
                #     plt.plot(x_line, y_line, color='blue')
                # else:
                #     plt.plot(x_line, y_line, color='yellow')


    # for each battery plot the battery with x and y coordinates
    for battery in batteries:
        x_bat = battery.x_coordinate
        y_bat = battery.y_coordinate
        plt.plot(x_bat, y_bat, 'o', color='green')
    
    # show this with matplotlib
    ax.set_aspect('equal', adjustable='box')
    # plt.show()
    plt.savefig("grid.png")
