import pygame
from sys import exit

class EventHandlerTitleScreen():
    def __init__(self, menu):
        self.menu = menu

    def eventHandle(self,optionList,selector):
        self.optionList = optionList
        self.selector = selector
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            self.menu.notify(event)
