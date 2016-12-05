
from app.scene.platformScreen.eventHandlerPlatformScreen import EventHandlerPlatformScreen
from app.scene.platformScreen.logicHandlerPlatformScreen import LogicHandlerPlatformScreen
from app.scene.drawer import Drawer
from app.settings import *
from app.sprites.GUI.scoreDisplay import ScoreDisplay
from app.sprites.playerPlatform import PlayerPlatform
from app.scene.musicFactory import MusicFactory

from app.mapData import MapData



class PlatformScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData
        self.nextScene = None

        self.mapData = self.gameData.mapData
        self.player = PlayerPlatform(self.mapData.spawmPointPlayerx, self.mapData.spawmPointPlayery, self.mapData)

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.mapData.notifySet.add(self.player)
        self.camera = self.mapData.camera

        self.eventHandler = EventHandlerPlatformScreen(self.gameData)
        self.logicHandler = LogicHandlerPlatformScreen(self.screen, self.player, self.mapData)
        self.drawer = Drawer()

        # Pour fair afficher un score... en construction!

        # self.score = ScoreDisplay()
        # self.mapData.spritesHUD.add(self.score)


        MusicFactory(PLATFORM_SCREEN, self.mapData.nameMap)


    def mainLoop(self):

        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle()
            self.logicHandler.handle(self.player, self.gameData)
            self.checkNewMap(self.logicHandler.newMapData)
            self.drawer.draw(self.screen, self.mapData.camera, self.mapData.spritesHUD, self.player)

    def checkNewMap(self, newMapData):
        if newMapData is not None:
            # we got to change
            self.sceneRunning = False
            self.nextScene = WORLD_MAP
            self.gameData.typeScene = WORLD_MAP
            self.gameData.mapData = newMapData

    def close(self):
        self.sceneRunning = False

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.gameData.typeScene = TITLE_SCREEN

        self.close()

    def backToWorldMap(self):
        newMapData = MapData('WorldMap', 'StartPointWorld')
        self.checkNewMap(newMapData)
