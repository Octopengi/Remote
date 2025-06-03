class Elevator:
    def __init__(self, num):
        self.num = num
        self.floor = 1
        self.direction = "None"
        self.requests = {1: [], 2:[], 3:[], 4:[], 5:[], 6:[]}

class ElevManag:
    def __init__(self):
        self.requests = {1: [], 2:[], 3:[], 4:[], 5:[], 6:[]}
        elevators = []

    def AddRequest(self, floor, direction):
        if direction not in self.requests[floor]:
            self.requests[floor].append(direction)