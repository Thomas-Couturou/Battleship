import unittest
import pygame
from src.main.battleship_game.settings import Settings
from src.main.battleship_game.cell import Cell
from src.main.battleship_game.point import Point
from src.main.battleship_game.boat import Boat

class cellTest(unittest.TestCase):

    def testOnClick(self):
        settings = Settings(800,600)
        boat = Boat(2)
        boat.lstPoints.append(Point(0,0))
        boat.lstPoints.append(Point(0,1))

        cell = Cell(pygame.Surface((10,10)), 10, 10, settings, None, Point(0,0))
        cell.onClick()
        self.assertEqual(settings.numberTurn, 1)
        self.assertEqual(settings.message, "Raté !")

        cell = Cell(pygame.Surface((10, 10)), 10, 10, settings, boat,Point(0, 0))
        cell.onClick()
        self.assertEqual(settings.numberTurn, 2)
        self.assertEqual(settings.message, "Touché !")

        cell = Cell(pygame.Surface((10, 10)), 10, 10, settings, boat,Point(0, 1))
        cell.onClick()
        self.assertEqual(settings.numberTurn, 3)
        self.assertEqual(settings.message, "Touché ! Coulé !")

