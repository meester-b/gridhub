class Cable():
    """
    Cable links two objects. It is always drawn from a House.
    """

    def __init__(self, x_start, y_start, x_end, y_end, uid):
        self.uid = uid
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        # self.length = length
        self.path = []

    # check functies (valid, met een huis verbonden, niet twee batterijen verbonden)
    def add_path(self):
        if self.x_start < self.x_end:
            for x_step in range(self.x_start, self.x_end + 1):
                self.path.append(f"{x_step}, {self.y_start}")
        else:
            for x_step in range(self.x_end, self.x_start + 1):
                self.path.append(f"{self.x_end + x_step}, {self.y_end}")

        self.path.pop()

        if self.y_start < self.y_end:
            for y_step in range(self.y_start, self.y_end + 1):
                self.path.append(f"{self.x_end}, {y_step}")
        else:
            for y_step in range(self.y_end, self.y_start + 1):
                self.path.append(f"{self.x_start}, {self.y_end - y_step}")
        
        return self

    def calc_length(self):
        self.length = abs(self.x_start - self.x_end) + abs(self.y_start - self.y_end)
        return self

if __name__ == "__main__":
    cable = Cable(3,2,2,3,1)
    cable.add_path()
    print(cable.path)
