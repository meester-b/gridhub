class Cable():
    """
    Cable links two objects. It is always drawn from a House.
    """
    def __init__(self, first_item, second_item):
        """
        Initialize the Cable class with a starting point, ending point, a path list and a length.
        """
        
        self.id = uid

        self.x_start = first_item.x_coordinate
        self.y_start = first_item.y_coordinate
        self.x_end = second_item.x_coordinate
        self.y_end = second_item.y_coordinate
        self.path = self.add_path()
        self.length = self.calc_length()

    # check functies (valid, met een huis verbonden, niet twee batterijen verbonden)
    def add_path(self):
        """
        This function returns a list of the grid-segment steps from a battery to a house.
        """
        path = []
        if self.x_start < self.x_end:
            for x_step in range(self.x_start, self.x_end):
                path.append([x_step, self.y_start])
        else:
            for x_step in range(self.x_end, self.x_start):
                path.append([self.x_start - x_step, self.y_start])

        if self.y_start < self.y_end:
            for y_step in range(self.y_start, self.y_end + 1):
                path.append([self.x_end, y_step])
        else:
            for y_step in range(self.y_end, self.y_start + 1):
                path.append([self.x_end, self.y_start - y_step + self.y_end])
            
        return path

    def calc_length(self):
        """
        This function returns the length of the path.
        """
        length = len(self.path)
        return length

# if __name__ == "__main__":
#     #cable = Cable()
#     cable.add_path()
#     print(cable.calc_length())
#     print(cable.path)
#     # list = []

#     # for coords in cable.path:
#     #     app = coords.split(",")
#     #     list.append(app)

#     # # print(cable.path.split(","))
#     # # print(cable.path[0:5])
#     # print(list)
