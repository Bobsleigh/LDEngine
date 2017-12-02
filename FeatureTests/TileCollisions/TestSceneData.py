__author__ = 'Bobsleigh'
from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX
from LDEngine.FeatureTests.TileCollisions.playerTest import PlayerTest


class TestSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestCollisions")

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerTest(playerInitx, playerInity, self)
        self.camera.add(self.player)