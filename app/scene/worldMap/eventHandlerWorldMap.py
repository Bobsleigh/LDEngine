import pygame
from app.tools.functionTools import *

class EventHandlerWorldMap():
    def __init__(self):
        self.menuPause = None

    def eventHandle(self,player):
        self.updatePressedKeys(player)

        for dummyEv in pygame.event.get():
            if dummyEv.type == pygame.QUIT:
                quitGame()

            elif dummyEv.type == pygame.KEYDOWN:
                if dummyEv.key == pygame.K_BACKSPACE:
                    pass
                    # self.menuPause.mainLoop()
                # elif dummyEv.key == pygame.K_ESCAPE:
                #     self.menuPause.mainLoop()
                elif dummyEv.key == pygame.K_RIGHT: #Does nothing for now...
                    player.rightPressed = True
                    player.moveRight()
                elif dummyEv.key == pygame.K_LEFT: #Does nothing for now...
                    player.leftPressed = True
                    player.moveLeft()
                elif dummyEv.key == pygame.K_UP:
                    player.upPressed = True
                    player.moveUp()
                elif dummyEv.key == pygame.K_DOWN:
                    player.downPressed = True
                    player.moveDown()
                elif dummyEv.key == pygame.K_SPACE:
                    pass
                elif dummyEv.key == pygame.K_RETURN:
                    pass

            elif dummyEv.type == pygame.KEYUP:
                if dummyEv.key == pygame.K_RIGHT:
                    player.rightPressed = False
                    player.repeatKeyCounter = 1
                elif dummyEv.key == pygame.K_LEFT:
                    player.leftPressed = False
                    player.repeatKeyCounter = 1
                elif dummyEv.key == pygame.K_UP:
                    player.upPressed = False
                    player.repeatKeyCounter = 1
                elif dummyEv.key == pygame.K_DOWN:
                    player.downPressed = False
                    player.repeatKeyCounter = 1

    def updatePressedKeys(self, player):
        if player.rightPressed:
            player.updateSpeedRight()
        if player.leftPressed:
            player.updateSpeedLeft()
        if player.upPressed:
            player.updateSpeedUp()
        if player.downPressed:
            player.updateSpeedDown()
