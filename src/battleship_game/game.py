import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from grid import Grid
from settings import Settings


class Game():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Bataille navale")
        size = pygame.display.get_desktop_sizes()[0]
        self.screen = pygame.display.set_mode(size, pygame.SCALED)

        self.screen.fill("white")
        pygame.display.flip()
        self.settings = Settings(size[0], size[1], 10, 10)

    def updateScore(self):
        arial_font_small = pygame.font.SysFont("arial", 24)
        arial_font_big = pygame.font.SysFont("arial", 30)
        arial_font_big.set_underline(True)

        remainingBoat = arial_font_big.render("Bateaux coulés", True, "black")
        self.screen.blit(remainingBoat, (self.settings.screenWidth * 0.65, self.settings.screenHeight * 0.25))

        cruiser = arial_font_small.render("Croiseurs (4 cases) : {}/{}".format(self.settings.numberCruiserDestroyed, self.settings.numberCruiser), True, "black")
        self.screen.blit(cruiser, (self.settings.screenWidth * 0.65, self.settings.screenHeight * 0.3))

        escortShip = arial_font_small.render("Escorteurs (3 cases) : {}/{}".format(self.settings.numberEscortShipDestroyed, self.settings.numberEscortShip), True, "black")
        self.screen.blit(escortShip, (self.settings.screenWidth * 0.65, self.settings.screenHeight * 0.35))

        torpedoBoat = arial_font_small.render("Torpilleurs (2 cases) : {}/{}".format(self.settings.numberTorpedoBoatDestroyed, self.settings.numberTorpedoBoat), True, "black")
        self.screen.blit(torpedoBoat, (self.settings.screenWidth * 0.65, self.settings.screenHeight * 0.4))

        submarine = arial_font_small.render("Sous-marins (1 case) : {}/{}".format(self.settings.numberSubmarineDestroyed, self.settings.numberSubmarine), True, "black")
        self.screen.blit(submarine, (self.settings.screenWidth * 0.65, self.settings.screenHeight * 0.45))

        arial_font_big.set_underline(False)
        turn = arial_font_big.render("Nombre de tours : {}".format(self.settings.numberTurn), True, "black")
        self.screen.blit(turn, (self.settings.screenWidth * 0.65, self.settings.screenHeight * 0.55))

    def play(self):
        self.settings.reset()
        arial_font = pygame.font.SysFont("arial", 36)
        title = arial_font.render("Bataille Navale", True, "black")
        solution = arial_font.render("Solution", True, "black", (200, 200, 200))
        playAgain = arial_font.render("Rejouer", True, "black", (200, 200, 200))

        menu = arial_font.render("Options", True, "black", (200, 200, 200))

        grid = Grid(self.settings)
        reveal = False
        play = False
        settingsMenu = False

        launched = True
        while launched:
            self.screen.fill((255, 255, 255))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    launched = False
                    settingsMenu = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if solution.get_rect(topleft=(self.settings.screenWidth*0.7, self.settings.screenHeight * 0.7)).collidepoint(event.pos):
                        reveal = True
                        self.settings.message = "Voici la solution. Vous avez arrêté après {} tours.".format(self.settings.numberTurn)
                    elif playAgain.get_rect(topleft=(self.settings.screenWidth*0.7, self.settings.screenHeight * 0.8)).collidepoint(event.pos):
                        launched = False
                        play = True
                    elif menu.get_rect(topleft=(self.settings.screenWidth*0.05, self.settings.screenHeight * 0.05)).collidepoint(event.pos):
                        launched = False
                        settingsMenu = True
            if self.checkGameEnd():
                reveal = True
                self.settings.message = "Fécilitations, vous avez terminé la grille en {} tours.".format(self.settings.numberTurn)

            grid.group.update(events, reveal)
            grid.group.draw(self.screen)
            message = arial_font.render(self.settings.message, True, "black")
            self.screen.blit(message, ((self.settings.screenWidth - message.get_width()) // 2, self.settings.screenHeight * 0.1))
            self.screen.blit(title, ((self.settings.screenWidth - title.get_width()) // 2, self.settings.screenHeight * 0.05))
            self.screen.blit(menu, (self.settings.screenWidth*0.05, self.settings.screenHeight * 0.05))
            self.screen.blit(solution, (self.settings.screenWidth*0.7, self.settings.screenHeight * 0.7))
            self.screen.blit(playAgain, (self.settings.screenWidth * 0.7, self.settings.screenHeight * 0.8))
            self.updateScore()
            pygame.display.update()

        return play, settingsMenu

    def settingsMenu(self):
        arial_font = pygame.font.SysFont("arial", 36)
        play = False
        settingsMenu = False
        title = arial_font.render("Bataille Navale", True, "black")
        leave = arial_font.render("Quitter le jeu", True, "black", (200, 200, 200))
        backGame = arial_font.render("Retour", True, "black", (200, 200, 200))

        widthChoice = arial_font.render("Largeur", True, "black")
        gridWidthSlider = Slider(self.screen, self.settings.screenWidth // 4, int(self.settings.screenHeight * 0.3), self.settings.screenWidth // 2, 40, min=10, max=30, step=1, initial=self.settings.gridWidth)
        heightChoice = arial_font.render("Hauteur", True, "black")
        gridHeightSlider = Slider(self.screen, self.settings.screenWidth // 4, int(self.settings.screenHeight * 0.5), self.settings.screenWidth // 2, 40, min=10, max=30, step=1, initial=self.settings.gridHeight)

        launched = True
        while launched:
            self.screen.fill((255, 255, 255))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    launched = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    launched = False
                    play = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    if leave.get_rect(topleft=((self.settings.screenWidth - leave.get_width()) // 2, self.settings.screenHeight * 0.9)).collidepoint(event.pos):
                        launched = False
                    if leave.get_rect(topleft=((self.settings.screenWidth - backGame.get_width()) // 2, self.settings.screenHeight * 0.8)).collidepoint(event.pos):
                        launched = False
                        play = True

            self.settings.gridWidth = gridWidthSlider.getValue()
            self.settings.gridHeight = gridHeightSlider.getValue()

            currentWidth = arial_font.render(str(self.settings.gridWidth), True, "black")
            currentHeight = arial_font.render(str(self.settings.gridHeight), True, "black")

            self.screen.blit(widthChoice, ((self.settings.screenWidth - widthChoice.get_width()) // 2, self.settings.screenHeight * 0.2))
            self.screen.blit(heightChoice, ((self.settings.screenWidth - heightChoice.get_width()) // 2, self.settings.screenHeight * 0.4))
            self.screen.blit(currentWidth, (self.settings.screenWidth*0.8, self.settings.screenHeight * 0.3))
            self.screen.blit(currentHeight, (self.settings.screenWidth * 0.8, self.settings.screenHeight * 0.5))
            self.screen.blit(title, ((self.settings.screenWidth - title.get_width()) // 2, self.settings.screenHeight * 0.05))

            self.screen.blit(backGame, ((self.settings.screenWidth - backGame.get_width()) // 2, self.settings.screenHeight * 0.8))
            self.screen.blit(leave, ((self.settings.screenWidth - leave.get_width()) // 2, self.settings.screenHeight * 0.9))

            pygame_widgets.update(events)
            pygame.display.update()

        return play, settingsMenu

    def checkGameEnd(self):
        end = True
        for boat in self.settings.lstBoat:
            end = end and boat.isSunk()
        return end
