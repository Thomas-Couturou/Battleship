import pygame
from grid import Grid
from settings import Settings

pygame.init()
pygame.display.set_caption("Bataille navale")
arial_font = pygame.font.SysFont("arial",30)

screen = pygame.display.set_mode(pygame.display.get_desktop_sizes()[0], pygame.SCALED)

settings = Settings(pygame.display.get_desktop_sizes()[0][0], pygame.display.get_desktop_sizes()[0][1])

screen.fill("white")
pygame.display.flip()

grid = Grid(settings)

launched = True
while launched:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            launched = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            launched = False

    grid.group.update(events)
    screen.fill((255, 255, 255))
    grid.group.draw(screen)
    pygame.display.update()

pygame.quit()
