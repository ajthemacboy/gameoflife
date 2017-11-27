import pygame, sys, random, os, csv, time, numpy
from PIL import Image
import final04_load as layout





class GAME:
    def __init__(self, fps, cellSize, x, y, sparsity, paused, restoreFile):

        # Var setup
        self.fps = fps
        self.cellSize = cellSize
        self.x = x
        self.y = y
        self.sparsity = sparsity
        if paused:
            self.state = "pause"
        else:
            self.state = "run"
        self.restoreFile = restoreFile

        self.lastState = "pause"

        # Display setup
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init
        self.screen = pygame.display.set_mode((x * cellSize + 1, y * cellSize + 48 + 1), 0, 8)                                # Set the screen size to be big enough for the number of cells (x * cellSize by y * cellSize) and 1 pixel for padding on the outside
        pygame.display.set_caption("Conway's Game of Life")

        # Font setup
        pygame.font.init()
        self.font = pygame.font.SysFont('Consolas', 16)

        # Game setup
        self.clock = pygame.time.Clock()
        self.board = [[0 for x in range(self.x)] for y in range(self.y)]
        self.buttons()


    def buttons(self):                                                                                                  # Create class for this outside of game class?

        # Pause/run button
        self.buttonState = pygame.Rect(0, self.y * self.cellSize, (self.x * self.cellSize) / 2, 16)
        self.textStatePause = self.font.render('Run', False, (255, 255, 255))
        self.textStateRun = self.font.render('Pause', False, (255, 255, 255))

        # Menu button
        self.buttonMenu = pygame.Rect((self.x * self.cellSize) / 2, self.y * self.cellSize, (self.x * self.cellSize) / 2, 16)
        self.textMenu = self.font.render('Menu', False, (255, 255, 255))

        # Dump button
        self.buttonDump = pygame.Rect(0, self.y * self.cellSize + 16, (self.x * self.cellSize) / 2, 16)
        self.textDump = self.font.render('Dump', False, (255, 255, 255))

        # Restore button
        self.buttonRestore = pygame.Rect((self.x * self.cellSize) / 2, self.y * self.cellSize + 16, (self.x * self.cellSize) / 2, 16)
        self.textRestore = self.font.render('Restore', False, (255, 255, 255))

        # Randomize button
        self.buttonRandomize = pygame.Rect(0, self.y * self.cellSize + 32, (self.x * self.cellSize) / 2, 16)
        self.textRandomize = self.font.render('Randomize', False, (255, 255, 255))

        # Clear button
        self.buttonClear = pygame.Rect((self.x * self.cellSize) / 2, self.y * self.cellSize + 32, (self.x * self.cellSize) / 2, 16)
        self.textClear = self.font.render('Clear', False, (255, 255, 255))

    def randomize(self):
        if self.sparsity != 0:
            for indexC in range(0 + padding, self.x - padding):
                for indexR in range(0 + padding, self.y - padding):
                    self.board[indexR][indexC] = random.randint(0, self.sparsity) // self.sparsity                      # Each cell has a 1 in probability n chance of starting alive


    def clear(self):
        self.screen.fill((0, 0, 0))


    def clickEvent(self):
        pos = pygame.mouse.get_pos()

        if pos[1] < self.y * self.cellSize:                                                                             # If click was above buttons
            self.cellClicked(pos)

        # Pause/run button
        elif self.buttonState.collidepoint(pos):                                                                        # Button clicked
            if self.state == "pause":
                self.state = "run"
            else:
                self.state = "pause"

        # Menu button
        elif self.buttonMenu.collidepoint(pos):                                                                         # Button clicked
            self.lastState = self.state
            self.drawBoard()
            self.state = "setup"

        # Dump button
        elif self.buttonDump.collidepoint(pos):
            array = numpy.array(self.board).astype('uint8')
            img = Image.fromarray(array * 255, "L")
            img.save("GoL_Dump_{}.bmp".format(time.strftime("%m-%d-%y_%H-%M-%S")))

        # Restore button
        elif self.buttonRestore.collidepoint(pos) and self.restoreFile:
            array = numpy.array(Image.open(self.restoreFile)).astype('uint8') / 255
            self.board = array.tolist()
            self.updateBoard()

        # Randomize button
        elif self.buttonRandomize.collidepoint(pos):
            self.randomize()

        # Clear button
        elif self.buttonClear.collidepoint(pos):
            self.board = [[0 for x in range(self.x)] for y in range(self.y)]

    def cellClicked(self, pos):
        if self.board[(pos[1]) // self.cellSize][(pos[0]) // self.cellSize] == 1:                                       # Toggle button
            self.board[(pos[1]) // self.cellSize][(pos[0]) // self.cellSize] = 0                                        # Calculate what cell the click was in
        else:
            self.board[(pos[1]) // self.cellSize][(pos[0]) // self.cellSize] = 1


    def drawBoard(self):

        # Board grid
        for indexC in range(0, self.x):
            for indexR in range(0, self.y):
                if self.board[indexR][indexC] == 1:
                    self.drawCell(indexC, indexR)

        # Pause/run button
        if self.state == "pause":
            pygame.draw.rect(self.screen, (85, 139, 47), self.buttonState)
            self.screen.blit(self.textStatePause, (4, y * self.cellSize + 1))
        elif self.state == "run":
            pygame.draw.rect(self.screen, (198, 40, 40), self.buttonState)
            self.screen.blit(self.textStateRun, (4, y * self.cellSize + 1))

        # Menu button
        pygame.draw.rect(self.screen, (106, 27, 154), self.buttonMenu)
        self.screen.blit(self.textMenu, ((self.x * self.cellSize) / 2 + 4, y * self.cellSize + 1))

        # Dump button
        pygame.draw.rect(self.screen, (21, 101, 192), self.buttonDump)
        self.screen.blit(self.textDump, (4, y * self.cellSize + 17))

        # Restore button
        if self.restoreFile:
            pygame.draw.rect(self.screen, (0, 131, 143), self.buttonRestore)
        else:
            pygame.draw.rect(self.screen, (63, 63, 63), self.buttonRestore)
        self.screen.blit(self.textRestore, ((self.x * self.cellSize) / 2 + 4, y * self.cellSize + 17))

        # Randomize button
        pygame.draw.rect(self.screen, (192, 202, 51), self.buttonRandomize)
        self.screen.blit(self.textRandomize, (4, y * self.cellSize + 34))

        # Clear button
        pygame.draw.rect(self.screen, (109, 76, 65), self.buttonClear)
        self.screen.blit(self.textClear, ((self.x * self.cellSize) / 2 + 4, y * self.cellSize + 34))

        self.drawGrid()


    def drawCell(self, x, y):
        rect = pygame.Rect(self.cellSize * x, self.cellSize * y, self.cellSize, self.cellSize)                          # Define rect for cell
        pygame.draw.rect(self.screen, (255, 0, 0), rect, 0)


    def updateBoard(self):
        boardNew = [[0 for x in range(self.x)] for y in range(self.y)]

        for indexC in range(0, self.x):
            for indexR in range(0, self.y):

                total = \
                    self.board[indexR % self.y][(indexC - 1) % self.x] \
                    + self.board[indexR % self.y][(indexC + 1) % self.x] \
                    + self.board[(indexR + 1) % self.y][indexC % self.x] \
                    + self.board[(indexR - 1) % self.y][indexC % self.x] \
                    + self.board[(indexR - 1) % self.y][(indexC - 1) % self.x] \
                    + self.board[(indexR - 1) % self.y][(indexC + 1) % self.x] \
                    + self.board[(indexR + 1) % self.y][(indexC - 1) % self.x] \
                    + self.board[(indexR + 1) % self.y][(indexC + 1) % self.x]

                if self.board[indexR][indexC] == 1 and total in listS:
                    boardNew[indexR][indexC] = 1                                                                        # Decide if cell lives or dies
                elif self.board[indexR][indexC] == 0 and total in listB:
                    boardNew[indexR][indexC] = 1

        self.board = boardNew


    def tick(self, fps=None):
        if fps is None:
            fps = self.fps
        self.clock.tick(fps)


    def drawGrid(self):                                                                                                 # Iterate over each visual cell, jumping cellSize n each time, with 1 pixel for padding on the outside
        for indexX in range(0, (self.x * self.cellSize) + 1, self.cellSize):
            pygame.draw.line(self.screen, (255, 255, 255), (indexX, 0), (indexX, (self.y * self.cellSize)), 1)

        for indexY in range(0, (self.y * self.cellSize) + 1, self.cellSize):
            pygame.draw.line(self.screen, (255, 255, 255), (0, indexY), ((self.x * self.cellSize), indexY), 1)

        # Lines along left and right sides
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.y * self.cellSize), (0, self.y * self.cellSize + 100))
        pygame.draw.line(self.screen, (255, 255, 255), (self.x * self.cellSize, self.y * self.cellSize), (self.x * self.cellSize, self.y * self.cellSize + 100))

        # 1st, 2nd, and 3rd horizontal lines between buttons
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.y * self.cellSize + 16), (self.x * self.cellSize, self.y * self.cellSize + 16))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.y * self.cellSize + 32), (self.x * self.cellSize, self.y * self.cellSize + 32))
        pygame.draw.line(self.screen, (255, 255, 255), (0, self.y * self.cellSize + 48), (self.x * self.cellSize, self.y * self.cellSize + 48))

        # Vertical line between buttons
        pygame.draw.line(self.screen, (255, 255, 255), ((self.x * self.cellSize) / 2, self.y * self.cellSize), ((self.x * self.cellSize) / 2, self.y * self.cellSize + 100))




