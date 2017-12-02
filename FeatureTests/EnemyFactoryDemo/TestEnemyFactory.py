from ldLib.Sprites.SpriteFactory import SpriteFactory

from FeatureTests.EnemyFactoryDemo.TestEnemyNoob import EnemyNoob

#
# Need to add all the enemy you gwant to generate.
# Otherwise, the enemy will not be created.
#

class EnemyFactory(SpriteFactory):
    def __init__(self):
        self.dictSprite = {"EnemyNoob": EnemyNoob}
