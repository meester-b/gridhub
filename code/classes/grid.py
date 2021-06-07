from .battery import *
from .cable import *
from .house import *

DIMENSION = 51

class Grid():
    def __init__(self):
        ## heb hier een s achter gezet en constante gebruikt
        self.rows = DIMENSION
        self.cols = DIMENSION
        self.grid = []

        # uncommenten als relative import werkt
        # self.houses = self.load_houses(source_file)
        # self.batteries = self.load_batteries(source_file)

        # loopen door je rijen
        # maak voor elke rij een lijst aan met daarin de y-coordinaten (dus de kolommen)
        # maak een grid aan als lijst van al je rijen

        ## niet zo mooi
        # row = []
        # for i in range(self.cols + 1):
        #     row.append(0)
        #     self.grid.append(row)
        #     row.clear

        # row = []
        ## liever 1 minder ver en dimensie zoals het echt is (51x51)
        # for i in range(self.cols):
        #     ## of i in de toekomst
        #     ## dit is mooier denk ik, kan je list gebruiken voor y en getal voor x
        #     row.append(0)

        for i in range(self.rows):
            new_row = []

            for i in range(self.cols):
                ## of i in de toekomst
                ## dit is mooier denk ik, kan je list gebruiken voor y en getal voor x
                new_row.append(0)

            self.grid.append(new_row)

    # uncomment als relative import werkt 
    def load_houses(self, source_file):     
        """
        Creates batteries from csv
        """

        id = 0
        houses = []

        with open(source_file, 'r') as in_file:           
            # later route name variabel maken
            reader = csv.reader(in_file)
            next(reader)

            for row in reader:
                # print(row)
                # split = row.replace('"', "")
                # split = split.split(",")
                x = row[0]
                y = row[1]
                cap = row[2]
                house = House(x, y, cap, id)
                houses.append(house)
                id += 1

        return houses

    def load_batteries(self, source_file):     
        """
        Creates batteries from csv
        """
        id = 0
        batteries = []

        with open(source_file, 'r') as in_file:           
            # later route name variabel maken
            reader = csv.reader(in_file)
            next(reader)

            for row in reader:
                cap = row[1]
                split = row[0].split(",")
                x = split[0]
                y = split[1]
                battery = Battery(x, y , cap, id)
                batteries.append(battery)
                id += 1

        return batteries
    # tot hier



    ### ik denk dat dit niet nodig is. Dit moet in main en kan "over elkaar heen liggen"
    ### dus verschillende lijsten met elkaar vergelijken ipv ze er echt op plaatsen.

    ## functie die battery objects in de grid plaatst en coordinaten vervangt
    # '''
    def add_batteries(self, batteries):
        for battery in batteries:
            x_coordinate = int(battery.x_coordinate)
            y_coordinate = int(battery.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 1

    ## functie die house objects in de grid plaatst en coordinaten vervangt
    # '''
    def add_houses(self, houses):
        for house in houses:
            x_coordinate = int(house.x_coordinate)
            y_coordinate = int(house.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 2

    ## functie die paths toevoegt op alle coordinaten waar de kabel langskomt en die coordinaten vervangt
    # '''
    def add_cables(self, path):
        for cable in path:
            x_coordinate = int(cable.x_coordinate)
            y_coordinate = int(cable.y_coordinate)
            self.grid[y_coordinate][x_coordinate] = 3


    # '''
    ### tot en met hier







# maak hiervan een 2D-array (dus lijsten in een lijst, default waarde is None/0), eventueel later met hash table
# for i in range(self.row + 1):
#     i = []
#     for col in range(self.col + 1):        # line break toevoegen zodat het een grid wordt
#         i.append(col)
#         coordinate = [row, col, None, None]
#         self.grid.append(coordinate)
# print(self.grid)