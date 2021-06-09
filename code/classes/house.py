import csv

class House():
    '''
    Initializes the House class
    '''

    def __init__(self, x_coordinate, y_coordinate, output, uid):
        self.id = uid
        self.x_coordinate = int(x_coordinate)
        self.y_coordinate = int(y_coordinate)
        self.output = output
        self.connected = False
        self.cables = []

    def is_connected(self):
        """
        Check if there exists a cable between the house and a battery.
        """
        return self.connected

    def house_coords(self):
        return [self.x_coordinate, self.y_coordinate]
