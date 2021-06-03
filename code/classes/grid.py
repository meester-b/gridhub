#from .battery import Battery, batteries
#from .house import House, houses

class Grid():
    def __init__(self):
        self.row = 4
        self.col = 4
        self.grid = []

        # loopen door je rijen
        # maak voor elke rij een lijst aan met daarin de y-coordinaten (dus de kolommen)
        # maak een grid aan als lijst van al je rijen
        row = []
        for i in range(self.col + 1):
            row.append(0)
            self.grid.append(row)
            row.clear

    # functie die battery objects in de grid plaatst en coordinaten vervangt
    '''
    def add_batteries(self, batteries):
        for battery in batteries:
            x_coordinate = battery.x_coordinate - 1
            y_coordinate = battery.y_coordinate - 1
            self.grid[x_coordinate][y_coordinate] = battery
    '''

    # functie die house objects in de grid plaatst en coordinaten vervangt
    '''
    def add_houses(self, houses):
        for house in houses:
            x_coordinate = house.x_coordinate - 1
            y_coordinate = house.y_coordinate - 1
            self.grid[x_coordinate][y_coordinate] = house
    '''

grid = Grid()
print(grid.grid)






# maak hiervan een 2D-array (dus lijsten in een lijst, default waarde is None/0), eventueel later met hash table
# for i in range(self.row + 1):
#     i = []
#     for col in range(self.col + 1):        # line break toevoegen zodat het een grid wordt
#         i.append(col)
#         coordinate = [row, col, None, None]
#         self.grid.append(coordinate)
# print(self.grid)