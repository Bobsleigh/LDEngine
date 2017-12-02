__author__ = 'Bobsleigh'
from LDEngine.ldLib.scene.SceneData import SceneData
from FeatureTests.TileCollisions.playerTest import PlayerTest
from LDEngine.ldLib.GUI.WrLDEngine.appedTextBox import WrLDEngine.appedTextBox
from LDEngine.ldLib.GUI.DialogBox import DialogBox


class DialogSceneData(SceneData):
    def __init__(self):
        super().__init__()

        self.wrLDEngine.appedTextBox = WrLDEngine.appedTextBox((100,100), (400,200), "Salut!TEST!The text can only be a single line: newline characters are not rendered. Null characters (‘x00’) raise a TypeError. Both Unicode and char (byte) strings are accepted. For Unicode strings only UCS-2 characters (‘u0001’ to ‘uFFFF’) are recognized. Anything greater raises a UnicodeError. For char strings ", (10,10))
        self.spritesHUD.add(self.wrLDEngine.appedTextBox)

        self.wrLDEngine.appedTextBox2 = WrLDEngine.appedTextBox((50,400), (100,100), "Bonjour", (10,10))
        self.spritesHUD.add(self.wrLDEngine.appedTextBox2)

        self.dialogBox = DialogBox((200,400), (100,100), "DialogBox", (10,10))
        self.spritesHUD.add(self.dialogBox)
        self.notifyGroup.add(self.dialogBox)