import pygame, sys, random, os
import version03_load as layout

listB, listS, fps, freq, cellSize, x, y, padding, sparsity, paused = layout.load()

class GAME:
    def __init__(self, fps, cellSize, x, y, sparsity, paused):

        # Var setup
        self.fps = fps
        self.cellSize = cellSize
        self.x = x
        self.y = y
        self.sparsity = sparsity
        if paused:
            self.state = "place"
        else:
            self.state = "run"

        # Display setup
        pygame.init
        self.screen = pygame.display.set_mode((x * cellSize + 1, y * cellSize + 16 + 2))                                # Set the screen size to be big enough for the number of cells (x * cellSize by y * cellSize) and 1 pixel for padding on the outside
        pygame.display.set_caption("Conway's Game of Life")

        # Font setup
        pygame.font.init()
        self.font = pygame.font.SysFont('Consolas', 16)
        self.placetext = self.font.render('Place cells - click to start', False, (255, 255, 255))                       # Assign button labels to blit later
        self.runtext = self.font.render('Simulating cells - click to pause', False, (0, 0, 0))

        # Game setup
        self.clock = pygame.time.Clock()
        self.button = pygame.Rect(0, y * cellSize, x * cellSize + 1, y * cellSize + 16)                                 # Define rect for button
        self.board = [[0 for x in range(self.x)] for y in range(self.y)]

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

        elif self.button.collidepoint(pos):                                                                             # Button clicked
            if self.state == "place":
                self.state = "run"
            else:
                self.state = "place"

    def cellClicked(self, pos):
        if self.board[(pos[1]) // self.cellSize][(pos[0]) // self.cellSize] == 1:                                       # Toggle button
            self.board[(pos[1]) // self.cellSize][(pos[0]) // self.cellSize] = 0                                        # Calculate what cell the click was in
        else:
            self.board[(pos[1]) // self.cellSize][(pos[0]) // self.cellSize] = 1

    def drawBoard(self):
        for indexC in range(0, self.x):
            for indexR in range(0, self.y):
                if self.board[indexR][indexC] == 1:
                    self.drawCell(indexC, indexR)

        if self.state == "place":
            pygame.draw.rect(self.screen, (0, 0, 255), self.button)
            self.screen.blit(self.placetext, (2, y * self.cellSize + 2))
        elif self.state == "run":
            pygame.draw.rect(self.screen, (0, 255, 0), self.button)
            self.screen.blit(self.runtext, (2, y * self.cellSize + 2))

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
        if fps == None:
            fps = self.fps
        self.clock.tick(fps)

    def drawGrid(self):                                                                                                 # Iterate over each visual cell, jumping cellSize n each time, with 1 pixel for padding on the outside
        for indexX in range(0, (self.x * self.cellSize) + 1, self.cellSize):
            pygame.draw.line(self.screen, (255, 255, 255), (indexX, 0), (indexX, (self.y * self.cellSize)), 1)

        for indexY in range(0, (self.y * self.cellSize) + 1, self.cellSize):
            pygame.draw.line(self.screen, (255, 255, 255), (0, indexY), ((self.x * self.cellSize), indexY), 1)


game = GAME(fps, cellSize, x, y, sparsity, paused)
game.randomize()
counter = freq

if __name__ == "__main__":
    while True:
        while game.state == "place":
            game.clear()
            event = pygame.event.poll()

            if event.type == pygame.QUIT: sys.exit()                                                                    # Exit program if window close button clicked
            elif event.type == pygame.MOUSEBUTTONDOWN: game.clickEvent()

            game.drawBoard()

            pygame.display.update()
            game.tick(fps * 4)                                                                                          # More responsive cell placing

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
