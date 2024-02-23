import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, image, x, y, settings):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.settings = settings

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.onClick()

    def onClick(self):
        self.image.fill((0,0,255))
        self.settings.numberTurn += 1