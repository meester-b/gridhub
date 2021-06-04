from .battery import Battery
from .house import House

class Cable():
    def __init__(self, x_start, x_end, y_start, y_end, length, uid):
        self.uid = uid
        self.x_start = x_start
        self.x_end = x_end
        self.y_start = y_start
        self.y_end = y_end
        self.length = abs(x_start-x_end) + abs(y_start-y_end)
    
    # check functies (valid, met een huis verbonden, niet twee batterijen verbonden)