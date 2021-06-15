import csv
import random

from .battery import *
from .cable import *
from .house import *


from code.classes import cable

# Dimensions in our grid
DIMENSION = 51

class Grid():
    """
    This Grid Class initializes the Battery object with attributes: a grid with DIMENSIONS rows and columns.
    Also the list of house and battery objects live here
    """

    def __init__(self, infile_house, infile_battery):
        """
        Initialize the Grid class.
        """

        self.rows = DIMENSION
        self.cols = DIMENSION
        self.grid = []
        self.houses = self.load_houses(infile_house)
        self.batteries = self.load_batteries(infile_battery)
        self.grid_distances = []
        # grid kent zijn eigen score
        self.score = 0
        self.is_valid = True

        # create a empty list of lists filled with 0's
        for i in range(self.rows):
            new_row = []

            # append 0's into every list
            for i in range(self.cols):
                new_row.append(0)

            self.grid.append(new_row)

        # place into grid
        self.add_houses(self.houses)
        self.add_batteries(self.batteries)

    def load_houses(self, source_file):     
        """
        Creates House objects and load them into a list of houses from csv.
        """

        id = 0
        houses = []

        # Open the data from 
        with open(source_file, 'r') as in_file:           
            reader = csv.reader(in_file)
            next(reader)

            for row in reader:
                x = row[0]
                y = row[1]
                cap = row[2]
                house = House(x, y, cap, id)
                houses.append(house)
                id += 1

        return houses

    def load_batteries(self, source_file):     
        """
        Creates battery objects and load them into a list of batteries from csv.
        """

        id = 0
        batteries = []

        with open(source_file, 'r') as in_file:           
            reader = csv.reader(in_file)
            next(reader)

            for row in reader:
                cap = row[1]
                split = row[0].split(",")
                x = split[0]
                y = split[1]
                battery = Battery(x, y , cap, id)
                batteries.append(battery)
                id += 1

        return batteries

    def add_batteries(self, batteries):
        """
        Functie die battery objects in de grid plaatst en coordinaten vervangt.
        """

        for battery in batteries:
            x_coordinate = int(battery.x_coordinate)
            y_coordinate = int(battery.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 1

    def add_houses(self, houses):
        """
        Functie die house objects in de grid plaatst en coordinaten vervangt.
        """

        for house in houses:
            x_coordinate = int(house.x_coordinate)
            y_coordinate = int(house.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 2

    # def add_cables(self, path):
    #     """
    #     Functie die paths toevoegt op alle coordinaten waar de kabel langskomt en die coordinaten vervangt  ######
    #     """
    #     for cable in path:
    #         location = cable.split(",")
    #         x_coordinate = int(location[0])
    #         y_coordinate = int(location[1])
    #         self.grid[y_coordinate][x_coordinate] = 3

    def print_grid(self):
        """
        Function that prints the grid.
        """

        for list in self.grid:
            print(f"{list}\n")

    def pick_random_house(self, list):
        """
        Pick a random House from list.
        """

        random.shuffle(list)
        return list.pop()

    def pick_random_bat(self, list):
        """
        Pick a random Battery from list.
        """

        random.shuffle(list)
        return list[0]
    
    def lay_cable(self, bat, house):
        """
        Creates a cable between a battery and a house.
        """

        new_cable = cable.Cable(bat, house)
        bat.cables.append(new_cable)

        return new_cable

    def bat_available(self, house):
        count = 0

        for bat in self.batteries:
            if house.output > bat.capacity_left:
                count += 1
            
        if count == len(self.batteries):
            return False

        return True

    def connect_house_con(self, house, bat):
        while house.output > bat.capacity_left:
            bat = self.pick_random_bat(self.batteries)

        bat.capacity_left -= house.output
        bat.add_house(house)
        self.lay_cable(bat, house)

    def calc_dist(self):
        sum = 0

        for bat in self.batteries:
            for cable in bat.cables:
                sum += cable.length

        self.score = sum

    def delete_cable(self, bat, house):
        """
        Deletes a cable between a battery and a house.
        """
        
        cable.Cable(bat, house).delete()        # werkt dit zo?

        # access current cable between house and battery
        # delete current cable
