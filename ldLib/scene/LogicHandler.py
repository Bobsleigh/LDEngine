import pygame

class LogicHandler:
    def __init__(self,gameData):
        self.gameData = gameData
        self.data = gameData.data
        self.nextScene = None

    def handle(self):
        self.data.allSprites.update()
        self.data.spritesHUD.update()
        self.data.spritesBackGround.update()
