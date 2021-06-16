"""
Do not forget to install matplotlib on laptop
pip3 install matplotlib

RUN BY:

"""
#import numpy as np
from matplotlib import pyplot as plt
import csv

# In de juiste mappen gaan
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from code.classes import battery, house, cable, grid

##
def visualise(grid_input):
    """
    Visualise our output
    """
    # 
    print("Loading visualisation...")
    
<<<<<<< HEAD
    #create x and y axes
=======
    # create x and y axes
>>>>>>> 961fd40b9a55beb8260a760eb795ebb7ec12527d
    plt.axis([0, 50, 0, 50])
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    plt.title('GridHub')
    plt.grid(True)

<<<<<<< HEAD
    houses = grid_input.houses
    batteries = grid_input.batteries
    for house in houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate
        plt.plot(x_house, y_house)

    # with open(house_file, 'r') as in_file:           
    #     reader = csv.reader(in_file)
    #     next(reader)
    #     for row in reader:
    #         x = row[0]
    #         y = row[1]
    #         plt.draw(x,y, '^', color='red')

    # with open(bat_file, 'r') as in_file:           
    #     reader = csv.reader(in_file)
    #     next(reader)

    #     for row in reader:
    #         split = row[0].split(",")
    #         x = split[0]
    #         y = split[1]
    #         plt.plot(x,y, 'o', color='green')


=======

    grid = grid_input
    houses = grid.houses
    batteries = grid.batteries
    for house in houses:
        x_house = house.x_coordinate
        y_house = house.y_coordinate
        plt.plot(x_house, y_house, '^', color='red')
    
    plt.show()
>>>>>>> 961fd40b9a55beb8260a760eb795ebb7ec12527d
    ##https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
    ## to plot a 'o' at a point
    #plot(x,y,'o')


<<<<<<< HEAD

    # plt.plot(15,15, '^', color='red')
=======
    
    # 
>>>>>>> 961fd40b9a55beb8260a760eb795ebb7ec12527d
    # plt.plot(15,30, 'o', color='green')
    # plt.plot(18, 19, '^', color='red')
    # plt.plot(40,37, '^', color='red')
    # point1 = [15,15]
    # point2 =[15,30]
    # x_values = [point1[0], point2[0]]
    # y_values = [point1[1], point2[1]]
    # 
    """
    If we have interval info of this list of paths draw lines between them.
    point1 = [1, 2]
    point2 = [3, 4]

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]

    
    """



# if __name__ == "__main__":
#     vis = visualise()
#     print(vis)
