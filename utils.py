import pygame

background_colour = (23, 23, 23)
width, height = 550, 550
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')

class ScreenEffects:
    def __init__(self):
        self.image = pygame.Surface((width, height), flags=pygame.SRCALPHA)
        self.FadeAlpha = 0
        self.FadedOut = False
        self.FadedIn = False
    
    def Reset(self):
        self.FadedOut = False
        self.FadedIn = False
    
    def FadeEffect(self, direction:int):
        self.image.fill((0,0,0))
        self.image.set_alpha(self.FadeAlpha)

        if (direction==-1 and self.FadeAlpha<255) or (direction==1 and self.FadeAlpha>0):
            self.FadeAlpha -= direction
        elif direction==1 and self.FadeAlpha==0:
            self.FadedIn = True
        elif direction==-1 and self.FadeAlpha==255:
            self.FadedOut = True

        screen.blit(self.image, (0,0))


fx = ScreenEffects()