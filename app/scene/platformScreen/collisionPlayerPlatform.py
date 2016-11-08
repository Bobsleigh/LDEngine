from app.settings import *
from app.tools.circle import Circle
import pygame

class CollisionPlayerPlatform:
    def __init__(self, player, map):
        # self.soundControl = soundPlayerController
        self.tileWidth = map.tmxData.tilewidth
        self.tileHeight = map.tmxData.tileheight
        self.mapHeight = map.tmxData.height * self.tileHeight
        self.mapWidth = map.tmxData.width * self.tileWidth
        self.player = player
        self.map = map

    def collisionAllSprites(self, player, mapData, gameData):
        for sprite in mapData.allSprites:
            if sprite.isPhysicsApplied == True or sprite.isCollisionApplied == True:

                self.rightCollision(sprite, mapData)
                self.leftCollision(sprite, mapData)
                self.downCollision(sprite, mapData)
                self.upCollision(sprite, mapData)

                self.collisionWithEnemy(player, mapData.enemyGroup)
                self.pickUpItem(player, mapData.itemGroup, gameData)


    def rightCollision(self,player, map):

        # mapHeight = map.tmxData.height * tileHeight
        i=0

        if player.collisionMask.rect.right + player.speedx > 0:
            if player.speedx >= self.tileWidth: #Si on va plus vite qu'une tile/seconde
                while player.collisionMask.rect.right+i*self.tileWidth < player.collisionMask.rect.right + player.speedx:
                    if player.collisionMask.rect.right+i*self.tileWidth >= self.mapWidth:
                        j=0
                        while map.tmxData.get_tile_gid((self.mapWidth - 1 - j*self.tileWidth)/self.tileWidth, player.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER) == SOLID and map.tmxData.get_tile_gid((self.mapWidth - 1- j*self.tileWidth)/self.tileWidth, (player.collisionMask.rect.bottom)/self.tileHeight, COLLISION_LAYER) == SOLID:
                            j += 1
                        player.onCollision(SOLID, RIGHT)
                        return

                    upRightTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.right + i*self.tileWidth)/self.tileWidth, player.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER)
                    downRightTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.right + i*self.tileWidth)/self.tileWidth, (player.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER)

                    if (upRightTileGid  == SOLID or downRightTileGid  == SOLID) and player.speedx > 0 and player.facingSide == RIGHT:
                        while map.tmxData.get_tile_gid((player.collisionMask.rect.right + 1)/self.tileWidth, player.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.collisionMask.rect.right + 1)/self.tileWidth, (player.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER) != SOLID:
                            player.collisionMask.rect.right += 1
                        player.onCollision(SOLID, RIGHT)
                    i += 1

            else:
                upRightTileGid = self.map.tmxData.get_tile_gid((player.collisionMask.rect.right + player.speedx)/self.tileWidth, player.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER)
                downRightTileGid = self.map.tmxData.get_tile_gid((player.collisionMask.rect.right + player.speedx)/self.tileWidth, (player.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER)
                lowMidRightTileGid = self.map.tmxData.get_tile_gid((player.collisionMask.rect.right + player.speedx)/self.tileWidth, (player.collisionMask.rect.centery-10-1)/self.tileHeight, COLLISION_LAYER)
                highMidRightTileGid = self.map.tmxData.get_tile_gid((player.collisionMask.rect.right + player.speedx)/self.tileWidth, (player.collisionMask.rect.centery+10-1)/self.tileHeight, COLLISION_LAYER)

                if (upRightTileGid  == SOLID or downRightTileGid == SOLID or lowMidRightTileGid == SOLID or highMidRightTileGid == SOLID) and player.speedx > 0:
                    # while map.tmxData.get_tile_gid((player.collisionMask.rect.right + 1)/self.tileWidth, player.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.collisionMask.rect.right + 1)/self.tileWidth, (player.collisionMask.rect.bottom)/self.tileHeight, COLLISION_LAYER) != SOLID:
                    #     player.collisionMask.rect.right += 1
                    player.onCollision(SOLID, RIGHT)
                elif upRightTileGid  == SPIKE or downRightTileGid == SPIKE or lowMidRightTileGid == SPIKE or highMidRightTileGid == SPIKE:
                    player.onCollision(SPIKE, RIGHT)
                elif (upRightTileGid  == SPRING or downRightTileGid == SPRING or lowMidRightTileGid == SPRING or highMidRightTileGid == SPRING) and player.speedx > 0:
                    player.onCollision(SPRING, RIGHT)

    def getUpRightTileGid(self):
        return self.map.tmxData.get_tile_gid((self.player.collisionMask.rect.right + self.player.speedx)/self.tileWidth, self.player.collisionMask.rect.top/self.tileHeight, COLLISION_LAYER)
    def getDownRightTileGid(self):
        return self.map.tmxData.get_tile_gid((self.player.collisionMask.rect.right + self.player.speedx)/self.tileWidth, (self.player.collisionMask.rect.bottom-1)/self.tileHeight, COLLISION_LAYER)
    def getLowMidRightTileGid(self):
        return self.map.tmxData.get_tile_gid((self.player.collisionMask.rect.right + self.player.speedx)/self.tileWidth, (self.player.collisionMask.rect.centery-10-1)/self.tileHeight, COLLISION_LAYER)
    def getHighMidRightTileGid(self):
        return self.map.tmxData.get_tile_gid((self.player.collisionMask.rect.right + self.player.speedx)/self.tileWidth, (self.player.collisionMask.rect.centery+10-1)/self.tileHeight, COLLISION_LAYER)
    # def getRightTilesList(self): à terminer si besoin (décomposer le nb de pts de vérification sur le sprite selon sa taille, à place de 4 fixes)
    #     tileList = []
    #     pointNumber = self.tileHeight
    #     tileList.append(self.map.tmxData.get_tile_gid((self.player.collisionMask.rect.right + self.player.speedx)/self.tileWidth, (self.player.collisionMask.rect.centery+10-1)/self.tileHeight, COLLISION_LAYER))

    def leftCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight
        # mapWidth = map.tmxData.width * tileWidth
        # mapHeight = map.tmxData.height * tileHeight
        i = 0

        if -player.speedx >= tileWidth:
            while player.collisionMask.rect.x-i*tileWidth > player.collisionMask.rect.x + player.speedx:
                if player.collisionMask.rect.x-i*tileWidth <= 0:
                    j=0
                    while map.tmxData.get_tile_gid((0 + j*tileWidth)/tileWidth, player.collisionMask.rect.top/tileHeight, COLLISION_LAYER) == SOLID and map.tmxData.get_tile_gid((0 + j*tileWidth)/tileWidth, (player.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER) == SOLID:
                        j += 1
                    player.onCollision(SOLID, LEFT)
                    return

                upLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left - i*tileWidth)/tileWidth, player.collisionMask.rect.top/tileHeight, COLLISION_LAYER)
                downLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left - i*tileWidth)/tileWidth, (player.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER)

                if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID) and player.facingSide == LEFT:
                    while map.tmxData.get_tile_gid((player.collisionMask.rect.left)/tileWidth, player.collisionMask.rect.top/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.collisionMask.rect.left)/tileWidth, (player.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER) != SOLID:
                        player.collisionMask.rect.left -= 1
                    player.onCollision(SOLID, LEFT)
                i += 1

        else:
            upLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left + player.speedx)/tileWidth, player.collisionMask.rect.top/tileHeight, COLLISION_LAYER)
            downLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left + player.speedx)/tileWidth, (player.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER)
            lowMidLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left + player.speedx)/tileWidth, (player.collisionMask.rect.centery-10)/tileHeight, COLLISION_LAYER)
            highMidLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left + player.speedx)/tileWidth, (player.collisionMask.rect.centery+10)/tileHeight, COLLISION_LAYER)

            if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID or lowMidLeftTileGid == SOLID or highMidLeftTileGid == SOLID) and player.speedx < 0:
                #while map.tmxData.get_tile_gid((player.collisionMask.rect.left)/tileWidth, player.collisionMask.rect.top/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.collisionMask.rect.left)/tileWidth, (player.collisionMask.rect.bottom-1)/tileHeight, COLLISION_LAYER) != SOLID:
                     #player.collisionMask.rect.left -= 1
                player.onCollision(SOLID, LEFT)
            elif upLeftTileGid  == SPIKE or downLeftTileGid  == SPIKE or lowMidLeftTileGid == SPIKE or highMidLeftTileGid == SPIKE:
                player.onCollision(SPIKE, LEFT)
            elif (upLeftTileGid  == SPRING or downLeftTileGid  == SPRING or lowMidLeftTileGid == SPRING or highMidLeftTileGid == SPRING) and player.speedx < 0:
                player.onCollision(SPRING, LEFT)


    def downCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight
        # mapWidth = map.tmxData.width * tileWidth
        # mapHeight = map.tmxData.height * tileHeight

        downLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left+1)/tileWidth, (player.collisionMask.rect.bottom + player.speedy)/tileHeight, COLLISION_LAYER)
        downRightTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.right)/tileWidth, (player.collisionMask.rect.bottom + player.speedy)/tileHeight, COLLISION_LAYER)
        downMidTileGID = map.tmxData.get_tile_gid((player.collisionMask.rect.centerx)/tileWidth, (player.collisionMask.rect.bottom + player.speedy)/tileHeight, COLLISION_LAYER)

        if downLeftTileGid == SOLID or downRightTileGid == SOLID or downMidTileGID == SOLID:
            # while map.tmxDaata.get_tile_gid((player.collisionMask.rect.left+1)/tileWidth, (player.collisionMask.rect.bottom)/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.collisionMask.rect.right)/tileWidth, (player.collisionMask.rect.bottom)/tileHeight, COLLISION_LAYER) != SOLID:
            #     player.collisionMask.rect.bottom += 1
            player.onCollision(SOLID, DOWN)
        elif downLeftTileGid == SPIKE or downRightTileGid == SPIKE  or downMidTileGID == SPIKE:
            player.onCollision(SPIKE, DOWN)
        elif downLeftTileGid == SPRING or downRightTileGid == SPRING  or downMidTileGID == SPRING:
            player.onCollision(SPRING, DOWN)
        else:
            player.onCollision(NONE, DOWN)

    def upCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight

        upLeftTileGid = map.tmxData.get_tile_gid((player.collisionMask.rect.left+1)/tileWidth, (player.collisionMask.rect.top + player.speedy)/tileHeight, COLLISION_LAYER)
        upRightTileGid = map.tmxData.get_tile_gid(player.collisionMask.rect.right/tileWidth, (player.collisionMask.rect.top + player.speedy)/tileHeight, COLLISION_LAYER)
        upMidTileGid = map.tmxData.get_tile_gid(player.collisionMask.rect.centerx/tileWidth, (player.collisionMask.rect.top + player.speedy)/tileHeight, COLLISION_LAYER)

        if upLeftTileGid == SOLID or upRightTileGid == SOLID or upMidTileGid == SOLID:
            player.onCollision(SOLID, UP)

        elif upLeftTileGid == SPIKE or upRightTileGid == SPIKE:
            player.onCollision(SPIKE, UP)
        elif upLeftTileGid == LADDER or upRightTileGid == LADDER or upMidTileGid == LADDER:
            player.onCollision(LADDER, UP)
        else:
            player.onCollision(NONE, UP)

    def collisionWithEnemy(self, player, enemyGroup):
        collisionList = pygame.sprite.spritecollide(player, enemyGroup, False)
        for enemy in collisionList:
            player.detonate()
            player.hurt()
            # player.loseLife()
            # self.soundControl.hurt()
            pass

    def pickUpItem(self, player, itemGroup, gameMemory):
        collisionList = pygame.sprite.spritecollide(player, itemGroup, False)
        for item in collisionList:
            gameMemory.registerItemPickedUp(item)
            item.kill()

