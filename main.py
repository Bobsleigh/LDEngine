import os
import sys

import pygame

from app.scene.sceneHandler import SceneHandler
from app.scene.titleScreen.titleScreen import TitleScreen
from app.settings import *

if __name__ == '__main__':

    exec(open('FeatureTests\TileCollisions\Test.py').read())