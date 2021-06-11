class Battery():
    """
    This Battery Class initializes the Battery object with attributes: coordinates, capacity, cost and if the max is reached.
    It also has certain functions and tracks the cables and houses connected.
    """
    def __init__(self, x_coordinate, y_coordinate, capacity, uid):
        """
        Initializes the Battery class
        """
        self.id = uid
        self.x_coordinate = int(x_coordinate)
        self.y_coordinate = int(y_coordinate)
        self.capacity = capacity
        self.cost = 5000
        self.houses = []
        self.cables = []
        self.capacity_left = 1507
        self.max_capacity = False

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
        self.houses.append(house)

    def bat_coords(self):
        """
        Adds a house to a battery.
        """
        return [self.x_coordinate, self.y_coordinate]

    def add_cable(self, first_item, second_item, uid):
        """
        Adds a cable to a battery.
        """
        