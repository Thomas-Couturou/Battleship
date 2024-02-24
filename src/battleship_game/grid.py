import random
from point import Point

class Grid():
    def __init__(self):
        self.gridMap = [[0 for i in range(10)] for j in range(10)]

    def checkBoatPlace(self, startRow, endRow, startCol, endCol, boat):

        validPlace = True
        for i in range(startRow, endRow):
            for j in range(startCol, endCol):
                if self.gridMap[i][j] != 0:
                    validPlace = False

        if validPlace:
            for i in range(startRow-1, endRow+1):
                for j in range(startCol-1, endCol+1):
                    if 0 <= i < 10 and 0 <= j < 10:
                        self.gridMap[i][j] = 1

            for i in range(startRow, endRow):
                for j in range(startCol, endCol):
                    self.gridMap[i][j] = 2
                    boat.lstPoints.append(Point(i,j))
        return validPlace


    def getBoatCoordinates(self, row, col, direction, boat):
        startRow, endRow, startCol, endCol = row, row + 1, col, col + 1

        if direction == "left":
            startCol = col - boat.length + 1
        elif direction == "right":
            endCol = col + boat.length
        elif direction == "up":
            startRow = row - boat.length + 1
        elif direction == "down":
            endRow = row + boat.length

        return startRow, endRow, startCol, endCol

    def getRandomDirection(self, row, col, boat):
        possibleDirection = []

        if col - boat.length >= 0:
            possibleDirection.append("left")
        if col + boat.length < 10:
            possibleDirection.append("right")
        if row - boat.length >= 0:
            possibleDirection.append("up")
        if row + boat.length < 10:
            possibleDirection.append("down")

        if possibleDirection == []:
            direction = None
        else :
            direction = random.choice(possibleDirection)
        return direction

    def createGridMap(self, lstBoat):
        random.seed()

        for boat in lstBoat:
            boatPlaced = False
            while not(boatPlaced):
                randomRow = random.randint(0, 9)
                randomCol = random.randint(0, 9)
                direction = self.getRandomDirection(randomRow, randomCol, boat)
                if direction != None:
                    startRow, endRow, startCol, endCol = self.getBoatCoordinates(randomRow, randomCol, direction, boat)
                    boatPlaced = self.checkBoatPlace(startRow, endRow, startCol, endCol,boat)

