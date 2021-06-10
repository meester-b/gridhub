import random
from .battery import *
from .cable import *
from .house import *

DIMENSION = 51

class Grid():
    def __init__(self, infile_house, infile_battery):
        self.rows = DIMENSION
        self.cols = DIMENSION
        self.grid = []
        self.houses = self.load_houses(infile_house)
        self.batteries = self.load_batteries(infile_battery)

        # list of lists maken voor coordinaten, overal nullen
        for i in range(self.rows):
            new_row = []

            for i in range(self.cols):
                new_row.append(0)

            self.grid.append(new_row)

        self.add_houses(self.houses)
        self.add_batteries(self.batteries)

    def load_houses(self, source_file):     
        """
        Creates batteries from csv
        """

        id = 0
        houses = []

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
        Creates batteries from csv
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

    ## functie die battery objects in de grid plaatst en coordinaten vervangt
    def add_batteries(self, batteries):
        """

        """
        for battery in batteries:
            x_coordinate = int(battery.x_coordinate)
            y_coordinate = int(battery.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 1

    ## functie die house objects in de grid plaatst en coordinaten vervangt
    def add_houses(self, houses):
        """

        """
        for house in houses:
            x_coordinate = int(house.x_coordinate)
            y_coordinate = int(house.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 2

    ## functie die paths toevoegt op alle coordinaten waar de kabel langskomt en die coordinaten vervangt
    def add_cables(self, path):
        """

        """
        for cable in path:
            location = cable.split(",")
            x_coordinate = int(location[0])
            y_coordinate = int(location[1])
            self.grid[y_coordinate][x_coordinate] = 3

    def print_grid(self):
        """
        
        """
        for list in self.grid:
            print(f"{list}\n")


    def pick_random_house(self, list):
        """

        """
        random.shuffle(list)
        return list.pop()

    def pick_random_bat(self, list):
        """

        """
        random.shuffle(list)
        return list[0]