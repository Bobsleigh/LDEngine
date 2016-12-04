from app.sprites.enemy.enemy import Enemy
from app.sprites.enemy.enemyShooter import EnemyShooter

class EnemyFactory:
    def __init__(self):
        self.dictEnemies = {'enemyBase':    Enemy,
                            'enemyShooter': EnemyShooter}

    def create(self, tmxEnemy, theMap=None):

        enemyName = tmxEnemy.name
        if enemyName in self.dictEnemies:
            enemy = self.dictEnemies[enemyName](tmxEnemy.x, tmxEnemy.y)

            for nameProp, prop in tmxEnemy.properties.items():
                if nameProp in enemy.dictProperties:
                    enemy.dictProperties[nameProp](prop)

            enemy.setTheMap(theMap)
            return enemy
        return None
