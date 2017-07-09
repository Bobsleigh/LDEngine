__author__ = 'Bobsleigh'

import pygame
import weakref

class SceneData:
    def __init__(self):
        self.nextScene = None

        self.notifySet = weakref.WeakSet()
        self.allSprites = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()
        self.spritesBackGround = pygame.sprite.Group()

        self.player = None
        self.camera = None