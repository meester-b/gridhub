#from .battery import Battery
#from .house import House

class Grid():
    def __init__(self):
        self.row = 4
        self.col = 4
        self.grid = []

        row1 = [0, 0, 0, 0, 0]
        row2 = [0, house, 0, 0]

        grid = [row1, row2]
        grid[1][1]

        # loopen door je rijen
        # maak voor elke rij een lijst aan met daarin de y-coordinaten (dus de kolommen)
        # maak een grid aan als lijst van al je rijen

        # maak hiervan een 2D-array (dus lijsten in een lijst, default waarde is None/0), eventueel later met hash table
        for i in range(self.row + 1):
            i = []
            for col in range(self.col + 1):        # line break toevoegen zodat het een grid wordt
                i.append(col)
                coordinate = [row, col, None, None]
                self.grid.append(coordinate)
        print(self.grid)

    # functie die battery objects in de grid plaatst en coordinaten vervangt
    '''
    def add_batteries(self, batteries):
        for battery in batteries:
            battery_position = battery.position
            grid.grid[battery.position] = battery
    '''

grid = Grid()
print(grid.grid)