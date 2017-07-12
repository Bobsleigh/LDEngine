import pygame
import os
import math

from app.settings import *
from ldLib.collision.collisionMask import CollisionMask
from ldLib.collision.collisionTile import collisionWithTile
from app.tools.imageBox import *


class PlayerTest(pygame.sprite.Sprite):
    def __init__(self, x, y, sceneData, max_health=10):
        super().__init__()

        self.name = "player"

        self.imageBase = rectSurface((32, 32), BLUE, 3)
        self.imageBase.set_colorkey(COLORKEY)

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.setShapeImage()
        self.image = self.imageShapeRight

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
        self.maxSpeedy = 5
        self.accx = 2
        self.accy = 2

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

    def setShapeImage(self):
        self.imageShapeLeft = pygame.transform.flip(self.imageBase, True, False)
        self.imageShapeRight = self.imageBase

    def update(self):
        self.capSpeed()

        self.previousX = self.x
        self.previousY = self.y

        self.moveX()
        self.moveY()
        self.rect.x = self.x
        self.rect.y = self.y

        if self.speedx > 0:
            self.image = self.imageShapeRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.image = self.imageShapeLeft
            self.facingSide = LEFT

        self.updateCollisionMask()
        self.updatePressedKeys()

    def moveX(self):
        self.x += self.speedx
        self.collisionMask.rect.x = self.x
        if collisionWithTile(self, SOLID, self.mapData):
            if self.speedx > 0:
                self.x = ((self.x + self.collisionMask.rect.width) // self.mapData.tmxData.tilewidth) * self.mapData.tmxData.tilewidth - self.collisionMask.rect.width
            else:
                self.x = (self.x // self.mapData.tmxData.tilewidth + 1) * self.mapData.tmxData.tilewidth
            self.collisionMask.rect.x = self.x

    def moveY(self):
        self.y += self.speedy
        self.collisionMask.rect.y = self.y
        if collisionWithTile(self, SOLID, self.mapData):
            if self.speedy > 0:
                self.y = ((self.y + self.collisionMask.rect.height) // self.mapData.tmxData.tileheight) * self.mapData.tmxData.tileheight - self.collisionMask.rect.height
            else:
                self.y = (self.y // self.mapData.tmxData.tileheight + 1) * self.mapData.tmxData.tileheight
            self.collisionMask.rect.y = self.y

    def capSpeed(self):
        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedy:
            self.speedy = self.maxSpeedy
        if self.speedy < 0 and self.speedy < -self.maxSpeedy:
            self.speedy = -self.maxSpeedy

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.updateSpeedRight()
                self.rightPressed = True
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.updateSpeedLeft()
                self.leftPressed = True
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.updateSpeedUp()
                self.upPressed = True
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.updateSpeedDown()
                self.downPressed = True
            elif event.key == pygame.K_SPACE:
                #self.nextItem()
                self.spacePressed = True
            elif event.key == pygame.K_LSHIFT:
                self.leftShiftPressed = True
            elif event.key == pygame.K_ESCAPE:
                pass

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.rightPressed = False
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.leftPressed = False
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                self.upPressed = False
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                self.downPressed = False
            elif event.key == pygame.K_LSHIFT:
                self.leftShiftPressed = False
            elif event.key == pygame.K_SPACE:
                self.spacePressed = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == MOUSE_LEFT:
                self.leftMousePressed = True
            elif event.button == MOUSE_RIGHT:
                self.rightMousePressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == MOUSE_LEFT:
                self.leftMousePressed = False
            elif event.button == MOUSE_RIGHT:
                self.rightMousePressed = False

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