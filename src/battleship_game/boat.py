class Boat():
    def __init__(self, length):
        self.length = length
        self.lstPoints = []
        self.lstTouched = [False for i in range(length)]

    def isSunk(self):
        sunk = True
        for i in self.lstTouched:
            sunk = sunk and i
        return sunk

    def touched(self, point):
        i = 0
        for testPoint in self.lstPoints:
            if testPoint.x == point.x and testPoint.y == point.y:
                self.lstTouched[i] = True
            i += 1