import pygame
import sys
from grid import Grid
from constants import *
from algorithms.bfs import bfs

# Converts mouse position into grid coordinates
def get_clicked_pos(pos):
    x, y = pos
    row = y // CELL_SIZE
    col = x // CELL_SIZE
    return row, col

# Draws control panel
def draw_panel(screen):
    panel_rect = pygame.Rect(GRID_WIDTH, 0, PANEL_WIDTH, HEIGHT)
    pygame.draw.rect(screen, BLACK, panel_rect)

    # Fonts
    font = pygame.font.SysFont(None, 30)
    small_font = pygame.font.SysFont(None, 24)

    # Title
    title = font.render("Controls", True, WHITE)
    screen.blit(title, (GRID_WIDTH + 50, 20))

    # Algorithm text
    algorithm_text = small_font.render("Algorithm: BFS", True, WHITE)
    screen.blit(algorithm_text, (GRID_WIDTH + 15, 80))

    # Start button
    start_button = pygame.Rect(GRID_WIDTH + 20, 140, 160, 40)
    pygame.draw.rect(screen, GRAY, start_button)

    start_text = small_font.render("Start", True, BLACK)
    screen.blit(start_text, (GRID_WIDTH + 72, 152))

    # Reset button
    reset_button = pygame.Rect(GRID_WIDTH + 20, 200, 160, 40)
    pygame.draw.rect(screen, GRAY, reset_button)

    reset_text = small_font.render("Reset", True, BLACK)
    screen.blit(reset_text, (GRID_WIDTH + 70, 212))

    # Temporary controls text
    controls_text = small_font.render("Space = BFS", True, WHITE)
    screen.blit(controls_text, (GRID_WIDTH + 20, 300))
    clear_text = small_font.render("C = Reset", True, WHITE)
    screen.blit(clear_text, (GRID_WIDTH + 20, 330))

    return start_button, reset_button

# Draws the current frame
def draw(screen, grid):
    screen.fill(BLACK)
    grid.draw(screen)
    start_button, reset_button = draw_panel(screen)
    pygame.display.flip()
    return start_button, reset_button

def main():
    pygame.init()

    # Creates window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")
    
    clock = pygame.time.Clock()

    # Initializes grid
    grid = Grid()

    running = True

    while running:
        clock.tick(FPS)

        # Draws frame first
        start_button, reset_button = draw(screen, grid)

        # Handles events
        for event in pygame.event.get():

            # Quit event
            if event.type == pygame.QUIT:
                running = False

            # Mouse click handling
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                pos = pygame.mouse.get_pos()

                # Check button clicks first
                if start_button.collidepoint(pos):
                    bfs(grid, lambda: draw(screen, grid))

                elif reset_button.collidepoint(pos):
                    grid.reset()

                else:
                    # Grid interaction
                    row, col = get_clicked_pos(pos)

                    if 0 <= row < ROWS and 0 <= col < COLS:

                        if grid.start is None:
                            grid.set_start(row, col)

                        elif grid.end is None and (row, col) != grid.start:
                            grid.set_end(row, col)

                        elif (row, col) != grid.start and (row, col) != grid.end:
                            grid.toggle_wall(row, col)

            # Right click logic
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                if 0 <= row < ROWS and 0 <= col < COLS:
                    grid.clear_cell(row, col)

            # Keyboard shortcuts (temporary)
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    bfs(grid, lambda: draw(screen, grid))

                if event.key == pygame.K_c:
                    grid.reset()

        # Final render
        draw(screen, grid)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()