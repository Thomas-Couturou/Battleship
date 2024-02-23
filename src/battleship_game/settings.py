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
