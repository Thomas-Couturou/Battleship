import unittest
from src.main.battleship_game.boat import Boat
from src.main.battleship_game.point import Point

class boatTest(unittest.TestCase):

    def testIsSunk(self):
        boat = Boat(2)
        self.assertFalse(boat.isSunk())

        boat.lstTouched[0] = True
        self.assertFalse(boat.isSunk())

        boat.lstTouched[1] = True
        self.assertTrue(boat.isSunk())

    def testTouched(self):
        boat = Boat(1)
        boat.lstPoints.append(Point(0,0))

        self.assertFalse(boat.lstTouched[0])

        boat.touched(Point(0, 1))
        self.assertFalse(boat.lstTouched[0])

        boat.touched(Point(0,0))
        self.assertTrue(boat.lstTouched[0])


