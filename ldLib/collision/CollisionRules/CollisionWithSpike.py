__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from app.settings import *

class CollisionWithSpike:
    def __init__(self):
        pass

    def onMoveX(self, sprite):
        if collisionWithTile(sprite, SPIKE, sprite.mapData):
            sprite.onSpike()

    def onMoveY(self, sprite):
        if collisionWithTile(sprite, SPIKE, sprite.mapData):
            sprite.onSpike()
