import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, image, x, y, settings, boat, point):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.settings = settings
        self.boat = boat
        self.isClick = False
        self.point = point

    def update(self, events, reveal):
        if reveal:
            self.onReveal()
        else:
            for event in events:
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.rect.collidepoint(event.pos) and not(self.isClick):
                        self.onClick()
                        self.isClick = True
            if self.boat != None and self.boat.isSunk():
                self.image.fill((255, 0, 0))


    def onClick(self):
        self.settings.numberTurn += 1
        if self.boat == None:
            self.image.fill((0, 0, 255))
            self.settings.message = "Raté !"
        else:
            self.boat.touched(self.point)
            if self.boat.isSunk():
                self.image.fill((255, 0, 0))
                self.settings.message = "Touché ! Coulé !"
                self.settings.sunkenBoat(self.boat)
            else:
                self.image.fill((0, 255, 0))
                self.settings.message = "Touché !"

    def onReveal(self):
        if self.boat == None:
            self.image.fill((0, 0, 255))
        else:
            if self.boat.isSunk():
                self.image.fill((255, 0, 0))
            else:
                self.image.fill((0, 255, 0))
