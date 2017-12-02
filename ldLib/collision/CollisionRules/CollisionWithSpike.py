__author__ = 'Bobsleigh'

from LDEngine.ldLib.collision.collisionTile import collisionWithTile
from LDEngine.ldLib.collision.CollisionRules.CollisionRule import CollisionRule
from LDEngine.app.settings import *

class CollisionWithSpike(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if collisionWithTile(sprite, SPIKE, sprite.mapData):
            sprite.onSpike()

    def onMoveY(self, sprite):
        if collisionWithTile(sprite, SPIKE, sprite.mapData):
            sprite.onSpike()
