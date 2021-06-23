class Cable():
    """
    Cable class links two objects. It is always drawn from a House.
    It cosists of a x and y coordinate start, x and y coordinate end, a path and the length of that path
    """
    def __init__(self, first_item, second_item):
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
        else:
            for x_step in range(self.x_end, self.x_start):
                path.append([self.x_start - x_step + self.x_end, self.y_start])

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

    # def __str__(self):
    #     """
    #     Give the Cable Object a name.
    #     """
    #     return f"{self.path}"
    