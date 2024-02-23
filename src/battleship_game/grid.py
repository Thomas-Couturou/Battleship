from cell import Cell
import pygame

class Grid():
    def __init__(self,settings):
        self.settings = settings
        self.group = pygame.sprite.Group()
        self.cells = self.initGrid()

    def initGrid(self):
        cells = []
        for i in range(self.settings.gridHeight):
            row = []
            for j in range(self.settings.gridWidth):
                cell = Cell(pygame.Surface((100, 100)), 100*i+100, 100*j+100)
                row.append(cell)
                self.group.add(cell)
            cells.append(row)
        return cells