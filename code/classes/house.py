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

    def load_houses(self, source_file):     
        """
        Creates batteries from csv
        """

        id = 0
        houses = []

        with open(source_file, 'r') as in_file:           
            # later route name variabel maken
            reader = csv.reader(in_file)

            for row in reader:
                split = row.replace('"', "").split(",")
                x = split[0]
                y = split[1]
                cap = split[3]
                house = House(x, y, cap, id)
                id += 1
                houses.append(house)

        return houses

    def is_linked(self):
        """
        Marks a house as connected if there exists a cable
        between the house and a battery.
        """
        return self.connected

