from boat import Boat

class Settings():
    def __init__(self, screenWidth, screenHeigth, gridWidth=10, gridHeight=10,
                 numberCruiser=1, numberEscortShip=2, numberTorpedoBoat=3,
                 numberSubmarine=4):
        self.screenWidth = screenWidth
        self.screenHeigth = screenHeigth
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight

        self.numberCruiser = numberCruiser
        self.numberEscortShip = numberEscortShip
        self.numberTorpedoBoat = numberTorpedoBoat
        self.numberSubmarine = numberSubmarine

        self.numberCruiserDestroyed = 0
        self.numberEscortShipDestroyed = 0
        self.numberTorpedoBoatDestroyed = 0
        self.numberSubmarineDestroyed = 0

        self.numberTurn = 0
        self.lstBoat = []
        self.message = ""

    def sunkenBoat(self, boat):
        if boat.length == 4:
            self.numberCruiserDestroyed += 1
        elif boat.length == 3:
            self.numberEscortShipDestroyed += 1
        elif boat.length == 2:
            self.numberTorpedoBoatDestroyed += 1
        elif boat.length == 1:
            self.numberSubmarineDestroyed += 1

    def createLstBoat(self):
        lstBoat = []
        for i in range(self.numberCruiser):
            lstBoat.append(Boat(4))
        for i in range(self.numberEscortShip):
            lstBoat.append(Boat(3))
        for i in range(self.numberTorpedoBoat):
            lstBoat.append(Boat(2))
        for i in range(self.numberSubmarine):
            lstBoat.append(Boat(1))
        self.lstBoat = lstBoat

    def reset(self):
        self.numberCruiserDestroyed = 0
        self.numberEscortShipDestroyed = 0
        self.numberTorpedoBoatDestroyed = 0
        self.numberSubmarineDestroyed = 0

        self.numberTurn = 0
        self.createLstBoat()
        self.message = ""
