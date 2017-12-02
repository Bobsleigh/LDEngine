import pygame
from LDEngine.ldLib.Sprites.GenericSprite import GenericSprite

#
# Generic enemy to create
#

class GenericEnemy(GenericSprite):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.name = "GenericEnemy"
        self.type = "Enemy"