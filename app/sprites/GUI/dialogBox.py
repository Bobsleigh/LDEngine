import pygame
import os
from app.settings import *
from app.sprites.GUI.Box import Box


class DialogBox(pygame.sprite.Sprite):
    def __init__(self,pos, size, text):
        super().__init__()

        self.marginX = 10
        self.marginY = 10
        self.spaceBetweenLines = 20

        self.box = Box(pos,size)

        self.image = self.box.image
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

        self.arial = pygame.font.SysFont("Arial", DIALOG_TEXT_SIZE)
        self.text = self.renderWrappedText(text)

    def isTextLongerThanBox(self, renderedTxt):
        txtRect = renderedTxt.get_rect()
        if txtRect.width + self.marginX * 2 > self.rect.width:
            return True
        else:
            return False

    def getWrappedLineList(self,text):
        line = ""
        lastLine = ""
        lineList = []
        renderList = []

        if self.isTextLongerThanBox(self.arial.render(text, False, BLACK)):
            wordList = text.split(" ")
            for word in wordList:
                lastLine = line
                line += (" " + word)
                render = self.arial.render(line, False, BLACK)

                if self.isTextLongerThanBox(render):
                    lineList.append(lastLine.lstrip())
                    lastWord = line.split(" ")[-1]
                    line = lastWord

            lineList.append(line.lstrip())

            return lineList

        else:
            return text

    def renderWrappedText(self, text):
        lineList = self.getWrappedLineList(text)
        i = 0

        while i < len(lineList):
            renderSize = self.arial.size(lineList[i])
            render = self.arial.render(lineList[i], False, BLACK)
            if i == 0:
                self.box.box.blit(render, (self.rect.x + self.marginX, self.rect.y + self.marginY))
            else:
                self.box.box.blit(render, (self.rect.x + self.marginX, self.rect.y + self.marginY + (self.spaceBetweenLines + renderSize[1]) * (i)))
            i += 1




