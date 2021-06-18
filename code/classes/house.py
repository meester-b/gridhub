class House():
    """
    This Battery Class initializes the House object with attributes: coordinates, output and cables.
    It also has certain functions and tracks if a House is connected.
    """
    
    def __init__(self, x_coordinate, y_coordinate, output, uid):
        """
        Initializes the House class.
        """
        self.id = uid
        self.x_coordinate = int(x_coordinate)
        self.y_coordinate = int(y_coordinate)
        self.output = float(output)
        self.connected = False
        self.cables = []
        self.bats = []
        self.available_bats = {}
        self.unavailable_bats = {}
        self.bat_options = len(self.available_bats)
        
    def is_connected(self):
        """
        Check if there exists a cable between the house and a battery.
        """
        return self.connected

    def house_coords(self):
        """
        Returns the house coordinates.
        """
        return [self.x_coordinate, self.y_coordinate]

    def add_bat(self, bat):
        """
        Adds a house to a battery.
        """
        self.bats.append(bat)
    
    # def print_house(self):
    #     print(self.x_coordinate)
    #     print(self.y_coordinate)
    #     print(self.cables)

    def better_option(self):
        if min(self.unavailable_bats, key=self.unavailable_bats) < min(self.available_bats, key=self.available_bats):
            return True
        return False
    
    def best_option(self):
        if self.available_bats:
            return min(self.available_bats, key=self.available_bats.get)
        return None

    def __str__(self):
        return f"House {self.id}"