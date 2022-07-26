from turtle import position
import pygame
from utils import *

def Text(msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
    font = pygame.font.Font('res/Text/Font.ttf', size)
    text = font.render(msg, True, color)

    rect = text.get_rect()

    rect.center = position

    screen.blit(text, rect)

class Button:
    def __init__(self, position:tuple, text:str, size:tuple = (208, 81), textSize:int=30):
        self.position = position
        self.size = list(size)
        self.normalSize = size
        self.text = text
        self.textSize = textSize

        self.sprite = pygame.image.load("res/Text/Button.png")
        self.rect = self.sprite.get_rect()
        self.pressed = False

    def Draw(self):
        sprite = pygame.transform.smoothscale(self.sprite, self.size)

        self.rect = sprite.get_rect()
        self.rect.center = self.position


        screen.blit(sprite, self.rect)
        Text(self.text, self.rect.center, size=self.textSize)
    
    def HoverEffect(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.size[0] <  self.normalSize[0] + 10 and self.size[1] <  self.normalSize[1] + 10 :
                self.size[0] += 1
                self.size[1] += 1   

            if pygame.mouse.get_pressed()[0]:
                self.pressed = True

        else:
            if self.size[0] > self.normalSize[0] and self.size[1] >  self.normalSize[1]:
                self.size[0] -= 1
                self.size[1] -= 1        
    def Update(self):
        self.HoverEffect()
        self.Draw()

class MovingSnake:
    def __init__(self):
        self.position = [width/2,525]
        self.sprite = pygame.image.load("res/SnakeHead_Up.png")
        self.tail = pygame.image.load("res/SnakeBody.png")
        self.rect = self.sprite.get_rect()
        self.size = 5
    
    def Draw(self):
        self.rect.center = self.position
        screen.blit(self.sprite, self.rect)

        pos = self.rect.topleft[1]

        for x in range(self.size-1):
            screen.blit(self.tail, (self.rect.topleft[0], pos+((50*x)+50)))

    def Update(self):
        self.Draw()
        self.HandleMovement()

    def HandleMovement(self):
        self.position[1]-=1

        if self.position[1]+((50*(self.size-1))+50) < -25:
            self.position[1] = height+25

            if pygame.mouse.get_pos()[0]<25:
                self.position[0] = 25
            elif pygame.mouse.get_pos()[0]>525:
                self.position[0] = width-25
            else:
                self.position[0] = pygame.mouse.get_pos()[0]

class GamemodeSifter:
    def __init__(self, images:list, names:list):
        self.position = position

        for x in range(len(images)):
            images[x] = pygame.transform.scale(images[x], (400,300))

        self.images = images
        self.names = names

        self.currentImg = 0
    
    def Draw(self):
        screen.blit(self.images[self.currentImg], (75, 70))
        Text(self.names[self.currentImg], (275, 270), size=20)

    def Update(self):
        self.Draw()