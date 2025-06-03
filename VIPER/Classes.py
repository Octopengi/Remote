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
        direction = direction.lower()

        if len(direction) != 1:
            return
        
        if direction not in self.requests[floor]:
            self.requests[floor].append(direction)

    """def AssignReqs(self):
        for i in self.requests.keys():
            if len(self.requests[i]) != 0:
                for x in self.elevators:
                    if x.direction in """