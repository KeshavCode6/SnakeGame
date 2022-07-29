from utils import *
from grid import *
from snake import *
from ui import *
import sys

pygame.init()
def ClassicMode():
    grid = Grid(25)
    snake = Snake(grid)

    while True:
        clock.tick(90)
        screen.fill(background_colour)
        grid.Update()
        snake.Update()
        pygame.display.set_caption(f"Snake (Score: {snake.score})")
        
        if not snake.isAlive:
            return

        pygame.display.flip()

def GameModeSelector():
    fx.Reset()
    BackButton = Button((525, 25), "<-", (50, 50), textSize=15)
    Selector = GamemodeSifter({"Classic Mode": ClassicMode})
    MovingSnakeUI = MovingSnake()

    fade = False
    while True:
        screen.fill(background_colour)
        clock.tick(100)
        MovingSnakeUI.Update()
        Text("Select a gamemode", (275, 40), size=30)
        Text("High Score: 0", (150, 430), size=20, color=(210,210,210))
        Text("Last Score: 0", (400, 430), size=20, color=(210,210,210))

        BackButton.Update()
        Selector.Update()

        if not fx.FadedIn:
            fx.FadeEffect(1)

        if BackButton.pressed:
            fade = True
        
        if fade:
            if fx.FadedOut == False:
                fx.FadeEffect(-1)
            else:
                return
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()    

def MainMenu():
    fx.Reset()
    PlayButton = Button((275, 150), "Play")
    AboutButton = Button((275, 250), "About")
    SettingsButton = Button((275, 350), "Settings")
    QuitButton = Button((275, 450), "Quit")
    MovingSnakeUI = MovingSnake()
    fade = False

    while True:
        clock.tick(100)
        screen.fill(background_colour)

        MovingSnakeUI.Update()

        Text("Snake but CURSED", (275, 50), size=40)

        PlayButton.Update()
        AboutButton.Update()
        SettingsButton.Update()
        QuitButton.Update()

        if not fx.FadedIn:
            fx.FadeEffect(1)

        if PlayButton.pressed:
            fade = True

        if fade:
            if fx.FadedOut == False:
                fx.FadeEffect(-1)
            else:
                GameModeSelector() 
                break               

        if QuitButton.pressed:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        