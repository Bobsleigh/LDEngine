import pygame
from sys import exit

class EventHandlerTitleScreen():
    def __init__(self):
        pass

    def eventHandle(self,optionList,selector):
        self.optionList = optionList
        self.selector = selector
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT: #Does nothing for now...
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveRight()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_LEFT: #Does nothing for now...
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveLeft()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_UP:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveUp()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_DOWN:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveDown()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_SPACE:
                    self.optionList[self.selector.vPos].doOption()
                elif event.key == pygame.K_RETURN:
                    self.optionList[self.selector.vPos].doOption()
