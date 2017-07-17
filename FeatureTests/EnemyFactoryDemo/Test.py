from FeatureTests.EnemyFactoryDemo.TestSceneData import TestSceneData
from FeatureTests.EnemyFactoryDemo.TestSceneLogicHandler import TestSceneLogicHandler

import os
import sys

import pygame

from ldLib.scene.Scene import Scene
from ldLib.scene.GameData import GameData
from app.settings import *

#
# This test check if the factory for the list of enemy work well
#

if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
         os.chdir(sys._MEIPASS)

    # Screen
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenSize)

    pygame.display.set_caption("TestEnemyFactory")

    # Init
    pygame.mixer.pre_init(22050 , -16, 2, 4096)
    # pygame.mixer.init()
    pygame.init()
    pygame.font.init()

    # Hide the mouse
    # pygame.mouse.set_visible(False)

    # Create the test scene
    gameData = GameData()
    gameData.sceneData = TestSceneData()
    logicHandler = TestSceneLogicHandler(gameData)
    testScene = Scene(screen, gameData, logicHandler)
    testScene.run()