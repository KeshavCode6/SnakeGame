import pygame, sys
from utils import *
from grid import *

class Snake:
    def __init__(self, grid:Grid):
        self.grid = grid
        self.rect = pygame.Rect(0,0, grid.cellSize, grid.cellSize)
        
        self.velocity = (0,1)
        self.nextMove = 0
        
        self.isAlive = True
        self.score = 0

        self.headSprites = [pygame.transform.scale(pygame.image.load("res/SnakeHead_Up.png"), (self.grid.cellSize, self.grid.cellSize)),
                            pygame.transform.scale(pygame.image.load("res/SnakeHead_Down.png"), (self.grid.cellSize, self.grid.cellSize)),
                            pygame.transform.scale(pygame.image.load("res/SnakeHead_Left.png"), (self.grid.cellSize, self.grid.cellSize)),
                            pygame.transform.scale(pygame.image.load("res/SnakeHead_Right.png"), (self.grid.cellSize, self.grid.cellSize))]
        self.currentSprite = self.headSprites[1]
        self.tails = [self.rect]
        self.Grow()
        self.tailSprite = pygame.transform.scale(pygame.image.load("res/SnakeBody.png"), (self.grid.cellSize, self.grid.cellSize))
    
    def Draw(self):
        screen.blit(self.currentSprite, self.rect)

        i = 1
        while i < len(self.tails):
            screen.blit(self.tailSprite, self.tails[i])
            i+=1
    
    def Update(self):
        self.Draw()
        self.GetInput()
        self.Movement()

    def GetInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.velocity = (0, -1)
                    self.currentSprite = self.headSprites[0]
                if event.key == pygame.K_DOWN:
                    self.velocity = (0, 1)
                    self.currentSprite = self.headSprites[1]
                if event.key == pygame.K_LEFT:
                    self.velocity = (-1, 0)
                    self.currentSprite = self.headSprites[2]
                if event.key == pygame.K_RIGHT:
                    self.velocity = (1, 0)
                    self.currentSprite = self.headSprites[3]
                
                if event.key == pygame.K_ESCAPE:
                    self.isAlive = False
    
    def CheckForApple(self):
        cell = self.grid.GetCellAt(self.rect.topleft)

        if cell is not None:
            if cell.isApple:
                self.Grow()
                self.grid.GenApple()
                cell.isApple = False

    def Grow(self):
        lastPart = self.tails[len(self.tails)-1].topleft
        self.tails.append(pygame.Rect(lastPart[0]-self.grid.cellSize, lastPart[1], self.grid.cellSize, self.grid.cellSize))

        self.score += 1

    def CheckForSelfCollision(self):
        i = 1
        while i < len(self.tails):
            if self.rect.colliderect(self.tails[i]):
                self.isAlive = False
            i += 1

    def Movement(self):
        self.nextMove += 0.1
        
        if self.nextMove >= 1:
            self.CheckForApple()
            self.CheckForSelfCollision()

            i = len(self.tails)-1

            while i > 0:
                self.tails[i].topleft = self.tails[i-1].topleft
                i-=1
 
            self.rect.x += self.velocity[0]*self.grid.cellSize
            self.rect.y += self.velocity[1]*self.grid.cellSize
            
            self.nextMove = 0
        
            if self.rect.x <0 or self.rect.x>=width or self.rect.y<0 or self.rect.y>=height:
                self.isAlive = False
                return

        
