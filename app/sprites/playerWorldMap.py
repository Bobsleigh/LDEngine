__author__ = 'Bobsleigh'

import pygame
import os

from app.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "player"

        self.imageShapeRight = pygame.image.load(os.path.join('img', 'joueur_droite.png'))
        self.imageShapeLeft = pygame.image.load(os.path.join('img', 'joueur_gauche.png'))
        self.image = self.imageShapeRight

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.facingSide = RIGHT

        #Tile Coordinates
        self.tileX = x / TILE_WIDTH
        self.tileY = y / TILE_HEIGHT

        self.isPhysicsApplied = True

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False

        self.repeatKeyCounter = 1
        self.repeatKeyCounterMax = 8

    def update(self):
        self.rect.x = self.tileX * TILE_WIDTH
        self.rect.y = self.tileY * TILE_HEIGHT - self.rect.height

        if self.facingSide == RIGHT:
            self.image = self.imageShapeRight
        if self.facingSide == LEFT:
            self.image = self.imageShapeLeft

    def moveRight(self):
        self.tileX += 1
        self.facingSide = RIGHT

    def moveLeft(self):
        self.tileX -= 1
        self.facingSide = LEFT

    def moveUp(self):
        self.tileY -= 1
        self.facingSide = UP

    def moveDown(self):
        self.tileY += 1
        self.facingSide = DOWN

    def updateSpeedRight(self):
        if self.repeatKeyCounter == 0:
            self.repeatKeyCounter += 1
            self.moveRight()
        elif self.repeatKeyCounter >= self.repeatKeyCounterMax:
            self.repeatKeyCounter = 0
        else:
            self.repeatKeyCounter += 1

    def updateSpeedLeft(self):
        if self.repeatKeyCounter == 0:
            self.repeatKeyCounter += 1
            self.moveLeft()
        elif self.repeatKeyCounter >= self.repeatKeyCounterMax:
            self.repeatKeyCounter = 0
        else:
            self.repeatKeyCounter += 1

    def updateSpeedUp(self):
        if self.repeatKeyCounter == 0:
            self.repeatKeyCounter += 1
            self.moveUp()
        elif self.repeatKeyCounter >= self.repeatKeyCounterMax:
            self.repeatKeyCounter = 0
        else:
            self.repeatKeyCounter += 1

    def updateSpeedDown(self):
        if self.repeatKeyCounter == 0:
            self.repeatKeyCounter += 1
            self.moveDown()
        elif self.repeatKeyCounter >= self.repeatKeyCounterMax:
            self.repeatKeyCounter = 0
        else:
            self.repeatKeyCounter += 1