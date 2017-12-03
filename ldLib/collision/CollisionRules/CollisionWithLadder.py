__author__ = 'Bobsleigh'

from LDEngine.ldLib.collision.collisionTile import collisionCenterWithTile
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState
from LDEngine.ldLib.Sprites.Player.ClimbingState import ClimbingState
from LDEngine.ldLib.collision.CollisionRules.CollisionRule import CollisionRule
from LDEngine.app.settings import *

class CollisionWithLadder(CollisionRule):
    def __init__(self):
        super().__init__()

    def onMoveX(self, sprite):
        if collisionCenterWithTile(sprite, LADDER, sprite.mapData):
            if not isinstance(sprite.state, ClimbingState):
                sprite.state = ClimbingState()
        else:
            if isinstance(sprite.state, ClimbingState):
                sprite.state = IdleState()

    def onMoveY(self, sprite):
        pass