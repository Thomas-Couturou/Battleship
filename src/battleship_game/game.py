import pygame
from grid import Grid
from settings import Settings

pygame.init()
pygame.display.set_caption("Bataille navale")
arial_font = pygame.font.SysFont("arial",36)
size = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(size, pygame.SCALED)

screen.fill("white")
pygame.display.flip()

title = arial_font.render("Bataille Navale" , True, "black")
settings = Settings(size[0], size[1], 20, 20)
grid = Grid(settings)

def updateScore(settings):
    arial_font_small = pygame.font.SysFont("arial", 24)
    arial_font_big = pygame.font.SysFont("arial", 30)
    arial_font_big.set_underline(True)
    remainingBoat = arial_font_big.render("Bateaux restants", True, "black")
    screen.blit(remainingBoat, (settings.screenWidth * 0.65,
                          settings.screenHeigth * 0.25))
    cruiser = arial_font_small.render("Croiseurs : {}/{}".format(0,settings.numberCruiser), True, "black")
    screen.blit(cruiser, (settings.screenWidth * 0.65,
                        settings.screenHeigth * 0.3))
    EscortShip = arial_font_small.render("Escorteurs : {}/{}".format(0,settings.numberEscortShip), True, "black")
    screen.blit(EscortShip, (settings.screenWidth * 0.65,
                          settings.screenHeigth * 0.35))
    TorpedoBoat = arial_font_small.render("Torpilleurs : {}/{}".format(0,settings.numberTorpedoBoat), True, "black")
    screen.blit(TorpedoBoat, (settings.screenWidth * 0.65,
                             settings.screenHeigth * 0.4))
    Submarine = arial_font_small.render("Sous-marins : {}/{}".format(0,settings.numberSubmarine), True, "black")
    screen.blit(Submarine, (settings.screenWidth * 0.65,
                             settings.screenHeigth * 0.45))


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
    screen.blit(title, ((settings.screenWidth - title.get_width()) // 2, settings.screenHeigth * 0.05))
    updateScore(settings)
    pygame.display.update()

pygame.quit()
