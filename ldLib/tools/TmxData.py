#
# TmxData
#
# WrLDEngine.apper of a TiledMap
# generated by pytmx.util_pygame.load_pygame('MapName.tmx')
#
# All the data are parsed to give more elemental functionalities
#
# layer : All layer in order (bottom to top)
# A basic layer set-up can be :
#  - Collision_TL
#  - Background_TL
#  - Terrain_TL
#  - Sprite_TL
#  - SpriteHUD_TL
#  - Upper_TL
#  - GameHUD_TL
#  - Menu_TL
#  - IOZone_OL
#  - Sprite_OL
#  NOTE : The layer name and number CAN be different.
# gidMap : The gidMap between gid and real number in the tilesets
#
# Nomenclature :
#
# The "gid" are the numbers generated by pytmx when loading the tmx file.
# The number 0 is non existent tile (transparency).
#
# The "tileType" are the number we can understand by checking the tilesets.
# The number 0 is non existent tile (transparency).
# The number 1 to L1 x C1 are the L1 x C1 first tiles of the first set (L1 x C1).
# (read from left to right, top to bottom)
# The number L1 x C1 + 1 to L1 x C1 + L2 x C2 are the L2 x C2 nexts tiles of the second set (L2 x C2).
# And so on...
#
# For info, useful function of TiledMap :
#       get_tile_gid(i,j,layer(number))
#       get_layer_by_name(name)
#
# To check all data :
#  pp.pprint(self.rawTmxData.__dict__)
#
# Link
# http://pytmx.readthedocs.io/en/latest/
#

import ntpath
import pprint as pp
import re

from LDEngine.app.settings import *
from LDEngine.ldLib.tools.Printer import *


