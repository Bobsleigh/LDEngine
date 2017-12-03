__author__ = 'Bobsleigh'

from LDEngine.ldLib.collision.collisionTile import collisionExclusivelyWithTile
from LDEngine.ldLib.Sprites.Player.FallingState import FallingState
from LDEngine.ldLib.Sprites.Player.JumpState import JumpState
from LDEngine.ldLib.collision.CollisionRules.CollisionRule import CollisionRule
from LDEngine.app.settings import *

class CollisionWithNothing(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        pass

    def onMoveY(self, sprite):
        if collisionExclusivelyWithTile(sprite, NONE, sprite.mapData):
            if not isinstance(sprite.state, JumpState) and not isinstance(sprite.state, FallingState):
                sprite.state = FallingState()
