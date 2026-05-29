import pygame
from constants import *

class Grid:
    def __init__(self):
        self.rows = ROWS
        self.cols = COLS
        self.cell_size = CELL_SIZE

    def draw(self, screen):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * self.cell_size
                y = row * self.cell_size

                pygame.draw.rect(
                    screen,
                    WHITE,
                    (x, y, self.cell_size, self.cell_size)
                )

                pygame.draw.rect(
                    screen,
                    GRAY,
                    (x, y, self.cell_size, self.cell_size),
                    1
                )