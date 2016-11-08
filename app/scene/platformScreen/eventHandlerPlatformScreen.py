import pygame
from app.tools.functionTools import *


class EventHandlerPlatformScreen():
    def __init__(self, player):
        self.menuPause = None
        self.player = player

    def eventHandle(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    pass
                    #self.menuPause.mainLoop()
                # elif event.key == pygame.K_ESCAPE:
                #     self.menuPause.mainLoop()
                elif event.key == pygame.K_RIGHT:
                    self.player.updateSpeedRight()
                    self.player.rightPressed = True
                elif event.key == pygame.K_LEFT:
                    self.player.updateSpeedLeft()
                    self.player.leftPressed = True
                elif event.key == pygame.K_UP:
                    self.player.updateSpeedUp()
                elif event.key == pygame.K_DOWN:
                    self.player.updateSpeedDown()
                elif event.key == pygame.K_SPACE:
                    self.player.jump()
                elif event.key == pygame.K_LCTRL:
                    self.player.shootBullet()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.player.rightPressed = False
                elif event.key == pygame.K_LEFT:
                    self.player.leftPressed = False

        self.updatePressedKeys()

    def updatePressedKeys(self):
        if self.player.rightPressed:
            self.player.updateSpeedRight()
        if self.player.leftPressed:
            self.player.updateSpeedLeft()



