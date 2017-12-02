__author__ = 'Bobsleigh'

from LDEngine.ldLib.scene.Drawer import Drawer
from LDEngine.app.settings import *

class DialogSceneDrawer(Drawer):
    def __init__(self):
        super().__init__()

    def draw(self, screen, sprites, spritesHUD, spritesBackGround, player):
        screen.fill(WHITE)
        super().draw(screen, sprites, spritesHUD, spritesBackGround, player)