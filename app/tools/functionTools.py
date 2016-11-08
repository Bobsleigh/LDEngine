from sys import exit

# seek the attribute name in object, if none, pass
def seekAtt(objectLocal, nameAttribute):
    try:
        return getattr(objectLocal, nameAttribute)
    except AttributeError:
        return None

# quit game ( NEVER USE quit() )
def quitGame():
    exit()
