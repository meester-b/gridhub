# import csv and random
import csv
import random

# import all the battery adn
from .battery import *
from .cable import *
from .house import *
from .coordinate import *


from code.classes import cable

# Dimensions in our grid
DIMENSION = 51

class Grid():
    """
    This Grid Class initializes the Battery object with attributes: a grid with DIMENSION rows and columns.
    Also the list of house and battery objects live here
    """

    def __init__(self, infile_house, infile_battery):
        """
        Initialize the Grid class.
        """
        self.rows = DIMENSION
        self.cols = DIMENSION
        self.grid = []
        self.connected_coordinates = []
        self.houses = self.load_houses(infile_house)
        self.coordinates = self.add_coordinates()
        self.batteries = self.load_batteries(infile_battery)
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
        # self.add_coordinates()
        self.add_houses(self.houses)
        self.add_batteries(self.batteries)
        

    def load_houses(self, source_file):     
        """
        Creates House objects and load them into a list of houses from csv.
        """

        id = 1
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

        id = 1
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

                self.coordinates[int(x) + (51 - int(y)) * 51].batteries.append(battery)
                self.connected_coordinates.append(self.coordinates[int(x) + (51 - int(y)) * 51])

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
        
        random.shuffle(list)

    
    
    def pick_closest_battery(self, house):
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

        """
        while house.output > bat.capacity_left:
            bat = self.pick_random_bat(self.batteries)

        bat.capacity_left -= house.output
        self.lay_cable(bat, house)

    def connect_con(self, bat, house):
        bat.capacity_left -= house.output
        self.lay_cable(bat, house)

    def reconnect_constraint(self, house, bat):
        """

        """
        bat.capacity_left -= house.output
        
        house.bats.clear()
        house.cables.clear()
        
        self.lay_cable(bat, house)

    def calc_dist(self):
        """
        Calculate the total distance 
        """
        sum = 0

        for house in self.houses:
            for cable in house.cables:
                sum += cable.length

        self.score = sum

    def delete_cable(self, bat, house):
        """
        Deletes a cable between a battery and a house.
        """
        
        cable.Cable(bat, house).delete()        # werkt dit zo?

        # access current cable between house and battery
        # delete current cable

    # def connect_house_greedy_con(self, house, bat):
    
    def __str__(self):
        return f"grid object"


    #######################
    # Shared cables
    #######################

    def add_coordinates(self):
        list = []

        for y in range(DIMENSION):
            for x in range(DIMENSION):
                coordinate = Coordinate(x, y)
                list.append(coordinate)

        return list

    def calc_distance(self, point1, point2):
        dist = abs(point1.y_coordinate - point2.y_coordinate) + abs(point1.x_coordinate - point2.x_coordinate)
        return dist

    def calc_path(self, point1, point2):
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
        coordinate.batteries.append(bat)

    def is_connected(self, coordinate):
        if coordinate.batteries:
            return True
        return False

    def connect_power(self, path, bat):
        for point in path:
            # for coordinate in self.coordinates:
            #     if coordinate.id == 100 * point[0] + point[1]:
            #         self.mark_connected(coordinate, bat)
            print(point)
            # print(bat)
            self.coordinates[point[0] + (50 - point[1]) * 51].batteries.append(bat)
            self.connected_coordinates.append(self.coordinates[point[0] + (50 - point[1]) * 51])

            
            

        