class TmxData:
    def __init__(self, rawTmxData):

        self.rawTmxData = rawTmxData

        self.tileWidth = self.rawTmxData.tilewidth
        self.tileHeight = self.rawTmxData.tileheight
        self.width = self.rawTmxData.width
        self.height = self.rawTmxData.height

        self.mapName = ntpath.basename(self.rawTmxData.filename)

        self.layers = self.extractLayerName()

        # gidMap : gid -> tileType
        self.gidMap = self.rawTmxData.tiledgidmap
        # Add the number 0 in the gid
        self.gidMap[0] = 0
        self.reversedGidMap = self.reverseGidMap()

        self.layerCollisionName = 'Collision_TL'
        self.layerTerrainName = 'Terrain_TL'

        # An element of the list is : [(i,j, the layer, the new number)]
        self.listTileToChange = []

        self.diagnoseTmxData()


    # Give the gid from the tile type
    def get_gidFromTileType(self, noTile):
        return self.reversedGidMap[noTile]

    # Give the real type of tile for an gid
    def get_tileTypeFromGid(self, gid):
        return self.gidMap[gid]

    # Give the real type of tile at position (x,y)
    def get_tileType(self, x, y, layer):
        layerNumber = self.get_layerNumber(layer)

        gid = self.rawTmxData.get_tile_gid(x, y, layerNumber)
        return self.gidMap[gid]

    # Give the real type of tile at the sprite collisionMask position
    # May add an shift (i,j) if needed
    def get_tileTypeInSprite(self, sprite, layer, position='C', i=0, j=0):
        layerNumber = self.get_layerNumber(layer)

        pos = self.get_spritePosition(self, sprite.collisionMask, position)
        gid = self.rawTmxData.get_tile_gid((pos.x + j*self.tileWidth)/self.tileWidth, (pos.y + i*self.tileWidth)/self.tileHeight, layerNumber)
        return self.gidMap[gid]

    # Give the real type of tile at the sprite collisionMask position (We add the movement speed)
    def get_nextTileTypeInMovingSprite(self, sprite, layer, position='C'):
        layerNumber = self.get_layerNumber(layer)

        pos = self.get_spritePosition(self, sprite.collisionMask, position)
        gid = self.rawTmxData.get_tile_gid((pos.x + sprite.speedx)/self.tileWidth, (pos.y + sprite.speedy)/self.tileHeight, layerNumber)
        return self.gidMap[gid]

    # Add a tile at position (x,y) to the list to change it
    def addTileTypeXYToListToChange(self, coupleXY, newNumber, layer=None):
        if layer is None:
            layer = self.layerTerrainName
        else:
            layer = self.get_layerName(layer)
        self.addTileTypeIJToListToChange((int(coupleXY[1]/self.tileHeight), int(coupleXY[0]/self.tileWidth)), newNumber, layer)

    # Add a tile at position (i,j) to the list to change it
    def addTileTypeIJToListToChange(self, coupleIJ, newNumber, layer=None):
        if layer is None:
            layer = self.layerTerrainName
        else:
            layer = self.get_layerName(layer)
        self.listTileToChange.LDEngine.append((coupleIJ[0], coupleIJ[1], layer, newNumber))

    # Change all the time at once and update : CARE, we use "redraw_tiles" of pyscroll.BufferedRenderer
    # We change all, because it is more fast this way.
    # (One by one is too slow)
    def changeAllTileTypeInList(self, bufferedRenderer):
        # If the list is empty, we do nothing
        if self.listTileToChange:
            # Loop on self.listTileToChange
            for (i,j,layer,newNumber) in self.listTileToChange:
                layer = self.rawTmxData.get_layer_by_name(layer)
                layerData = layer.data
                layerData[i][j] = self.get_gidFromTileType(newNumber)
            # Change all
            bufferedRenderer.redraw_tiles(bufferedRenderer._buffer)
            # Clean up the list
            self.listTileToChange = []


    ###################################################
    # Privates functions
    ###################################################
    # Extract the layer names
    def extractLayerName(self):

        layers = {}
        dim = len(self.rawTmxData.layers)
        for k in range(0,dim-1):
            layer = pp.pformat(self.rawTmxData.layers[k])
            layer = re.findall(r'"([^"]*)"', layer)[0]
            layers[layer] = k
        return layers

    ###################################################
    # Reverse the Gid map to get the real ID of tile in function of a number in the Gid
    def reverseGidMap(self):
        reversed = {}
        for key, value in self.gidMap.items():
            reversed[value] = key
        return reversed

    ###################################################
    # Give the layer number (can input a number or a name)
    def get_layerNumber(self, layer):
        try:
            layerNumber = int(layer)
        except ValueError:
            layerNumber = self.layers[layer]
        return layerNumber

    ###################################################
    # Give the layer name (can input a number or a name)
    def get_layerName(self, layer):
        try:
            int(layer)
        except ValueError:
            layerName = layer
        else:
            layerName = pp.pformat(self.rawTmxData.layers[layer])
            layerName = re.findall(r'"([^"]*)"', layerName)[0]
        return layerName

    ###################################################
    # Give the position (x,y) of a sprite : Left(L), Right(R), Upper(U), Bottom(B), Center(C)
    def get_spritePosition(self, sprite, position='C'):
        if position == 'C':
            return sprite.rect.centerx, sprite.rect.centery
        if position == 'B' or position == 'CB':
            return sprite.rect.centerx, sprite.rect.bottom
        if position == 'U' or position == 'CU':
            return sprite.rect.centerx, sprite.rect.top
        if position == 'L' or position == 'CL':
            return sprite.rect.left, sprite.rect.centery
        if position == 'R' or position == 'CR':
            return sprite.rect.right, sprite.rect.centery
        if position == 'BL':
            return sprite.rect.left, sprite.rect.bottom
        if position == 'BR':
            return sprite.rect.right, sprite.rect.bottom
        if position == 'UL':
            return sprite.rect.left, sprite.rect.top
        if position == 'UR':
            return sprite.rect.right, sprite.rect.top
        raise ValueError('Not a valid position for a sprite in TmxData')

    ###################################################
    # Check some default propriety in the map
    # If some error occur, a message will be print
    # Set TAP_DIAGNOSE_MAP_TMX to 1 (to use)
    def diagnoseTmxData(self):
        if TAP_DIAGNOSE_MAP_TMX == 1:
            # Check if the map got an in zone : IOZone_OL
            try:
                self.rawTmxData.get_layer_by_name("IOZone_OL")
            except ValueError:
                printWarning("No IOZone_OL layer detected in " + self.mapName)
            # Check if the map got an in zone : InZone
            found = 0
            for obj in self.rawTmxData.objects:
                if obj.type == "InZone":
                    found = 1
                    break
            if found == 0:
                printWarning("No InZone detected in " + self.mapName)
