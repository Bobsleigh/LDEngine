import os
import pygame

from app.sprites.enemy.enemy import Enemy
from app.scene.platformScreen.collisionPlayerPlatform import *
# from app.tool.animation import Animation


class Bullet(Enemy):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'Bullet.png'))

        self.name = "bullet"

        self.imageBulletRight = list()
        self.imageBulletRight.append(pygame.image.load(os.path.join('img', 'Bullet.png')))

        self.imageBulletLeft = list()
        self.imageBulletLeft.append(pygame.image.load(os.path.join('img', 'Bullet.png')))

        self.image = self.imageBulletRight[0]

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height/2

        if direction == RIGHT:
            self.speedx = 10
            self.image = self.imageBulletRight[0]
            self.imageBulletList = self.imageBulletRight
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.image = self.imageBulletLeft[0]
            self.imageBulletList = self.imageBulletLeft
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.animation = None

        self.friendly = friendly
        self.isCollisionApplied = True

    def update(self):
        self.rect.x += self.speedx
        if self.animation is not None :
           next(self.animation)
        self.updateCollisionMask()

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y


    # For animation testing by Marie. timer is the number of time between frame.
    def stand_animation(self,frames,timer):
        while True:
            for frame in frames:
                self.image = frame
                for i in range(timer):
                    yield None

    def onCollision(self, collidedWith, sideOfCollision):
        if collidedWith == SOLID or collidedWith == SPIKE or collidedWith == SPRING:
            self.detonate()

    def hitEnemy(self):
        self.detonate()

    def detonate(self):
        self.kill()

class BeerBullet(Bullet):
    def __init__(self, x, y, direction=RIGHT, friendly=True):
        super().__init__(x, y, os.path.join('img', 'biere32x32.png'))

        self.name = "bullet"

        image1 = pygame.image.load(os.path.join('img', 'biere32x32.png'))
        image2 = pygame.image.load(os.path.join('img', 'biere32x32-2.png'))
        image3 = pygame.image.load(os.path.join('img', 'biere32x32-3.png'))
        image4 = pygame.image.load(os.path.join('img', 'biere32x32-4.png'))
        self.frames = [image1,image2,image3,image4]
        self.image = self.frames[0]

        self.animation = self.stand_animation(self.frames,6)

        self.direction = direction

        self.rect = self.image.get_rect()
        self.rect.y = y - self.rect.height / 2

        if direction == RIGHT:
            self.speedx = 10
            self.rect.x = x
        elif direction == LEFT:
            self.speedx = -10
            self.rect.x = x - self.rect.width
        self.speedy = 0

        self.friendly = friendly
