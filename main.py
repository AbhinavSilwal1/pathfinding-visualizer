import pygame
import sys
from grid import Grid
from constants import *

def get_clicked_pos(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")

    clock = pygame.time.Clock()

    grid = Grid()

    running = True

    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Left Click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                if 0 <= row < ROWS and 0 <= col < COLS:

                    if grid.start is None:
                        grid.set_start(row, col)

                    elif grid.end is None and (row, col) != grid.start:
                        grid.set_end(row, col)

                    elif (row, col) != grid.start and (row, col) != grid.end:
                        grid.toggle_wall(row, col)

            # Right Click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                if 0 <= row < ROWS and 0 <= col < COLS:
                    grid.clear_cell(row, col)

        screen.fill(BLACK)

        grid.draw(screen)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()