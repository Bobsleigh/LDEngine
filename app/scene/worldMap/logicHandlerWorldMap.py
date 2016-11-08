from app.mapData import MapData
from app.scene.worldMap.collisionPlayerWorldMap import CollisionPlayerWorldMap

class LogicHandlerWorldMap:
    def __init__(self, player, gameData):
        self.sceneRunning = True
        self.endState = None
        # self.spawmPointPlayerx = 0
        # self.spawmPointPlayery = 0
        self.newMapData = None
        self.boolGoToLevelHome = False
        self.gameData = gameData
        self.mapData = gameData.mapData
        self.collisionChecker = CollisionPlayerWorldMap(player, self.mapData)

    def handle(self, player, oldX, oldY):
        self.collisionChecker.collisionAllSprites(player, self.mapData, oldX, oldY)
        self.handleZoneCollision(player)
        self.mapData.allSprites.update()

    def handleZoneCollision(self, player):
        for obj in self.mapData.tmxData.objects:
            if self.isPlayerIsInZone(player, obj) == True:
                if obj.name == "OutZone":

                    #Skip level transition if level is locked
                    if obj.LevelZone == 'LevelDesert' and self.gameData.mapUnlock['map2'] == False:
                        break
                    if obj.LevelZone == 'LevelSaloon' and self.gameData.mapUnlock['map3'] == False:
                        break
                    if obj.LevelZone == 'LevelIndian' and self.gameData.mapUnlock['map3'] == False:
                        break

                    nameNewZone = obj.LevelZone
                    nameInZone = obj.InZone

                    # Special case for LevelHome
                    if obj.LevelZone == 'LevelHome':
                        self.boolGoToLevelHome = True
                    else:
                        # Initializing new map
                        self.newMapData = MapData(nameNewZone, nameInZone)

    def isPlayerIsInZone(self, player, object):

        if player.rect.centerx  >= object.x and \
           player.rect.centerx <= object.x + object.width and \
           player.rect.centery >= object.y and \
           player.rect.centery <= object.y + object.height:
           return True
        else:
           return False