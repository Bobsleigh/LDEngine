__author__ = 'Bobsleigh'

import pygame
from LDEngine.ldLib.Sprites.SecondBoss.EnemyState import EnemyState
from LDEngine.app.settings import *

class MoveLeftState(EnemyState):
    def __init__(self):
        super().__init__()

    def update(self, sprite, mapData):
        sprite.updateSpeedLeft()

    def enter(self, sprite):
        pass

    def exit(self, sprite):
        pass