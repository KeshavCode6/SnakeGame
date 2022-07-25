import pygame, random
from utils import *

class Cell:
    def __init__(self, position:tuple, size:tuple):
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.sprite = pygame.transform.scale(pygame.image.load("res/Tile.png"), size)
        self.apple = pygame.transform.scale(pygame.image.load("res/Apple.png"), size)
        self.isApple = False
    def Draw(self):
        if not self.isApple:
            screen.blit(self.sprite, self.rect)
        else:
            screen.blit(self.apple, self.rect)

class Grid:
    def __init__(self, cellSize):
        self.cells = []
        self.cellSize = cellSize

        x, y = 0, 0


        while x < width:
            while y < height:
                self.cells.append(Cell((x,y), (self.cellSize, self.cellSize)))
                y+=self.cellSize

            y = 0
            x += self.cellSize
        self.GenApple()

    def GetCellAt(self, pos:tuple):
        for cell in self.cells:
            if cell.rect.topleft == pos:
                return cell
    def Draw(self):
        for cell in self.cells:
            cell.Draw()
    
    def GenApple(self):
        i = random.randint(0, len(self.cells)-1)

        self.cells[i].isApple = True
    
    def Update(self):
        self.Draw()