import pygame
from ldLib.scene.SceneDataTMX import SceneDataTMX
from FeatureTests.EnemyFactoryDemo.PlayerTest import PlayerTest
from FeatureTests.EnemyFactoryDemo.TestEnemyFactory import EnemyFactory

class TestSceneData(SceneDataTMX):
    def __init__(self):
        super().__init__("TestEnemyFactory", "InZone_01")

        playerInitx = 50
        playerInity = 50
        try:
            playerInitx = self.spawmPointPlayerx
            playerInity = self.spawmPointPlayery
        except AttributeError:
            pass

        self.player = PlayerTest(playerInitx, playerInity, self)

        # Enemy Factory, we create all in one shot
        self.enemyGroup = pygame.sprite.Group()
        eFactory = EnemyFactory()
        for obj in self.tmxData.objects:
            if obj.type == "Enemy":
                enemy = eFactory.create(obj, self)
                if enemy is not None:
                    self.allSprites.add(enemy)
                    self.enemyGroup.add(enemy)

        # Add all the sprite to see them
        self.camera.add(self.allSprites)
