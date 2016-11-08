from app.scene.worldMap.eventHandlerWorldMap import EventHandlerWorldMap
from app.scene.worldMap.logicHandlerWorldMap import LogicHandlerWorldMap

from app.scene.drawer import Drawer
from app.settings import *
from app.sprites.playerWorldMap import Player
from app.scene.musicFactory import MusicFactory
from copy import deepcopy
import pygame


class WorldMap:
    def __init__(self, screen, gameData):
        # Écran
        self.screen = screen

        self.gameData = gameData
        self.mapData = self.gameData.mapData
        self.player = Player(self.mapData.spawmPointPlayerx, self.mapData.spawmPointPlayery)

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.camera = self.mapData.camera

        # Handler
        self.eventHandlerWorldMap = EventHandlerWorldMap()
        self.logicHandler = LogicHandlerWorldMap(self.player, self.gameData)
        self.drawer = Drawer()

        self.nextScene = None

        MusicFactory(WORLD_MAP)

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            oldTilePosX = deepcopy(self.player.tileX)
            oldTilePosY = deepcopy(self.player.tileY)
            self.eventHandlerWorldMap.eventHandle(self.player)

            self.logicHandler.handle(self.player, oldTilePosX,oldTilePosY)
            self.checkNewMap(self.logicHandler.newMapData)

            self.drawer.draw(self.screen, self.mapData.camera, self.mapData.spritesHUD, self.player)

        if self.nextScene == None:
            self.nextScene = self.logicHandler.endState


    def checkNewMap(self, newMapData):

        if newMapData is not None:
            # we got to change
            self.sceneRunning = False
            self.nextScene = PLATFORM_SCREEN
            self.gameData.typeScene = PLATFORM_SCREEN
            self.gameData.mapData = newMapData

    def close(self):
        self.sceneRunning = False #To stop game running