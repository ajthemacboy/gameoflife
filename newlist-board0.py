import pygame, sys, random, os

import layout2 as layout1


class GAME():
    def __init__(self, screen, x, y, cellSize):
        self.screen = screen
        self.x = x * cellSize
        self.y = y * cellSize
        self.cellSize = cellSize

    def drawCell(self, x, y):
        rect = pygame.Rect(self.cellSize * x, self.cellSize * y, self.cellSize, self.cellSize)  # Define rect for cell
        pygame.draw.rect(self.screen, (255, 0, 0), rect, 0)

    def drawLines(self):  # Iterate over each cell, jumping 16 each time, with 1 pixel for padding on the outside
        for indexX in range(0, self.x + 1, 16):
            pygame.draw.line(self.screen, (255, 255, 255), (indexX, 0), (indexX, self.y), 1)
        for indexY in range(0, self.y + 1, 16):
            pygame.draw.line(self.screen, (255, 255, 255), (0, indexY), (self.x, indexY), 1)


listB, listS, fps, frequency, x, y, padding, probability = layout1.launchRules()  # Start the UI as defined in the layout file and assign the values return

cellSize = 16
state = "place"  # Start in place mode
counter = frequency

pygame.init()
screen = pygame.display.set_mode((x * cellSize + 1,
                                  y * cellSize + cellSize + 1))  # Set the screen size to be big enough for the number of cells (x * cellSize by y * cellSize) and 1 pixel for padding on the outside
pygame.display.set_caption("Conway's Game of Life")

pygame.font.init()
font = pygame.font.SysFont('Consolas', 16)
placetext = font.render('Place cells - click to start', False, (255, 255, 255))  # Assign button labels to blit later
runtext = font.render('Simulating cells - click to pause', False, (0, 0, 0))

clock = pygame.time.Clock()

game = GAME(screen, x, y, cellSize)
board = [[0 for x in range(x)] for y in range(y)]
button = pygame.Rect(0, y * cellSize + 1, x * cellSize + 1, y * cellSize + cellSize)  # Define rect for button

for indexC in range(0 + padding, x - padding):
    for indexR in range(0 + padding, y - padding):
        board[indexR][indexC] = random.randint(0,
                                               probability) // probability  # Each cell has a 1 in probability chance of being alive

while True:
    while state == "place":
        screen.fill((0, 0, 0))
        event = pygame.event.poll()

        if event.type == pygame.QUIT:  # Exit program if window close button clicked
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if button.collidepoint(pygame.mouse.get_pos()):  # Check for button click
                state = "run"  # Change state if clicked

            pos = pygame.mouse.get_pos()  # Get mouse position if left mouse button is down
            if pos[1] <= y * cellSize:  # Only continue if the Y pos is above the button
                if board[(pos[1]) // cellSize][(pos[0]) // cellSize] == 1:  # Toggle button
                    board[(pos[1]) // cellSize][(pos[0]) // cellSize] = 0  # Calculate what cell the click was in
                else:
                    board[(pos[1]) // cellSize][(pos[0]) // cellSize] = 1

        for indexC in range(0, x):
            for indexR in range(0, y):
                if board[indexR][indexC] == 1:
                    game.drawCell(indexC, indexR)

        game.drawLines()  # Draw grid
        pygame.draw.rect(screen, (0, 0, 255), button)  # Draw button
        screen.blit(placetext, (2, y * cellSize + 2))  # Draw button text
        pygame.display.update()

    while state == "run":
        screen.fill((0, 0, 0))

        event = pygame.event.poll()
        if event.type == pygame.QUIT:  # Exit program if window close button clicked
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(pygame.mouse.get_pos()):  # Check for button click
                state = "place"  # Change state if clicked

        if counter >= frequency:
            boardNew = [[0 for x in range(x)] for y in range(y)]
            for indexC in range(0, x):
                for indexR in range(0, y):

                    west = board[indexR % y][(indexC - 1) % x]  # Get neighbors
                    east = board[indexR % y][(indexC + 1) % x]
                    south = board[(indexR + 1) % y][indexC % x]
                    north = board[(indexR - 1) % y][indexC % x]

                    northwest = board[(indexR - 1) % y][(indexC - 1) % x]
                    northeast = board[(indexR - 1) % y][(indexC + 1) % x]
                    southwest = board[(indexR + 1) % y][(indexC - 1) % x]
                    southeast = board[(indexR + 1) % y][(indexC + 1) % x]

                    total = north + south + east + west + northwest + northeast + southwest + southeast  # Count neighbors (0-8)

                    if board[indexR][indexC] == 1 and total in listS:
                        boardNew[indexR][indexC] = 1  # Decide if cell lives or dies
                    elif board[indexR][indexC] == 0 and total in listB:
                        boardNew[indexR][indexC] = 1

            board = boardNew
            counter = 0

        for indexC in range(0, x):  # Draw the cells
            for indexR in range(0, y):
                if board[indexR][indexC] == 1:
                    game.drawCell(indexC, indexR)

        game.drawLines()
        pygame.draw.rect(screen, (0, 255, 0), button)  # Draw button
        screen.blit(runtext, (2, y * cellSize + 2))  # Draw button text
        pygame.display.update()
        counter += 1

        clock.tick(fps)  # Frames per second
