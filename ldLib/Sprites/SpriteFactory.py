#
# Simple sprite factory (self.dictSprite is void)
#
# Need to create children to do something.
#
# The concept of factory is that the factory known all the types he can construct.
# He create them and then return them.
#

class SpriteFactory:
    def __init__(self):
        self.dictSprite = {}

    def create(self, spriteTmx, theMap=None):

        spriteName = spriteTmx.name
        if spriteName in self.dictSprite:
            sprite = self.dictSprite[spriteName](spriteTmx.x, spriteTmx.y)

            # In the same time, we launch all the construction of the sprite if needed
            for nameProp, prop in spriteTmx.properties.items():
                if nameProp in sprite.dictProperties:
                    sprite.dictProperties[nameProp](prop)

            sprite.setTheMap(theMap)
            return sprite
        return None
