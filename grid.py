import pygame
from constants import *

class Grid:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.cell_size = CELL_SIZE

        # 0 = empty, 1 = wall
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

    def toggle_wall(self, row, col):
        self.grid[row][col] = 1 - self.grid[row][col]

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size
                y = row * self.cell_size

                color = WHITE if self.grid[row][col] == 0 else (50, 50, 50)

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