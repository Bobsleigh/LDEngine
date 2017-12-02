from LDEngine.ldLib.Sprites.GenericEnemy import GenericEnemy
from LDEngine.ldLib.tools.ImageBox import rectSurface
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpring import CollisionWithSpring
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpike import CollisionWithSpike
from LDEngine.ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState

from LDEngine.app.settings import *

#
# enemy who do "nothing"
#

class EnemyNoob(GenericEnemy):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.name = "EnemyNoob"
        self.type = "Enemy"

        self.color = PURPLE
        self.image = rectSurface((30, 30), self.color, 2)

        self.previousX = self.x
        self.previousY = self.y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 5
        self.maxSpeedyUp = 25
        self.maxSpeedyDown = 10

        self.isFrictionApplied = True
        self.isGravityApplied = True
        self.isCollisionApplied = True

        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly
        self.collisionRules.append(CollisionWithSolid())
        self.collisionRules.append(CollisionWithSpring())
        self.collisionRules.append(CollisionWithSpike())

        self._state = IdleState()

        self.dictProperties = {"Color": self.setColor}

    def update(self):
        super().update()

        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

    def capSpeed(self):
        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedyDown:
            self.speedy = self.maxSpeedyDown
        if self.speedy < 0 and self.speedy < -self.maxSpeedyUp:
            self.speedy = -self.maxSpeedyUp

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        for rule in self.collisionRules:
            rule.onMoveX(self)

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        for rule in self.collisionRules:
            rule.onMoveY(self)

    def setColor(self, color):
        self.color = MAPCOLOR[color]
        self.image = rectSurface((30, 30), self.color, 2)