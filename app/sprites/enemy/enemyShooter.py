import pygame
import os

from app.sprites.enemy.enemy import Enemy
from app.sprites.bullet import BeerBullet
from app.tools.animation import Animation

from app.settings import *
import random


class EnemyShooter(Enemy):
    def __init__(self, x, y, theMap=None, direction="Right"):
        super().__init__(x, y)

        self.name = "enemyShooter"

        self.imageEnemy = pygame.image.load(os.path.join('img', 'enemybob.png'))

        self.frames = [self.imageEnemy]
        self.animation = Animation(self,self.frames,20)

        self.rect = self.imageEnemy.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speedx = 0
        self.speedy = 0

        self.theMap = theMap

        self.setDirection(direction)

        self.isGravityApplied = True
        self.isCollisionApplied = True

        self.imageIterShoot = random.randint(10,70)
        self.imageWaitNextShoot = 80

        self.dictProperties = {'direction': self.setDirection}

    def setDirection(self, direction):
        if direction is "Right":
            self.direction = "Right"
        else:
            self.direction = "Left"

    def setTheMap(self, theMap):
        self.theMap = theMap

    def update(self):

        self.animation.update(self)
        self.updateCollisionMask()

        self.imageIterShoot += 1
        if self.imageIterShoot > self.imageWaitNextShoot:

            if self.direction == "Right":
                bullet = BeerBullet(self.rect.x + self.rect.width + 1, self.rect.centery, RIGHT, False)
            elif self.direction == "Left":
                bullet = BeerBullet(self.rect.x - 1, self.rect.centery, LEFT, False)

            self.theMap.camera.add(bullet)
            self.theMap.allSprites.add(bullet)
            self.theMap.enemyBullet.add(bullet)

            self.imageIterShoot = 0


        self.rect.x += self.speedx
        if self.speedy < 15:
            self.rect.y += self.speedy


    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def dead(self):
        self.soundDead.play()
        self.kill()

    def onCollision(self, collidedWith, sideOfCollision):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                # On colle la sprite sur le mur à droite
                self.speedx = 0
                self.collisionMask.rect.right += self.mapData.tmxData.tilewidth - (
                self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            elif sideOfCollision == LEFT:
                self.speedx = 0
                self.collisionMask.rect.left -= (
                self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle la sprite sur le mur à gauche
            elif sideOfCollision == DOWN:
                self.speedy = 0

            elif sideOfCollision == UP:
                # Coller le player sur le plafond
                while self.mapData.tmxData.get_tile_gid(
                                (self.collisionMask.rect.left + 1) / self.mapData.tmxData.tilewidth,
                                (self.collisionMask.rect.top) / self.mapData.tmxData.tileheight,
                                COLLISION_LAYER) != SOLID and self.mapData.tmxData.get_tile_gid(
                            self.collisionMask.rect.right / self.mapData.tmxData.tilewidth,
                            (self.collisionMask.rect.top) / self.mapData.tmxData.tileheight, COLLISION_LAYER) != SOLID:
                    self.collisionMask.rect.bottom -= 1
                self.collisionMask.rect.bottom += 1  # Redescendre de 1 pour sortir du plafond
                self.speedy = 0
                if self.jumpState == CLIMBING:
                    self.jumpState = JUMP
                    self.upPressed = False

        if collidedWith == SPIKE:
            self.dead()

        if collidedWith == SPRING:
            if sideOfCollision == DOWN:
                self.spring()
            else:  # On agit comme avec un SOLID
                self.speedx = 0
                # On colle le player sur le mur à droite
                self.collisionMask.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1