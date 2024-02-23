from cell import Cell
import pygame

class Grid():
    def __init__(self,settings):
        self.settings = settings
        self.group = pygame.sprite.Group()
        self.cells = self.initGrid()

    def initGrid(self):
        cells = []
        length = min(0.5*self.settings.screenWidth, 0.7*self.settings.screenHeigth)
        scaleI = length//self.settings.gridHeight
        scaleJ = length//self.settings.gridWidth
        for i in range(self.settings.gridHeight):
            row = []
            for j in range(self.settings.gridWidth):
                cell = Cell(pygame.Surface((scaleI-1, scaleJ-1)), scaleI*i+0.2*self.settings.screenHeigth, scaleJ*j+0.1*self.settings.screenWidth)
                row.append(cell)
                self.group.add(cell)
            cells.append(row)
        return cells
