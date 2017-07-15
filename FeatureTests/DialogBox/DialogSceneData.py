__author__ = 'Bobsleigh'
from ldLib.scene.SceneData import SceneData
from FeatureTests.TileCollisions.playerTest import PlayerTest
from ldLib.GUI.WrappedTextBox import WrappedTextBox


class DialogSceneData(SceneData):
    def __init__(self):
        super().__init__()

        self.wrappedTextBox = WrappedTextBox((100,100), (400,200), "Salut!TEST!The text can only be a single line: newline characters are not rendered. Null characters (‘x00’) raise a TypeError. Both Unicode and char (byte) strings are accepted. For Unicode strings only UCS-2 characters (‘u0001’ to ‘uFFFF’) are recognized. Anything greater raises a UnicodeError. For char strings ", (10,10))
        self.spritesHUD.add(self.wrappedTextBox)

        self.wrappedTextBox2 = WrappedTextBox((50,400), (100,100), "Bonjour", (10,10))
        self.spritesHUD.add(self.wrappedTextBox2)