class Battery():
    '''
    Initializes the Battery class
    '''
    def __init__(self, position, capacity, uid):
        self.id = uid
        self.position = position
        self.capacity = capacity
        self.cost = 5000
        self.connections = {}
        self.max_capacity = False