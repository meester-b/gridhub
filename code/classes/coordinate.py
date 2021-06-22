class Coordinate():
    """
    
    """
    def __init__(self, x_coordinate, y_coordinate):
        """
        
        """
        self.id = 100 * x_coordinate + y_coordinate
        self.x_coordinate = x_coordinate 
        self.y_coordinate = y_coordinate
        self.batteries = []

        # voor iterative
        self.houses = []

    def __str__(self):
        return f"Coordinate with ({self.x_coordinate},{self.y_coordinate})"
        #  is connected to {self.batteries}"
