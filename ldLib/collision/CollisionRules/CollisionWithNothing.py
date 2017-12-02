__author__ = 'Bobsleigh'

from LDEngine.ldLib.collision.collisionTile import collisionExclusivelyWithTile
from LDEngine.app.settings import *
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState
from LDEngine.ldLib.Sprites.Player.JumpState import JumpState
from LDEngine.ldLib.collision.CollisionRules.CollisionRule import CollisionRule

class CollisionWithNothing(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        pass

    def onMoveY(self, sprite):
        if collisionExclusivelyWithTile(sprite, NONE, sprite.mapData):
            if not isinstance(sprite.state, JumpState):
                sprite.state = JumpState()