listB, listS, fps, freq, cellSize, x, y, padding, sparsity, paused, restoreFile = layout.load()
game = GAME(fps, cellSize, x, y, sparsity, paused, restoreFile)
game.randomize()
counter = freq

if __name__ == "__main__":
    while True:
        while game.state == "setup":
            listB, listS, fps, freq, cellSize, x, y, padding, sparsity, paused, restoreFile = layout.load(lockSize=True)
            game.listB = listB
            game.listS = listS
            game.fps = fps
            game.freq = freq
            game.cellSize = cellSize
            game.x = x
            game.y = y
            game.padding = padding
            game.sparsity = sparsity
            game.restoreFile = restoreFile

            game.state = game.lastState

        while game.state == "pause":
            game.clear()
            event = pygame.event.poll()

            if event.type == pygame.QUIT: sys.exit()                                                                    # Exit program if window close button clicked
            elif event.type == pygame.MOUSEBUTTONDOWN: game.clickEvent()

            game.drawBoard()

            pygame.display.update()

        while game.state == "run":
            game.clear()
            event = pygame.event.poll()

            if event.type == pygame.QUIT: sys.exit()                                                                    # Exit program if window close button clicked
            elif event.type == pygame.MOUSEBUTTONDOWN: game.clickEvent()

            if counter >= freq:
                game.updateBoard()
                counter = 0

            game.drawBoard()

            pygame.display.update()
            counter += 1
            game.tick()
