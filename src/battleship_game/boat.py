class Boat():
    def __init__(self, length, lstPoints):
        self.length = length
        self.lstPoints = lstPoints
        self.lstTouched = [False for i in range(length)]

    def isSunk(self):
        sunk = True
        for i in self.lstTouched:
            sunk = sunk and i
        return sunk