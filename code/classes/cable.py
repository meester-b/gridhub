class Cable():
    """
    Cable links two objects. It is always drawn from a House.
    """

    def __init__(self, x_start, y_start, x_end, y_end, uid):
        self.uid = uid
        self.x_start = int(x_start)
        self.x_end = int(x_end)
        self.y_start = int(y_start)
        self.y_end = int(y_end)
        self.path = self.add_path()
        self.length = self.calc_length()

    # check functies (valid, met een huis verbonden, niet twee batterijen verbonden)
    def add_path(self):
        path = []

        if self.x_start < self.x_end:
            for x_step in range(self.x_start, self.x_end):
                path.append([x_step, self.y_start])

            if self.y_start < self.y_end:
                for y_step in range(self.y_start, self.y_end + 1):
                    path.append([self.x_end, y_step])
            else:
                for y_step in range(self.y_end, self.y_start + 1):
                    path.append([self.x_end, self.y_start - y_step + self.y_end])
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
        length = len(self.path)
        return length

if __name__ == "__main__":
    cable = Cable(5,15,0,10,1)
    cable.add_path()
    print(cable.calc_length())
    print(cable.path)
    # list = []

    # for coords in cable.path:
    #     app = coords.split(",")
    #     list.append(app)

    # # print(cable.path.split(","))
    # # print(cable.path[0:5])
    # print(list)
