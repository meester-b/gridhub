class House():
    """
    This House class initializes the House object with attributes: coordinates, output and cables.
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

        # For iterative algorithm
        self.path = None
    
    def __str__(self):
        """
        String representation
        """

        return f"House {self.id}"
        
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
    
    def best_option(self):
        """
        Returns the key of the closest battery for a house, if any is allowed.
        """

        if self.available_bats:
            return min(self.available_bats, key=self.available_bats.get)

        return None

    