from FeatureTests.DialogBox.DialogSceneData import DialogSceneData
from FeatureTests.DialogBox.DialogSceneLogicHandler import DialogSceneLogicHandler

__author__ = 'Bobsleigh'

import os
import sys

import pygame

from ldLib.scene.Scene import Scene
from ldLib.scene.GameData import GameData
from app.settings import *
from FeatureTests.DialogBox.DialogSceneDrawer import DialogSceneDrawer



if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
         os.chdir(sys._MEIPASS)

    # Screen
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenSize)
    screen.fill(WHITE)

    pygame.display.set_caption("TestDialogBox")

    # Init
    pygame.mixer.pre_init(22050 , -16, 2, 4096)
    # pygame.mixer.init()
    pygame.init()
    pygame.font.init()

    # Hide the mouse
    # pygame.mouse.set_visible(False)

    # Create the test scene
    gameData = GameData()
    gameData.sceneData = DialogSceneData()
    logicHandler = DialogSceneLogicHandler(gameData)
    testScene = Scene(screen, gameData, logicHandler)
    testScene.drawer = DialogSceneDrawer()
    testScene.run()