def collisionBulletWall(bullet, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight
    mapWidth = map.tmxData.width * tileWidth
    mapHeight = map.tmxData.height * tileHeight

    if (bullet.rect.top < tileHeight or bullet.rect.bottom > mapHeight - tileHeight) or (bullet.rect.left < tileWidth or bullet.rect.right > mapWidth - tileWidth):
        bullet.kill()
        return

    if bullet.speedx > 0:
        upRightTileGid = map.tmxData.get_tile_gid((bullet.rect.right + bullet.speedx)/tileWidth, bullet.rect.top/tileHeight, COLLISION_LAYER)
        downRightTileGid = map.tmxData.get_tile_gid((bullet.rect.right + bullet.speedx)/tileWidth, (bullet.rect.bottom-1)/tileHeight, COLLISION_LAYER)

        if (upRightTileGid  == SOLID or downRightTileGid  == SOLID):
            bullet.kill()

    elif bullet.speedx < 0:
        upLeftTileGid = map.tmxData.get_tile_gid((bullet.rect.left + bullet.speedx)/tileWidth, bullet.rect.top/tileHeight, COLLISION_LAYER)
        downLeftTileGid = map.tmxData.get_tile_gid((bullet.rect.left + bullet.speedx)/tileWidth, (bullet.rect.bottom)/tileHeight, COLLISION_LAYER)

        if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID) and bullet.speedx < 0:
            bullet.kill()

    if (bullet.rect.top < tileHeight or bullet.rect.bottom > mapHeight - tileHeight) or (bullet.rect.left < tileWidth or bullet.rect.right > mapWidth - tileWidth):
        bullet.kill()
        return

    if bullet.speedx > 0:
        upRightTileGid = map.tmxData.get_tile_gid((bullet.rect.right + bullet.speedx)/tileWidth, bullet.rect.top/tileHeight, COLLISION_LAYER)
        downRightTileGid = map.tmxData.get_tile_gid((bullet.rect.right + bullet.speedx)/tileWidth, (bullet.rect.bottom-1)/tileHeight, COLLISION_LAYER)

        if (upRightTileGid  == SOLID or downRightTileGid  == SOLID):
            bullet.kill()

    elif bullet.speedx < 0:
        upLeftTileGid = map.tmxData.get_tile_gid((bullet.rect.left + bullet.speedx)/tileWidth, bullet.rect.top/tileHeight, COLLISION_LAYER)
        downLeftTileGid = map.tmxData.get_tile_gid((bullet.rect.left + bullet.speedx)/tileWidth, (bullet.rect.bottom)/tileHeight, COLLISION_LAYER)

        if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID) and bullet.speedx < 0:
            bullet.kill()

