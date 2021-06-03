import csv

batteries = []

class Battery():
    '''
    Initializes the Battery class
    '''
    def __init__(self, position, capacity, uid):
        self.id = uid
        self.position = position
        self.capacity = capacity
        self.cost = 5000
        self.houses = []
        self.max_capacity = False

        with open('data/district_1/district-1_batteries.csv') as file:           # later route name variabel maken
            reader = csv.reader(file)
            for row in reader:

        #read csv
            #create all battery objects
        #batteries.append(battery)