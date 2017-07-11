__author__ = 'Bobsleigh'
from ldLib.scene.SceneDataTMX import SceneDataTMX
from FeatureTests.TileCollisions.playerTest import PlayerTest


class TestSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestCollisions")

        self.player = PlayerTest(50, 50, self)
        self.camera.add(self.player)