def collisionBulletEnemy(bullet, map):
    collisionList = pygame.sprite.spritecollide(bullet, map.enemyGroup, False)
    for enemy in collisionList:
        bullet.detonate()

def collisionGrenadeEnemy(grenade, map):
    collisionList = pygame.sprite.spritecollide(grenade, map.enemyGroup, False)
    for enemy in collisionList:
        grenade.detonate()

def collisionBulletPlayer(map, player):
    collisionList = pygame.sprite.spritecollide(player, map.enemyBullet, False)
    for bullet in collisionList:
        player.hurt()
        bullet.kill()

def printTile(tile):
    if tile == SOLID:
        print('SOLID')
    elif tile == SPIKE:
        print('SPIKE')
    elif tile == SPRING:
        print('SPRING')
    else:
        print(tile)

def collisionExplosionEnemy(explosion, mapData):
    circle = Circle((explosion.collisionMask.rect.centerx, explosion.collisionMask.rect.centery),explosion.collisionMask.rect.width/2)

    for enemy in mapData.enemyGroup:
        if collisionCircleRect(circle, enemy.rect):
            enemy.hurt()


def collisionCircleRect(circle, rect):
    circleDistancex = abs(circle.x - rect.centerx)
    circleDistancey = abs(circle.y - rect.centery)

    if (circleDistancex > (rect.width/2 + circle.r)):
        return False
    if (circleDistancey > (rect.height/2 + circle.r)):
        return False

    if (circleDistancex <= (rect.width/2)):
        return True
    if (circleDistancey <= (rect.height/2)):
        return True

    cornerDistance_sq = (circleDistancex - rect.width/2)**2 + (circleDistancey - rect.height/2)**2

    return (cornerDistance_sq <= (circle.r**2))

def printTopTile(tile):
    if tile == SOLID:
        print("SOLID")
    elif tile == SPIKE:
        print("SPIKE")
    elif tile == SPRING:
        print("SPRING")
    elif tile == LADDER:
        print("LADDER")

def printJumpState(state):
    if state == GROUNDED:
        print("GROUNDED")
    elif state == JUMP:
        print("JUMP")
    elif state == CLIMBING:
        print("CLIMBING")

