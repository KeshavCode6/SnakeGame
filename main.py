from utils import *
from grid import *
from snake import *
from ui import *
import sys
pygame.init()


def Game():
    # Game Vars
    grid = Grid(25)
    snake = Snake(grid)

    # Main Menu Vars
    PlayButton = Button((270, 250), "Play")
    SettingsButton = Button((270, 350), "Settings")
    QuitButton = Button((270, 450), "Quit")
    MovingSnakeUI = MovingSnake()

    while True:
        # Main Menu
        screen.fill(background_colour)

        MovingSnakeUI.Update()

        Text("Snake but CURSED", (270, 50), size=40)
        Text("High Score: 0", (270, 120), size=20)
        Text("Score: 0", (270, 170), size=20)

        PlayButton.Update()
        SettingsButton.Update()
        QuitButton.Update()

        if PlayButton.pressed:
            # Starts Game If Pressed
            if fx.FadedOut == False:
                fx.FadeEffect(-1)
            else:
                fx.FadeEffect(1)
            
            if fx.FadedIn:
                fx.Reset()

                while True:
                    clock.tick(90)
                    pygame.display.set_caption(f"Snake (Score: {snake.score})")
                    if not snake.isAlive:
                        return

                    screen.fill(background_colour)
                    grid.Update()
                    snake.Update()
                    pygame.display.flip()

        if QuitButton.pressed:
            pygame.quit()
            sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
        


while True:
    Game()
