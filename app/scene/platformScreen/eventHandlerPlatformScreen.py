import pygame
from app.tools.functionTools import *


class EventHandlerPlatformScreen():
    def __init__(self, gameData):
        self.menuPause = None
        self.gameData = gameData


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

            for obj in self.gameData.mapData.notifySet:
                obj.notify(event)



