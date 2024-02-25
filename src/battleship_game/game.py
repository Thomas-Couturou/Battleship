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


settings = Settings(size[0], size[1], 10, 10)


def updateScore(settings):
    arial_font_small = pygame.font.SysFont("arial", 24)
    arial_font_big = pygame.font.SysFont("arial", 30)
    arial_font_big.set_underline(True)

    remainingBoat = arial_font_big.render("Bateaux coulés", True, "black")
    screen.blit(remainingBoat, (settings.screenWidth * 0.65, settings.screenHeigth * 0.25))

    cruiser = arial_font_small.render("Croiseurs : {}/{}".format(settings.numberCruiserDestroyed,settings.numberCruiser), True, "black")
    screen.blit(cruiser, (settings.screenWidth * 0.65, settings.screenHeigth * 0.3))

    EscortShip = arial_font_small.render("Escorteurs : {}/{}".format(settings.numberEscortShipDestroyed,settings.numberEscortShip), True, "black")
    screen.blit(EscortShip, (settings.screenWidth * 0.65, settings.screenHeigth * 0.35))

    TorpedoBoat = arial_font_small.render("Torpilleurs : {}/{}".format(settings.numberTorpedoBoatDestroyed,settings.numberTorpedoBoat), True, "black")
    screen.blit(TorpedoBoat, (settings.screenWidth * 0.65, settings.screenHeigth * 0.4))

    Submarine = arial_font_small.render("Sous-marins : {}/{}".format(settings.numberSubmarineDestroyed,settings.numberSubmarine), True, "black")
    screen.blit(Submarine, (settings.screenWidth * 0.65, settings.screenHeigth * 0.45))

    arial_font_big.set_underline(False)
    turn = arial_font_big.render("Nombre de tours : {}".format(settings.numberTurn), True,"black")
    screen.blit(turn, (settings.screenWidth * 0.65, settings.screenHeigth * 0.55))

def play(settings):
    settings.reset()
    title = arial_font.render("Bataille Navale", True, "black")
    solution = arial_font.render("Solution", True, "black", (200, 200, 200))
    playAgain = arial_font.render("Rejouer", True, "black", (200, 200, 200))
    grid = Grid(settings)
    reveal = False
    play = False

    launched = True
    while launched:
        screen.fill((255, 255, 255))
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                launched = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                launched = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if solution.get_rect(topleft = (settings.screenWidth*0.7,settings.screenHeigth * 0.7)).collidepoint(event.pos) :
                    reveal = True
                elif solution.get_rect(topleft = (settings.screenWidth*0.7,settings.screenHeigth * 0.8)).collidepoint(event.pos) :
                    launched = False
                    play = True

        grid.group.update(events, reveal)
        grid.group.draw(screen)
        message = arial_font.render(settings.message, True, "black")
        screen.blit(message, ((settings.screenWidth - message.get_width()) // 2,settings.screenHeigth * 0.1))
        screen.blit(title, ((settings.screenWidth - title.get_width()) // 2, settings.screenHeigth * 0.05))
        screen.blit(solution, (settings.screenWidth*0.7,settings.screenHeigth * 0.7))
        screen.blit(playAgain,(settings.screenWidth * 0.7, settings.screenHeigth * 0.8))
        updateScore(settings)
        pygame.display.update()

    return play

playAgain = True
while playAgain:
    playAgain = play(settings)

pygame.quit()
