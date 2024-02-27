import pygame
from src.main.battleship_game.game import Game

game = Game()
playAgain = True
settingsMenu = False
while playAgain or settingsMenu:
    if playAgain:
        playAgain,settingsMenu = game.play()
    else:
        playAgain, settingsMenu = game.settingsMenu()

pygame.quit()
