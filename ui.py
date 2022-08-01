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

            if pygame.mouse.get_pressed()[0] and fx.FadedIn:
                self.pressed = True
            else:
                self.pressed = False

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

class SelectorButton(Button):
    def __init__(self, position:tuple, text:str, size:tuple = (208, 81), textSize:int=30):
        super().__init__(position, text, size, textSize)
        self.sprite.fill((200,200,200))
        self.sprite.set_alpha(200)

class GamemodeSifter:
    def __init__(self, gamemodes:dict):
        self.Modes = {
            "Classic Mode":pygame.image.load("res\Icons\ClassicModeIcon.png"),
            "2 Player mode":pygame.image.load("res\Icons\ComingSoonIcon.png"),
            "Sussy Mode":pygame.image.load("res\Icons\ComingSoonIcon.png")
        }

        self.names = list(self.Modes.keys())
        self.images = list(self.Modes.values())
        self.currentMode = 0

        self.leftButton = SelectorButton((30, 225), "<", (40, 80))
        self.rightButton = SelectorButton((520, 225), ">", (40, 80))
        self.SelectButton = Button((275, 500), "Select")

        self.pressWaitTime = 1
        self.gamemodes = gamemodes

        self.selected = False
    def Draw(self):
        MainImage = pygame.transform.scale(self.Modes[self.names[1]], (200,200))
        MainImage.set_alpha(255)
        screen.blit(MainImage, (175, 125))
        
        if len(self.Modes) >= 2:
            LeftImage = self.Modes[self.names[0]]
            LeftImage.set_alpha(100)
            screen.blit(LeftImage, (60, 175))

        if len(self.Modes) >= 3:
            RightImage = self.Modes[self.names[2]]
            
            RightImage.set_alpha(100)
            screen.blit(RightImage, (390, 175))

        Text(f"{self.names[1]}", (275, 350), size=30)
        
    def Update(self):
        self.Draw()
        self.leftButton.Update()
        self.rightButton.Update()

        if self.names[1] in list(self.gamemodes.keys()):
            self.SelectButton.Update()

        self.HandleSifting()
    
    def ScrollRight(self):
        names = []
        names.append(self.names[len(self.names)-1])

        x = 0
        while x < len(self.names)-1:
            names.append(self.names[x])
            x+=1
        
        self.names = names

    def ScrollLeft(self):
        names = []

        x = 1
        while x < len(self.names):
            names.append(self.names[x])
            x+=1
        
        names.append(self.names[0])
        self.names = names

    def HandleSifting(self):
        if self.pressWaitTime < 0:
            if self.leftButton.pressed:
                self.ScrollLeft()
                self.pressWaitTime = 1
            
            if self.rightButton.pressed:
                self.ScrollRight()
                self.pressWaitTime = 1            
        else:
            self.pressWaitTime -= 0.05
        
        if self.SelectButton.pressed:
            self.gamemodes[self.names[1]]()
            self.selected = True
        
