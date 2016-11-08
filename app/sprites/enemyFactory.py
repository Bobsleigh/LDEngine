from app.sprites.enemy.enemy import Enemy
from app.sprites.enemy.enemyShooter import EnemyShooter
from app.tools.functionTools import *


class EnemyFactory:
    def __init__(self):
        pass

    def create(self, enemy, theMap=None):
        eName = seekAtt(enemy, "name")
        if eName == "enemyCactus":
            return self.createEnemyCactus(enemy)
        if eName == "enemyShooter":
            return self.createEnemyShooter(enemy, theMap)


    def createEnemyBase(self, enemy):
        enemyCreated = Enemy(enemy.x, enemy.y)
        return enemyCreated

    def createEnemyShooter(self, enemy, theMap):
        direction = seekAtt(enemy, "direction")

        if direction is None:
            return EnemyShooter(enemy.x, enemy.y, theMap)
        else:
            return EnemyShooter(enemy.x, enemy.y, theMap, direction)