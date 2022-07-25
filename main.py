from utils import *
from grid import *
from snake import *
from ui import *
import sys
pygame.init()


grid = Grid(25)
snake = Snake(grid)

def MainMenu():
    PlayButton = Button((270, 250), "Play")
    SettingsButton = Button((270, 350), "Settings")
    QuitButton = Button((270, 450), "Quit")

    MovingSnakeUI = MovingSnake()

    while True:
        screen.fill(background_colour)

        MovingSnakeUI.Update()

        Text("Snake but CURSED", (270, 50), size=40)
        Text("High Score: 0", (270, 120), size=20)
        Text("Score: 0", (270, 170), size=20)

        PlayButton.Update()
        SettingsButton.Update()
        QuitButton.Update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        

def GameLoop():
    grid.__init__(25)
    snake.__init__(grid)
    pygame.display.set_mode((width, height))

    while True:
        clock.tick(90)
        pygame.display.set_caption(f"Snake (Score: {snake.score})")
        if not snake.isAlive:
            return

        screen.fill(background_colour)
        grid.Update()
        snake.Update()
        pygame.display.flip()


while True:
    MainMenu()
    GameLoop()
