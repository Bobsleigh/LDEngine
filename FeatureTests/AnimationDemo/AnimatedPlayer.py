import os
import pygame

from LDEngine.ldLib.tools.ImageBox import rectSurface
from LDEngine.ldLib.animation.Animation import Animation
from LDEngine.ldLib.collision.collisionMask import CollisionMask
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSolid import CollisionWithSolid
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpring import CollisionWithSpring
from LDEngine.ldLib.collision.CollisionRules.CollisionWithSpike import CollisionWithSpike
from LDEngine.ldLib.collision.CollisionRules.CollisionWithLadder import CollisionWithLadder
from LDEngine.ldLib.collision.CollisionRules.CollisionWithNothing import CollisionWithNothing
from LDEngine.ldLib.Sprites.Player.IdleState import IdleState

from LDEngine.app.settings import *

class AnimatedPlayer(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "player"

        # Code for animation
        self.imageShapeRight = [pygame.image.load(os.path.join('img', 'playerRight.png')),
                                pygame.image.load(os.path.join('img', 'playerRight1.png')),
                                pygame.image.load(os.path.join('img', 'playerRight2.png'))]
        self.imageShapeLeft = [pygame.transform.flip(img, True, False) for img in self.imageShapeRight]

        self.image = self.imageShapeRight[0]

        self.animationLeft = Animation(self.imageShapeLeft, 30, True)
        self.animationRight = Animation(self.imageShapeRight, 30)
        self.animation = self.animationRight

        #End of code for animation

        self.imageTransparent = rectSurface((32, 32), WHITE, 3)
        self.imageTransparent.set_colorkey(COLORKEY)

        self.rect = self.image.get_rect()  # Position centrée du player
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.previousX = x
        self.previousY = y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 5
        self.maxSpeedyUp = 25
        self.maxSpeedyDown = 10
        self.accx = 2
        self.accy = 2
        self.jumpSpeed = 15
        self.springJumpSpeed = 25

        self.isFrictionApplied = True
        self.isGravityApplied = True
        self.isCollisionApplied = True
        self.facingSide = RIGHT
        self.friendly = True

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False
        self.leftShiftPressed = False
        self.spacePressed = False
        self.leftMousePressed = False
        self.rightMousePressed = False

        self.mapData = sceneData
        self.mapData.player = self

        self.isAlive = True

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        self.collisionRules = []
        self.collisionRules.append(CollisionWithNothing())  # Gotta be first in the list to work properly
        self.collisionRules.append(CollisionWithSolid())
        self.collisionRules.append(CollisionWithSpring())
        self.collisionRules.append(CollisionWithSpike())
        self.collisionRules.append(CollisionWithLadder())

        self._state = IdleState()
        # self.nextState = None

    def update(self):
        # Update image with animation
        self.image = self.animation.update()

        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

        # Update animation instead
        if self.speedx > 0:
            self.animation = self.animationRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.animation = self.animationLeft
            self.facingSide = LEFT

        self.updateCollisionMask()
        self.updatePressedKeys()

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

    def capSpeed(self):
        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedyDown:
            self.speedy = self.maxSpeedyDown
        if self.speedy < 0 and self.speedy < -self.maxSpeedyUp:
            self.speedy = -self.maxSpeedyUp

    def updateSpeedRight(self):
        self.speedx += self.accx

    def updateSpeedLeft(self):
        self.speedx -= self.accx

    def updateSpeedUp(self):
        self.speedy -= self.accy

    def updateSpeedDown(self):
        self.speedy += self.accy

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def stop(self):
        self.speedx = 0
        self.speedy = 0

    def dead(self):
        self.isAlive = False

    def onSpike(self):
        self.kill()

    def onCollision(self, collidedWith, sideOfCollision,limit=0):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                #On colle le player sur le mur à droite
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            if sideOfCollision == LEFT:
                self.x = self.previousX
                self.rect.x = self.x
                self.updateCollisionMask()
                self.speedx = 0
                self.rect.left -= (self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle le player sur le mur de gauche
            if sideOfCollision == DOWN:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                #self.speedy = 0
            if sideOfCollision == UP:
                self.y = self.previousY
                self.rect.y = self.y
                self.updateCollisionMask()
                self.speedy = 0

    def notify(self, event):
        self.nextState = self.state.handleInput(self, event)

        # if self.nextState != None:
        #     self.state.exit(self)
        #     self.state = self.nextState
        #     self.state.enter(self)
        #     self.nextState = None

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state.exit(self)
        self._state = value
        self._state.enter(self)


    def updatePressedKeys(self):
        if self.rightPressed:
            self.updateSpeedRight()
        if self.leftPressed:
            self.updateSpeedLeft()
        if self.upPressed:
            self.updateSpeedUp()
        if self.downPressed:
            self.updateSpeedDown()
        if self.leftMousePressed:
            pass
        if self.rightMousePressed:
            pass
        if self.leftShiftPressed:
            pass
        if self.spacePressed:
            pass

    def jump(self):
        self.speedy = -self.jumpSpeed