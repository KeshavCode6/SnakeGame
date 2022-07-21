import pygame, random, sys

pygame.init()

background_colour = (23, 23, 23)
width, height = 550, 550
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')

def Text(msg:str, position:tuple, color:tuple=(255,255,255), size:int=50):
    font = pygame.font.Font('res/Text/Font.ttf', size)
    text = font.render(msg, True, color)

    rect = text.get_rect()

    rect.center = position

    screen.blit(text, rect)

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
                self.isAlive = False
                pygame.quit()

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

            i = len(self.tails)-1

            while i > 0:
                self.tails[i].topleft = self.tails[i-1].topleft
                i-=1
 
            self.rect.x += self.velocity[0]*self.grid.cellSize
            self.rect.y += self.velocity[1]*self.grid.cellSize

            if self.rect.x <0 or self.rect.x>width or self.rect.y<0 or self.rect.y>height:
                self.isAlive = False
                return
            
            self.CheckForSelfCollision()

            self.nextMove = 0

        

grid = Grid(25)
snake = Snake(grid)

def MainMenu():
    while True:
        screen.fill(background_colour)

        Text("Snake but CURSED", (250, 50), size=40)

        Text("Play", (60, 150), size=30)
        Text("Coming Soon?", (150, 250), size=30)
        Text("Quit", (60, 350), size=30)

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
