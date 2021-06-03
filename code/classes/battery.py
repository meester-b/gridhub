import csv

batteries = []

class Battery():
    '''
    Initializes the Battery class
    '''
    def __init__(self, x_coordinate, y_coordinate, capacity, uid):
        self.id = uid
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.capacity = capacity
        self.cost = 5000
        self.houses = []
        self.max_capacity = False

        #read csv
        #create all battery objects
        #batteries.append(battery)
        with open('data/district_1/district-1_batteries.csv') as file:           # later route name variabel maken
            print(file)
            reader = csv.reader(file)
            for row in reader:
                coordinate = row[0].split(",")
                x_coordinate = int(coordinate[0])
                y_coordinate = int(coordinate[1])
                capacity = int(row[1])
                battery = Battery(x_coordinate=x_coordinate, y_coordinate=y_coordinate, capacity=capacity)
                batteries.append(battery)

print(batteries)