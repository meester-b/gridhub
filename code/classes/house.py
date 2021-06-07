import csv

class House():
    '''
    Initializes the House class
    '''

    def __init__(self, x_coordinate, y_coordinate, max_output, uid):
        self.id = uid
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.max_output = max_output
        self.connected = False
        self.cables = []

    def is_connected(self):
        """
        Check if there exists a cable between the house and a battery.
        """
        return self.connected

