import unittest
from src.main.battleship_game.settings import Settings
from src.main.battleship_game.boat import Boat

class settingsTest(unittest.TestCase):

    def testSunkenBoat(self):
        settings = Settings(10,10)

        settings.lstBoat = []
        boat4 = Boat(4)
        settings.lstBoat.append(boat4)
        self.assertEqual(settings.numberCruiserDestroyed, 0)
        settings.sunkenBoat(boat4)
        self.assertEqual(settings.numberCruiserDestroyed, 1)

        settings.lstBoat = []
        boat3 = Boat(3)
        settings.lstBoat.append(boat3)
        self.assertEqual(settings.numberEscortShipDestroyed, 0)
        settings.sunkenBoat(boat3)
        self.assertEqual(settings.numberEscortShipDestroyed, 1)

        settings.lstBoat = []
        boat2 = Boat(2)
        settings.lstBoat.append(boat2)
        self.assertEqual(settings.numberTorpedoBoatDestroyed, 0)
        settings.sunkenBoat(boat2)
        self.assertEqual(settings.numberTorpedoBoatDestroyed, 1)

        settings.lstBoat = []
        boat1 = Boat(1)
        settings.lstBoat.append(boat1)
        self.assertEqual(settings.numberSubmarineDestroyed, 0)
        settings.sunkenBoat(boat1)
        self.assertEqual(settings.numberSubmarineDestroyed, 1)


    def testCreateLstBoat(self):
        settings = Settings(10,10)
        settings.lstBoat = []
        settings.createLstBoat()
        self.assertEqual(len(settings.lstBoat), settings.numberCruiser + settings.numberEscortShip + settings.numberTorpedoBoat + settings.numberSubmarine)


    def testReset(self):
        settings = Settings(10,10)
        self.numberCruiserDestroyed = 1
        self.numberEscortShipDestroyed = 2
        self.numberTorpedoBoatDestroyed = 3
        self.numberSubmarineDestroyed = 4
        self.numberTurn = 15
        self.message = "Hello"

        settings.reset()
        self.assertEqual(settings.numberCruiserDestroyed, 0)
        self.assertEqual(settings.numberEscortShipDestroyed, 0)
        self.assertEqual(settings.numberTorpedoBoatDestroyed, 0)
        self.assertEqual(settings.numberSubmarineDestroyed, 0)
        self.assertEqual(settings.numberTurn, 0)
        self.assertEqual(settings.message, "")
