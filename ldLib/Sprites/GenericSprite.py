import pygame
from LDEngine.ldLib.collision.collisionMask import CollisionMask
from LDEngine.ldLib.animation.Animation import Animation

#
# Generic sprite to create
#
# All the name and type need to have the first letter in capital (because.. windows)
#

class GenericSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "GenericSprite"
        self.type = "Sprite"

        self.imageSprite = pygame.Surface((1, 1))
        self.imageSprite.set_alpha(0)
        self.image = self.imageSprite

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y

        self.collisionMask = CollisionMask(self.rect.x, self.rect.y, self.rect.width, self.rect.height)

        # dictProperties have all the property we can read in the xml file of the map for the sprite.
        # We need to give the name of the property and the function to call if found.
        # Example : self.dictProperties = {"Color": self.setColor}
        self.dictProperties = {}

        self.collisionRules = []

        self.mapData = None
        self._state = None

    def setTheMap(self, mapData):
        self.mapData = mapData

    def update(self):
        #self.animation.update()
        self.updateCollisionMask()

    def updateCollisionMask(self):
        self.collisionMask.rect.x = self.rect.x
        self.collisionMask.rect.y = self.rect.y

    def isHit(self,dmg=0):
        pass

    def dead(self):
        self.kill()

    def notify(self, event):
        pass

    def state(self):
        return self._state