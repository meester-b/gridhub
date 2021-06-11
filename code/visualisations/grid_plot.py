"""
Do not forget to install matplotlib on laptop
pip3 install matplotlib

RUN BY:

"""
import numpy as np
from matplotlib import pyplot as plt

# In de juiste mappen gaan
import sys, os
sys.path.insert(0, os.path.abspath('../..'))
from code.classes import battery, house, cable, grid

##
def visualise(grid_input):
    """
    Visualise our output
    """
    houses = grid_input.houses
    batteries = grid_input.batteries
    
    
    
    
    
    
    
    
    plt.axis([0, 50, 0, 50])
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16 ,17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
    plt.title('GridHub')
    plt.grid(True)

    ##https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html
    ## to plot a 'o' at a point
    #plot(x,y,'o')
    plt.plot(15,15, '^', color='red')
    plt.plot(15,30, 'o', color='green')
    plt.plot(18, 19, '^', color='red')
    plt.plot(40,37, '^', color='red')
    point1 = [15,15]
    point2 =[15,30]
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values)
    """
    If we have interval info of this list of paths draw lines between them.
    point1 = [1, 2]
    point2 = [3, 4]

    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]

    
    """
    plt.show()


# if __name__ == "__main__":
#     vis = visualise()
#     print(vis)
