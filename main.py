import os
import sys

import pygame

from app.scene.sceneHandler import SceneHandler
from app.scene.titleScreen.titleScreen import TitleScreen
from app.settings import *

if __name__ == '__main__':

    # Uncomment the test you want to run. This main file is needed to keep the relative path intact.

    if (TAG_MARIE==1):
        exec(open('FeatureTests\AnimationDemo\Test.py').read())

    if TAG_BP:
        #exec(open('FeatureTests\TileCollisions\Test.py').read())
        exec(open('FeatureTests\TmxDataDemo\Test.py').read())
        #exec(open('FeatureTests\DialogBox\Test.py').read())

# exec(open('FeatureTests\DialogBox\Test.py').read())
# exec(open('FeatureTests\TileCollisions\Test.py').read())
# exec(open('FeatureTests\DialogBox\Test.py').read())
