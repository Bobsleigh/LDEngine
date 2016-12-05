import sys

# seek the attribute name in object, if none, pass
def seekAtt(objectLocal, nameAttribute):
    try:
        return getattr(objectLocal, nameAttribute)
    except AttributeError:
        return None

# quit game ( NEVER USE quit() or exit() ), we use sys.exit()
def quitGame():
    sys.exit()
