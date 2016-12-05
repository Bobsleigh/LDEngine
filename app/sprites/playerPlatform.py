import pygame
import os

from app.settings import *
from app.sprites.bullet import Bullet
from app.sprites.collisionMask import CollisionMask


class PlayerPlatform(pygame.sprite.Sprite):
    def __init__(self, x, y, mapData):
        super().__init__()

        self.name = "player"

        self.imageBase=pygame.image.load(os.path.join('img', 'joueur_droite.png'))

        self.imageShapeLeft = None
        self.imageShapeRight = None

        self.setShapeImage()
        self.image = self.imageShapeRight

        self.imageTransparent = pygame.Surface((1,1))
        self.imageTransparent.set_colorkey(BLACK)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #To dodge rounding problems with rect
        self.x = x
        self.y = y
        self.pastFrameX = x
        self.pastFrameY = y

        self.speedx = 0
        self.speedy = 0
        self.maxSpeedx = 5
        self.maxSpeedyUp = 18
        self.maxSpeedyDown = 15
        self.maxSpeedyUpClimbing = 6
        self.maxSpeedyDownClimbing = 6
        self.accx = 2
        self.accy = 2
        self.jumpSpeed = -13

        self.isPhysicsApplied = True
        self.isCollisionApplied = True
        self.jumpState = JUMP
        self.facingSide = RIGHT

        self.life = 1
        self.lifeMax = 1
        self.lifeMaxCap = 5
        self.isInvincible = False
        self.invincibleFrameCounter = [0,0] #Timer,flashes nb
        self.invincibleTimer = 20 #Must be even number
        self.invincibleNbFlashes = 5

        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False


        self.mapData = mapData

        self.isAlive = True

        #Link your own sounds here
        #self.soundSpring = pygame.mixer.Sound(os.path.join('music_pcm', 'LvlUpFail.wav'))
        #self.soundBullet = pygame.mixer.Sound(os.path.join('music_pcm', 'Gun.wav'))
        #self.soundGetHit = pygame.mixer.Sound(os.path.join('music_pcm', 'brokenGlass.wav'))
        #self.soundSpring.set_volume(1)
        #self.soundBullet.set_volume(.3)
        #self.soundGetHit.set_volume(.3)

        self.collisionMask = CollisionMask(self.rect.x + 3, self.rect.y, self.rect.width-6, self.rect.height)

    def setShapeImage(self):
        self.imageShapeLeft = pygame.transform.flip(self.imageBase, True, False)
        self.imageShapeRight = self.imageBase


    def update(self):
        self.capSpeed()
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.speedx > 0:
            self.image = self.imageShapeRight
            self.facingSide = RIGHT
        if self.speedx < 0:
            self.image = self.imageShapeLeft
            self.facingSide = LEFT

        self.invincibleUpdate()
        self.updateCollisionMask()
        self.updatePressedKeys()
        self.updateJumpState()

    def capSpeed(self):
        if self.jumpState == CLIMBING:
            if self.speedy > 0 and self.speedy > self.maxSpeedyDownClimbing:
                self.speedy = self.maxSpeedyDownClimbing
            if self.speedy < 0 and self.speedy < -self.maxSpeedyUpClimbing:
                self.speedy = -self.maxSpeedyUpClimbing

        if self.speedx > 0 and self.speedx > self.maxSpeedx:
            self.speedx = self.maxSpeedx
        if self.speedx < 0 and self.speedx < -self.maxSpeedx:
            self.speedx = -self.maxSpeedx
        if self.speedy > 0 and self.speedy > self.maxSpeedyDown:
            self.speedy = self.maxSpeedyDown
        if self.speedy < 0 and self.speedy < -self.maxSpeedyUp:
            self.speedy = -self.maxSpeedyUp

    def jump(self):
        if self.jumpState == GROUNDED:
            self.speedy = self.jumpSpeed
            self.jumpState = JUMP

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

    def updateJumpState(self):
        if self.jumpState == CLIMBING:
            self.isGravityApplied = False
            self.isPhysicsApplied = False
        else:
            self.isGravityApplied = True
            self.isPhysicsApplied = True

    def gainLife(self):
        if self.life < self.lifeMax:
            self.life = self.lifeMax

    def gainLifeMax(self):
        if self.lifeMax < self.lifeMaxCap:
            self.lifeMax += 1
            self.life = self.lifeMax
        else:
            self.lifeMax = self.lifeMaxCap
            self.life = self.lifeMax

    def knockedBack(self):
        #Can break collision ATM
        if self.speedx == 0:
            self.speedx = self.maxSpeedx

        self.speedx = (-self.speedx/abs(self.speedx)) * self.maxSpeedx
        self.speedy = (-self.speedy/abs(self.speedx)) * self.maxSpeedx

    def invincibleOnHit(self):
        self.isInvincible = True
        self.invincibleFrameCounter[0] = 1

    def invincibleUpdate(self):
        if self.invincibleFrameCounter[0] > 0 and self.invincibleFrameCounter[1] < self.invincibleNbFlashes:
            self.invincibleFrameCounter[0] += 1
            if self.invincibleFrameCounter[0]== self.invincibleTimer:
                self.invincibleFrameCounter[0] = 1
                self.invincibleFrameCounter[1] +=1

        elif self.invincibleFrameCounter[1] == self.invincibleNbFlashes:
            self.isInvincible = False
            self.invincibleFrameCounter = [0,0]
        self.visualFlash()

    def dead(self):
        self.isAlive = False

    def pickedPowerUpMaxHealth(self):
        self.gainLifeMax()

    def pickedPowerUpHealth(self):
        self.gainLife()

    def visualFlash(self):
        if self.invincibleFrameCounter[0] == 5:
            self.imageShapeLeft = self.imageTransparent
            self.imageShapeRight = self.imageTransparent
            self.image = self.imageTransparent
        elif self.invincibleFrameCounter[0] == 15:
            self.setShapeImage()
            if self.facingSide == RIGHT:
                self.image = self.imageShapeRight
            else:
                self.image = self.imageShapeLeft

    def shootBullet(self):
        if self.facingSide == RIGHT:
            bullet = Bullet(self.rect.x + self.rect.width +1, self.rect.centery, self.facingSide)
        else:
            bullet = Bullet(self.rect.x -1, self.rect.centery, self.facingSide)
        self.mapData.camera.add(bullet)
        self.mapData.allSprites.add(bullet)
        self.mapData.friendlyBullet.add(bullet)

        if TAG_MARIE ==1:
            print(bullet.isCollisionApplied)
        #self.soundBullet.play()

    def spring(self):
        self.jumpState = JUMP
        self.speedy = -self.maxSpeedyUp
        #self.soundSpring.play()

    def onCollision(self, collidedWith, sideOfCollision):
        if collidedWith == SOLID:
            if sideOfCollision == RIGHT:
                #On colle le player sur le mur à droite
                self.speedx = 0
                self.collisionMask.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1
            if sideOfCollision == LEFT:
                self.speedx = 0
                self.collisionMask.rect.left -= (self.collisionMask.rect.left % self.mapData.tmxData.tilewidth)  # On colle le player sur le mur de gauche
            if sideOfCollision == DOWN:
                self.speedy = 0
                if self.jumpState != CLIMBING:
                    self.jumpState = GROUNDED
            if sideOfCollision == UP:
                # Coller le player sur le plafond
                while self.mapData.tmxData.get_tile_gid((self.collisionMask.rect.left + 1) / self.mapData.tmxData.tilewidth,
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
            else: #On agit comme avec un SOLID
                self.speedx = 0
                # On colle le player sur le mur à droite
                self.collisionMask.rect.right += self.mapData.tmxData.tilewidth - (self.collisionMask.rect.right % self.mapData.tmxData.tilewidth) - 1

        if collidedWith == LADDER:
            if sideOfCollision == UP:
                if self.jumpState != CLIMBING:
                    self.jumpState = CLIMBING
                    self.speedx = 0
                    self.speedy = 0

        if collidedWith == NONE:
            if sideOfCollision == DOWN:
                if self.jumpState == GROUNDED:
                    self.jumpState = JUMP

            if sideOfCollision == UP:
                if self.jumpState == CLIMBING:
                    self.jumpState = JUMP
                    self.upPressed = False

    def hurt(self):
        if not self.isInvincible:
            self.invincibleOnHit()
            self.visualFlash()

    def notify(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.updateSpeedRight()
                self.rightPressed = True
            elif event.key == pygame.K_LEFT:
                self.updateSpeedLeft()
                self.leftPressed = True
            elif event.key == pygame.K_UP:
                self.updateSpeedUp()
            elif event.key == pygame.K_DOWN:
                self.updateSpeedDown()
            elif event.key == pygame.K_SPACE:
                self.jump()
            elif event.key == pygame.K_LCTRL:
                self.shootBullet()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.rightPressed = False
            elif event.key == pygame.K_LEFT:
                self.leftPressed = False

    def updatePressedKeys(self):
        if self.rightPressed:
            self.updateSpeedRight()
        if self.leftPressed:
            self.updateSpeedLeft()
        if self.upPressed:
            self.updateSpeedUp()
        if self.downPressed:
            self.updateSpeedDown()
