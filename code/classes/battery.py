import csv

class Battery():
    '''
    Initializes the Battery class
    '''
    def __init__(self, x_coordinate, y_coordinate, capacity, uid):
        self.id = uid
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity
        self.cost = 5000
        self.houses = []
        self.max_capacity = False

        ## misschien handig? moet leeg zijn
        self.batteries = []


    ## naar graph als relative import werkt
    # def load_batteries(self, source_file):     
    #     """
    #     Creates batteries from csv
    #     """
    #     id = 0
    #     batteries = []

    #     with open(source_file, 'r') as in_file:           
    #         # later route name variabel maken
    #         reader = csv.reader(in_file)

    #         ## dit is wel goed
    #         for row in reader:
    #             split = row.replace('"', "").split(",")
    #             x = split[0]
    #             y = split[1]
    #             cap = split[2]
    #             battery = Battery(x, y, cap, id)
    #             batteries.append(battery)
    #             id += 1

    #     return batteries

    def is_full(self):
        """
        Checks if a battery as at max capacity.
        Or if no new house can be added without breaking capacity
        """
        return self.max_capacity

    def add_house(self, house):
        """
        Adds a house to a battery.
        """

        self.houses.add(house)

        return 