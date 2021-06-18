class Cable():
    """
    Cable links two objects. It is always drawn from a House.
    """
    def __init__(self, first_item, second_item):
        """
        Initialize the Cable class with a starting point, ending point, a path list and a length.
        """
        # check functies (valid, met een huis verbonden, niet twee batterijen verbonden)

        self.x_start = first_item.x_coordinate
        self.y_start = first_item.y_coordinate
        self.x_end = second_item.x_coordinate
        self.y_end = second_item.y_coordinate
        self.path = self.add_path()
        self.length = self.calc_length()
    
    def add_path(self):
        """
        This function returns a list of the grid-segment steps from a battery to a house.
        """
        path = []
        if self.x_start < self.x_end:
            for x_step in range(self.x_start, self.x_end):
                path.append([x_step, self.y_start])
            # print(1)
        else:
            # print(range(self.x_end, self.x_start))
            for x_step in range(self.x_end, self.x_start):
                path.append([self.x_start - x_step + self.x_end, self.y_start])
            # print(2)

        if self.y_start < self.y_end:
            for y_step in range(self.y_start, self.y_end + 1):
                path.append([self.x_end, y_step])
            # print(3)
        else:
            for y_step in range(self.y_end, self.y_start + 1):
                path.append([self.x_end, self.y_start - y_step + self.y_end])
            # print(4)
        return path

    def calc_length(self):
        """
        This function returns the length of the path.
        """
        length = len(self.path)
        return length

# class Item():
#         def __init__(self, x, y):
#             self.x_coordinate = x
#             self.y_coordinate = y

# if __name__ == "__main__":
#     item1 = Item(6, 10)
#     item2 = Item(5, 10)
#     cable = Cable(item1, item2)
#     print(cable.path)