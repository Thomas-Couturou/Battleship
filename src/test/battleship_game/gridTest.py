import unittest
from src.main.battleship_game.boat import Boat
from src.main.battleship_game.settings import Settings
from src.main.battleship_game.point import Point
from src.main.battleship_game.grid import Grid

class gridTest(unittest.TestCase):

    def testInitGrid(self):
        settings = Settings(800, 600)
        grid = Grid(settings)
        settings.gridHeight = 2
        settings.gridWidth = 2
        boat = Boat(2)
        settings.lstBoat = []
        settings.lstBoat.append(boat)
        boat.lstPoints.append(Point(0, 0))
        boat.lstPoints.append(Point(0, 1))
        grid.gridMap = [[2, 2], [1, 1]]
        cells = grid.initGrid()

        self.assertEqual(cells[0][0].boat, boat)
        self.assertEqual(cells[0][1].boat, boat)
        self.assertEqual(cells[1][0].boat, None)
        self.assertEqual(cells[1][1].boat, None)

    def testCheckBoatPlace(self):
        settings = Settings(800, 600)
        settings.gridHeight = 3
        settings.gridWidth = 3
        boat = Boat(2)
        settings.lstBoat = []
        settings.lstBoat.append(boat)
        grid = Grid(settings)
        grid.gridMap = [[0 for j in range(settings.gridWidth)] for i in range(settings.gridHeight)]

        checkPlace = grid.checkBoatPlace(0, 1, 0, 2, boat)
        self.assertTrue(checkPlace)

        self.assertEqual(grid.gridMap[0][0], 2)
        self.assertEqual(grid.gridMap[0][1], 2)
        self.assertEqual(grid.gridMap[0][2], 1)
        self.assertEqual(grid.gridMap[1][0], 1)
        self.assertEqual(grid.gridMap[1][1], 1)
        self.assertEqual(grid.gridMap[1][2], 1)
        self.assertEqual(grid.gridMap[2][0], 0)
        self.assertEqual(grid.gridMap[2][1], 0)
        self.assertEqual(grid.gridMap[2][2], 0)

        checkPlace = grid.checkBoatPlace(0, 1, 0, 2, boat)
        self.assertFalse(checkPlace)


    def testGetBoatCoordinates(self):
        settings = Settings(800, 600)
        boat = Boat(2)
        settings.lstBoat = []
        settings.lstBoat.append(boat)
        grid = Grid(settings)
        startRow, endRow, startCol, endCol = grid.getBoatCoordinates(0, 0, "right", boat)
        self.assertEqual((startRow, endRow, startCol, endCol), (0, 1, 0, 2))
        startRow, endRow, startCol, endCol = grid.getBoatCoordinates(0, 1, "left", boat)
        self.assertEqual((startRow, endRow, startCol, endCol), (0, 1, 0, 2))
        startRow, endRow, startCol, endCol = grid.getBoatCoordinates(0, 0, "down", boat)
        self.assertEqual((startRow, endRow, startCol, endCol), (0, 2, 0, 1))
        startRow, endRow, startCol, endCol = grid.getBoatCoordinates(1, 0, "up", boat)
        self.assertEqual((startRow, endRow, startCol, endCol), (0, 2, 0, 1))

    def testGetRandomDirection(self):
        settings = Settings(800, 600)
        settings.gridHeight= 1
        settings.gridWidth = 2
        boat = Boat(2)
        settings.lstBoat = []
        settings.lstBoat.append(boat)
        grid = Grid(settings)

        direction = grid.getRandomDirection(0,0,boat)
        self.assertEqual(direction, "right")
        direction = grid.getRandomDirection(0, 1, boat)
        self.assertEqual(direction, "left")

        settings.gridHeight = 2
        settings.gridWidth = 1
        direction = grid.getRandomDirection(0, 0, boat)
        self.assertEqual(direction, "down")
        direction = grid.getRandomDirection(1, 0, boat)
        self.assertEqual(direction, "up")

        settings.gridHeight = 1
        direction = grid.getRandomDirection(0, 0, boat)
        self.assertEqual(direction, None)


    def testAffectBoatToCell(self):
        settings = Settings(800,600)
        grid = Grid(settings)
        boat = Boat(1)
        point = Point(0,0)
        boat.lstPoints.append(point)
        settings.lstBoat = []
        settings.lstBoat.append(boat)


        boatTest = grid.affectBoatToCell(point)
        self.assertEqual(boat, boatTest)