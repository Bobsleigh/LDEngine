#To initialize my pet
from app.MusicHandler import MusicHandler


# All the global data for the game and player
class GameData:
    def __init__(self, scene=None):

        #Was map unlocked?
        self.mapUnlock = {}
        self.mapUnlock["map1"] = True
        self.mapUnlock["map2"] = False
        self.mapUnlock["map3"] = False
        self.mapUnlock["map4"] = False

        self.maxItemOfAType = 99

        self.scene = scene

        self.mapData = None

        self.MusicHandler = MusicHandler("mainMenu.ogg")
        self.MusicHandler.play()