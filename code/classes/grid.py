# Import csv and random.
import csv
import random

# Import the classes from battery, cable, house and coordinate.
from .battery import *
from .cable import *
from .house import *
from .coordinate import *


from code.classes import cable              ### ONNODIG??

# Dimensions in our grid.
DIMENSION = 51

class Grid():
    """
    This Grid class initializes the Grod object with attributes: a grid with DIMENSION rows and columns.
    The Grid has a list of connected coordinates, coordinates, houses, batteries, a score, a is_valid function
    and paths.
    """
    def __init__(self, infile_house, infile_battery):
        self.rows = DIMENSION
        self.cols = DIMENSION
        self.grid = []
        self.connected_coordinates = []
        self.coordinates = self.add_coordinates()
        self.houses = self.load_houses(infile_house)
        self.batteries = self.load_batteries(infile_battery)
        self.score = 0
        self.is_valid = True
        self.paths = []

        # Create a empty list of lists filled with 0's.
        for i in range(self.rows):
            new_row = []

            # A[pend 0's into every list.
            for i in range(self.cols):
                new_row.append(0)

            self.grid.append(new_row)

        # Place into grid.
        self.add_houses(self.houses)
        self.add_batteries(self.batteries)
    

    
    def output(self):
        """
        district, cost

        per batterij:
        location, capacity, houses
        
        per huis aan batterij:
        location, output, cables

        per kabel:
        list of coordinates of the path
        """
        pass

    def load_houses(self, source_file):     
        """
        Creates House objects and load them into a list of houses from csv.
        """
        
        # Start with an ID of 1 for the first house and create a list of houses.
        id = 1
        houses = []

        # Open the data from the file and read it with csv.
        with open(source_file, 'r') as in_file:           
            reader = csv.reader(in_file)
            next(reader)

            # For every row create a House object and append it to the list of houses.
            for row in reader:
                x = row[0]
                y = row[1]
                cap = row[2]
                house = House(x, y, cap, id)
                houses.append(house)
                id += 1

                # For the Iterative algorithm.
                self.coordinates[DIMENSION * DIMENSION + int(x) - DIMENSION * (int(y) + 1)].houses.append(house)

        # Return the list of houses.
        return houses

    def load_batteries(self, source_file):     
        """
        Creates battery objects and load them into a list of batteries from csv.
        """
        
        # Start with an ID of 1 for the first battery and create a list of batteries.
        id = 1
        batteries = []

        # Open the data from the file and read it with csv.
        with open(source_file, 'r') as in_file:           
            reader = csv.reader(in_file)
            next(reader)
            
            # For every row create a Battery object and append it to the list of batteries.
            for row in reader:
                cap = row[1]
                split = row[0].split(",")
                x = split[0]
                y = split[1]
                battery = Battery(x, y , cap, id)
                batteries.append(battery)
                id += 1

                # ######################################################################################################################
                self.coordinates[DIMENSION * DIMENSION + int(x) - DIMENSION * (int(y) + 1)].batteries.append(battery)
                self.connected_coordinates.append(self.coordinates[DIMENSION * DIMENSION + int(x) - DIMENSION * (int(y) + 1)])

        # Return the list of batteries.
        return batteries

    def add_batteries(self, batteries):
        """
        Function that places batteries in the grid as a 1.
        """
        for battery in batteries:
            x_coordinate = int(battery.x_coordinate)
            y_coordinate = int(battery.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 1

    def add_houses(self, houses):
        """
        Function that places houses in the grid as a 2.
        """
        for house in houses:
            x_coordinate = int(house.x_coordinate)
            y_coordinate = int(house.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 2

    def print_grid(self):
        """
        Function that prints the grid.
        """
        for list in self.grid:
            print(f"{list}\n")

    def pick_random_house(self, list, i):
        """
        Pick a random House from list.
        """
        return list[i]

    def pick_random_bat(self, list):
        """
        Pick a random Battery from list.
        """
        return random.choice(list)

    def shuffle_list(self, list):
        """
        Randomly shuffle a list.
        """        
        random.shuffle(list)
    
    def pick_closest_battery(self, house):
        """
        Picks the closest battery from a given house.
        """
        distances = []
        bats = []

        for battery in self.batteries:
            dist = abs(house.y_coordinate - battery.y_coordinate) + abs(house.x_coordinate - battery.x_coordinate)
            distances.append(dist)
            bats.append(battery)

        return bats[distances.index(min(distances))]

    def lay_cable(self, bat, house):
        """
        Creates a cable between a battery and a house.
        """
        new_cable = cable.Cable(bat, house)
        house.cables.append(new_cable)
        house.bats.append(bat)

        return new_cable

    def bat_available(self, house):
        """
        Checks whether there are batteries available for a house to connect to.
        """
        count = 0

        for bat in self.batteries:
            if house.output > bat.capacity_left:
                count += 1
            
        if count == len(self.batteries):
            return False

        return True

    def connect_house_random_con(self, house, bat):
        """
        Randomly connects a house to a battery within capacity restraints.
        """
        while house.output > bat.capacity_left:
            bat = self.pick_random_bat(self.batteries)

        bat.capacity_left -= house.output
        self.lay_cable(bat, house)

    def reconnect_constraint(self, house, bat):
        """
        Reconnects a house to a different battery than the original, within capacity restraints.
        """
        bat.capacity_left -= house.output
        
        house.bats.clear()
        house.cables.clear()
        
        self.lay_cable(bat, house)

    def calc_dist(self):
        """
        Calculate the total distance of all cables in a grid
        """
        sum = 0

        for house in self.houses:
            for cable in house.cables:
                sum += cable.length

        self.score = sum
    


    ##################
    # Shared cables
    ##################

    def add_coordinates(self):
        """
        Creates Coordinate objects for each coordinate and append them to a list.
        """
        list = []

        for y in range(DIMENSION - 1, -1, -1):
            for x in range(DIMENSION):
                coordinate = Coordinate(x, y)
                list.append(coordinate)
        return list

    def calc_distance(self, point1, point2):
        """
        Calculate the distance between two points on a grid.
        """
        dist = abs(point1.y_coordinate - point2.y_coordinate) + abs(point1.x_coordinate - point2.x_coordinate)
        return dist

    def calc_path(self, point1, point2):
        """
        Calculates the path between two points on the grid.
        """
        path = []
        
        if point1.x_coordinate < point2.x_coordinate:
            for x_step in range(point1.x_coordinate, point2.x_coordinate):
                path.append([x_step, point1.y_coordinate])
        else:
            for x_step in range(point2.x_coordinate, point1.x_coordinate):
                path.append([point1.x_coordinate - x_step + point2.x_coordinate, point1.y_coordinate])

        if point1.y_coordinate < point2.y_coordinate:
            for y_step in range(point1.y_coordinate, point2.y_coordinate + 1):
                path.append([point2.x_coordinate, y_step])
        else:
            for y_step in range(point2.y_coordinate, point1.y_coordinate + 1):
                path.append([point2.x_coordinate, point1.y_coordinate - y_step + point2.y_coordinate])
        
        return path

    def mark_connected(self, coordinate, bat):
        """
        Appends a battery to list of batteries of a coordinate and thus marks as connected.
        """
        coordinate.batteries.append(bat)

    def is_connected(self, coordinate):
        """
        Checks whether a coordinate has batteries and thus is connected.
        """
        if coordinate.batteries:
            return True
        return False

    def connect_power(self, path, bat):
        """
        Lays a path by adding a battery to a coordinate.
        """
        for point in path:
            x = point[0]
            y = point[1]

            if bat not in self.coordinates[DIMENSION * DIMENSION + x - DIMENSION * (y + 1)].batteries:
                self.coordinates[DIMENSION * DIMENSION + x - DIMENSION * (y + 1)].batteries.append(bat)
            self.connected_coordinates.append(self.coordinates[DIMENSION * DIMENSION + x - DIMENSION * (y + 1)])

    def add_path(self, path):
        """
        Adds a path to the list of paths.
        """
        self.paths.append(path)


    def bat_full(self, point, house):
        """
        Checks whether a battery is full.
        """
        if house.output > point.batteries[0].capacity_left:
            return True
        return False
            

    def __str__(self):
        """
        Give the Grid Object a name.
        """
        return f"Grid object"