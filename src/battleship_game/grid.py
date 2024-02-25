from cell import Cell
import pygame
import random
from point import Point

class Grid():
    def __init__(self,settings):
        self.settings = settings
        self.group = pygame.sprite.Group()
        self.gridMap = [[0 for j in range(self.settings.gridWidth)] for i in range(self.settings.gridHeight)]
        self.createGridMap()
        self.cells = self.initGrid()

    def initGrid(self):
        cells = []
        maxGrid = max(self.settings.gridWidth,self.settings.gridHeight)
        length = min(0.5*self.settings.screenWidth//maxGrid, 0.7*self.settings.screenHeigth//maxGrid)
        scaleI = length
        scaleJ = length
        for i in range(self.settings.gridHeight):
            row = []
            for j in range(self.settings.gridWidth):
                boat = self.affectBoatToCell(Point(i,j))
                cell = Cell(pygame.Surface((scaleI-1, scaleJ-1)), scaleI*i+0.2*self.settings.screenHeigth, scaleJ*j+0.1*self.settings.screenWidth, self.settings, boat, Point(i,j))
                row.append(cell)
                self.group.add(cell)
            cells.append(row)
        return cells

    def checkBoatPlace(self, startRow, endRow, startCol, endCol, boat):
        validPlace = True
        for i in range(startRow, endRow):
            for j in range(startCol, endCol):
                if self.gridMap[i][j] != 0:
                    validPlace = False

        if validPlace:
            for i in range(startRow-1, endRow+1):
                for j in range(startCol-1, endCol+1):
                    if 0 <= i < self.settings.gridHeight and 0 <= j < self.settings.gridWidth:
                        self.gridMap[i][j] = 1

            for i in range(startRow, endRow):
                for j in range(startCol, endCol):
                    self.gridMap[i][j] = 2
                    boat.lstPoints.append(Point(i,j))
        return validPlace


    def getBoatCoordinates(self, row, col, direction, boat):
        startRow, endRow, startCol, endCol = row, row+1, col, col+1

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
        if col + boat.length < self.settings.gridWidth:
            possibleDirection.append("right")
        if row - boat.length >= 0:
            possibleDirection.append("up")
        if row + boat.length < self.settings.gridHeight:
            possibleDirection.append("down")

        if possibleDirection == []:
            direction = None
        else :
            direction = random.choice(possibleDirection)
        return direction

    def createGridMap(self):
        random.seed()

        self.gridMap = [[0 for j in range(self.settings.gridWidth)] for i in range(self.settings.gridHeight)]

        for boat in self.settings.lstBoat:
            boatPlaced = False
            while not(boatPlaced):
                randomRow = random.randint(0, self.settings.gridHeight-1)
                randomCol = random.randint(0, self.settings.gridWidth-1)
                direction = self.getRandomDirection(randomRow, randomCol, boat)
                if direction != None:
                    startRow, endRow, startCol, endCol = self.getBoatCoordinates(randomRow, randomCol, direction, boat)
                    boatPlaced = self.checkBoatPlace(startRow, endRow, startCol, endCol,boat)

    def affectBoatToCell(self, point):
        boat = None
        for testBoat in self.settings.lstBoat:
            for testPoint in testBoat.lstPoints:
                if testPoint.x == point.x and testPoint.y == point.y:
                    boat = testBoat
        return boat