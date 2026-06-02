import pygame
import sys
from grid import Grid
from constants import *
from algorithms.bfs import bfs

# Converts mouse position into grid coordinates
def get_clicked_pos(pos):
    x, y = pos
    return y // CELL_SIZE, x // CELL_SIZE

# Draws control panel and returns button hitboxes
def draw_panel(screen):
    panel_rect = pygame.Rect(GRID_WIDTH, 0, PANEL_WIDTH, HEIGHT)
    pygame.draw.rect(screen, BLACK, panel_rect)

    font = pygame.font.SysFont(None, 30)
    small_font = pygame.font.SysFont(None, 24)

    title = font.render("Controls", True, WHITE)
    screen.blit(title, (GRID_WIDTH + 50, 20))

    algorithm_text = small_font.render("Algorithm: BFS", True, WHITE)
    screen.blit(algorithm_text, (GRID_WIDTH + 15, 80))

    start_button = pygame.Rect(GRID_WIDTH + 20, 140, 160, 40)
    reset_button = pygame.Rect(GRID_WIDTH + 20, 200, 160, 40)

    pygame.draw.rect(screen, GRAY, start_button)
    pygame.draw.rect(screen, GRAY, reset_button)

    screen.blit(small_font.render("Start", True, BLACK), (GRID_WIDTH + 72, 152))
    screen.blit(small_font.render("Reset", True, BLACK), (GRID_WIDTH + 70, 212))

    return start_button, reset_button

# Draws full frame
def draw(screen, grid):
    screen.fill(BLACK)
    grid.draw(screen)
    start_button, reset_button = draw_panel(screen)
    pygame.display.flip()
    return start_button, reset_button

def run_bfs(screen, grid):
    for _ in bfs(grid):
        draw(screen, grid)
        pygame.time.delay(30)

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")

    clock = pygame.time.Clock()
    grid = Grid()

    running = True

    while running:
        clock.tick(FPS)

        start_button, reset_button = draw(screen, grid)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()

                if start_button.collidepoint(pos):
                    run_bfs(screen, grid)

                elif reset_button.collidepoint(pos):
                    grid.reset()

                else:
                    row, col = get_clicked_pos(pos)

                    if 0 <= row < ROWS and 0 <= col < COLS:

                        if grid.start is None:
                            grid.set_start(row, col)

                        elif grid.end is None and (row, col) != grid.start:
                            grid.set_end(row, col)

                        elif (row, col) != grid.start and (row, col) != grid.end:
                            grid.toggle_wall(row, col)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                if 0 <= row < ROWS and 0 <= col < ROWS:
                    grid.clear_cell(row, col)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()