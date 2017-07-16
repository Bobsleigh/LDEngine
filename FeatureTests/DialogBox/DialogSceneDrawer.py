__author__ = 'Bobsleigh'

from ldLib.scene.Drawer import Drawer
from app.settings import *

class DialogSceneDrawer(Drawer):
    def __init__(self):
        super().__init__()

    def draw(self, screen, sprites, spritesHUD, spritesBackGround, player):
        screen.fill(WHITE)
        super().draw(screen, sprites, spritesHUD, spritesBackGround, player)