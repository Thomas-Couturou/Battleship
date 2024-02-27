import unittest
from src.main.battleship_game.boat import Boat
from src.main.battleship_game.game import Game

class gameTest(unittest.TestCase):

    def testcheckGameEnd(self):
        game = Game()

        game.settings.lstBoat = []
        self.assertTrue(game.checkGameEnd())

        game.settings.lstBoat = [Boat(1)]
        self.assertFalse(game.checkGameEnd())
        game.settings.lstBoat[0].lstTouched[0] = True
        self.assertTrue(game.checkGameEnd())