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
        self.capacity_left = False
        self.max_capacity = False

        ## misschien handig? moet leeg zijn
        # self.batteries = []

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