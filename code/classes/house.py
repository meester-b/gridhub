import csv

houses = []

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

        #read csv
            #create all battery objects
        #batteries.append(battery)