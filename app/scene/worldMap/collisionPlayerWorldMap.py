__author__ = 'Bobsleigh'

from app.settings import *
import pygame

class CollisionPlayerWorldMap:
    def __init__(self, player, map):
        # self.soundControl = soundPlayerController
        self.tileWidth = map.tmxData.tilewidth
        self.tileHeight = map.tmxData.tileheight
        self.mapHeight = map.tmxData.height * self.tileHeight
        self.mapWidth = map.tmxData.width * self.tileWidth
        self.player = player
        self.map = map

    def collisionAllSprites(self, player, mapData, oldTileX, oldTileY):
        currentTile = mapData.tmxData.get_tile_gid(self.player.tileX, self.player.tileY, COLLISION_LAYER)
        if currentTile == SOLID:
            player.tileX = oldTileX
            player.tileY = oldTileY

def printTile(tile):
    if tile == SOLID:
        print('SOLID')
    elif tile == SPIKE:
        print('SPIKE')
    else:
        print(tile)
