from LDEngine.FeatureTests.AnimationDemo.AnimatedPlayer import AnimatedPlayer

__author__ = 'Bobsleigh'
from LDEngine.ldLib.scene.SceneDataTMX import SceneDataTMX


class AnimationDemoSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("AnimateMap")

        self.player = AnimatedPlayer(50, 50, self)
        self.camera.add(self.player)