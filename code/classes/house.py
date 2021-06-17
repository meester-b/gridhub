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
        self.bat_options = 5

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

    def add_house(self, bat):
        """
        Adds a house to a battery.
        """
        self.bats.append(bat)