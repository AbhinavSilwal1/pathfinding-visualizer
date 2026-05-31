import pygame
from constants import *

class Grid:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.cell_size = CELL_SIZE

        # 0 = empty, 1 = wall
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        self.start = None
        self.end = None

    def toggle_wall(self, row, col):
        self.grid[row][col] = 1 - self.grid[row][col]

    def set_start(self, row, col):
        self.start = (row, col)

    def set_end(self, row, col):
        self.end = (row, col)

    def clear_cell(self, row, col):
        self.grid[row][col] = 0

        if self.start == (row, col):
            self.start = None

        if self.end == (row, col):
            self.end = None

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size
                y = row * self.cell_size

                if (row, col) == self.start:
                    color = GREEN

                elif (row, col) == self.end:
                    color = RED

                elif self.grid[row][col] == 1:
                    color = DARK_GRAY

                else:
                    color = WHITE

                pygame.draw.rect(
                    screen,
                    color,
                    (x, y, self.cell_size, self.cell_size)
                )

                pygame.draw.rect(
                    screen,
                    GRAY,
                    (x, y, self.cell_size, self.cell_size),
                    1
                )