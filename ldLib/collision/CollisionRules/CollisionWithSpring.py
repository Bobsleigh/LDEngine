__author__ = 'Bobsleigh'

from ldLib.collision.collisionTile import collisionWithTile
from app.settings import *

class CollisionWithSpring:
    def __init__(self):
        pass

    def onMoveX(self, sprite):
        pass

    def onMoveY(self, sprite):
        if collisionWithTile(sprite, SPRING, sprite.mapData):
            print("SPRING")
            if sprite.speedy > 0:
                sprite.speedy = -sprite.springJumpSpeed
#            sprite.collisionMask.rect.y = sprite.y