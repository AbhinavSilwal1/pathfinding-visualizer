import pygame
from constants import *

class Grid:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.cell_size = CELL_SIZE

        # Grid representation; 0 = empty cell, 1 = wall
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Start and end nodes
        self.start = None
        self.end = None
        self.visited = set()
        self.path = set()

    # Toggles wall state
    def toggle_wall(self, row, col):
        self.grid[row][col] = 1 - self.grid[row][col]

    # Sets a cell as a wall
    def set_wall(self, row, col):
        self.grid[row][col] = 1

    # Sets start node
    def set_start(self, row, col):
        self.start = (row, col)

    # Sets end node
    def set_end(self, row, col):
        self.end = (row, col)

    # Clears a cell and resets start/end if needed
    def clear_cell(self, row, col):
        self.grid[row][col] = 0

        if self.start == (row, col):
            self.start = None

        if self.end == (row, col):
            self.end = None

    # Marks a node as visited
    def mark_visited(self, row, col):
        self.visited.add((row, col))

    # Marks a node as part of the path
    def mark_path(self, row, col):
        self.path.add((row, col))

    # Clears previous algorithm visualization
    def clear_visualization(self):
        self.visited.clear()
        self.path.clear()

    # Resets entire grid state
    def reset(self):
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.start = None
        self.end = None
        self.visited.clear()
        self.path.clear()

    # Draws grid
    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):

                x = col * self.cell_size
                y = row * self.cell_size

                # Chooses cell color
                if (row, col) == self.start:
                    color = GREEN

                elif (row, col) == self.end:
                    color = RED

                elif (row, col) in self.path:
                    color = YELLOW

                elif (row, col) in self.visited:
                    color = BLUE

                elif self.grid[row][col] == 1:
                    color = DARK_GRAY

                else:
                    color = WHITE

                # Draws cell
                pygame.draw.rect(
                    screen,
                    color,
                    (x, y, self.cell_size, self.cell_size)
                )

                # Draws grid lines
                pygame.draw.rect(
                    screen,
                    GRAY,
                    (x, y, self.cell_size, self.cell_size),
                    1
                )