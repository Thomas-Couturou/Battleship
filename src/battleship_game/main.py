from boat import Boat
from grid import Grid

grid = Grid()
lstBoat = []

lstBoat.append(Boat(4))
lstBoat.append(Boat(3))
lstBoat.append(Boat(3))
lstBoat.append(Boat(2))
lstBoat.append(Boat(2))
lstBoat.append(Boat(2))
lstBoat.append(Boat(1))
lstBoat.append(Boat(1))
lstBoat.append(Boat(1))
lstBoat.append(Boat(1))

grid.createGridMap(lstBoat)

print(grid.gridMap)