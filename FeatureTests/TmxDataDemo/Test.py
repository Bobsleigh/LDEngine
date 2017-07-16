from FeatureTests.TmxDataDemo.TestSceneData import TestSceneData
from FeatureTests.TmxDataDemo.TestSceneLogicHandler import TestSceneLogicHandler

import os
import sys

import pygame

from ldLib.scene.Scene import Scene
from ldLib.scene.GameData import GameData
from app.settings import *

#
# This test does not work well.
#
# To use the tileType (not the gid) properly, we need to change all the "map.tmxData.get_tile_gid"
# in collision code.
#
# Instruction :
# Replace all the "map.tmxData.get_tile_gid" by "map.tmxData.get_tileType"
# BUT : The tmxData is not pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))   (Check MapData code)
#
# In this case, You need to do
# self.rawTmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
# self.tmxData = TmxData(self.rawTmxData)
#

if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
         os.chdir(sys._MEIPASS)

    # Screen
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenSize)

    pygame.display.set_caption("TestTmXData")

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