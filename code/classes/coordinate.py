class Coordinate():
    """
    Coordinate class initializes the coordinates, which allows for every coordinate on the grid
    to be accessed and checked for batteries.
    It consists of an ID, a x and y coordinated an a list of connected batteries. 
    For the iterative algorithm we also add a list of houses.
    """

    def __init__(self, x_coordinate, y_coordinate):
        """
        Initializes the Coordinate class.
        """

        self.id = 100 * x_coordinate + y_coordinate
        self.x_coordinate = x_coordinate 
        self.y_coordinate = y_coordinate
        self.batteries = []

        # For Iterative Algorithm
        self.houses = []

    def __str__(self):
        """
        Give the Coordinate Object a name.
        """
        
        return f"Coordinate with ({self.x_coordinate},{self.y_coordinate})"
