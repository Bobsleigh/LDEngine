__author__ = 'Bobsleigh'

from ldLib.scene.LogicHandler import LogicHandler
from FeatureTests.TileCollisions.TestScenePhysics import TestScenePhysics
from ldLib.collision.collisionNotifySprite import collisionNotifySprite
from app.settings import *

class AnimationDemoLogicHandler(LogicHandler):
    def __init__(self, gameData):
        super().__init__(gameData)
        self.physics = TestScenePhysics(gameData.sceneData)

    def handle(self):
        super().handle()
        self.physics.update()


    def handleCollision(self):
        for sprite in self.gameData.sceneData.allSprites:
            collisionNotifySprite(sprite, SOLID, self.gameData.sceneData)