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
        with open('data/district_1/district-1_houses.csv') as file:           # later route name variabel maken
            print(file)
            reader = csv.reader(file)
            for row in reader:
                x_coordinate = int(row[0])
                y_coordinate = int(row[1])
                max_output = int(row[2])
                house = House(x_coordinate=x_coordinate, y_coordinate=y_coordinate, max_output=max_output)
                houses.append(house)

print(houses)