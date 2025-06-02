class Elevator:
    def __init__(self, num):
        self.num = num
        self.floor = 1
        self.direction = "None"
        self.requests = {}