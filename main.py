import pygame
import sys
from grid import Grid
from constants import *
from algorithms.bfs import bfs
from algorithms.dfs import dfs

# Converts mouse position into grid coordinates
def get_clicked_pos(pos):
    x, y = pos
    return y // CELL_SIZE, x // CELL_SIZE

# Draws control panel and returns button hitboxes
def draw_panel(screen, selected_algorithm, dropdown_open):
    panel_rect = pygame.Rect(GRID_WIDTH, 0, PANEL_WIDTH, HEIGHT)
    pygame.draw.rect(screen, BLACK, panel_rect)

    font = pygame.font.SysFont(None, 30)
    small_font = pygame.font.SysFont(None, 24)

    title = font.render("Controls", True, WHITE)
    screen.blit(title, (GRID_WIDTH + 50, 20))

    # Dropdown menu
    dropdown_rect = pygame.Rect(GRID_WIDTH + 20, 80, 160, 40)
    pygame.draw.rect(screen, GRAY, dropdown_rect)

    label = selected_algorithm if selected_algorithm else "<Select Algorithm>"
    dropdown_text = small_font.render(label, True, BLACK)
    screen.blit(dropdown_text, (GRID_WIDTH + 22, 92))

    option_rects = []

    if dropdown_open:
        algorithms = ["BFS", "DFS"]

        for i, algorithm in enumerate(algorithms):
            rect = pygame.Rect(GRID_WIDTH + 20, 120 + (i * 40), 160, 40)

            pygame.draw.rect(screen, WHITE, rect)

            text = small_font.render(algorithm, True, BLACK)
            screen.blit(text, (GRID_WIDTH + 40, 132 + (i * 40)))

            option_rects.append((rect, algorithm))

    start_button = pygame.Rect(GRID_WIDTH + 20, 220, 160, 40)
    reset_button = pygame.Rect(GRID_WIDTH + 20, 280, 160, 40)

    pygame.draw.rect(screen, GRAY, start_button)
    pygame.draw.rect(screen, GRAY, reset_button)

    screen.blit(small_font.render("Start", True, BLACK), (GRID_WIDTH + 72, 232))
    screen.blit(small_font.render("Reset", True, BLACK), (GRID_WIDTH + 70, 292))

    return start_button, reset_button, dropdown_rect, option_rects

# Draws full frame
def draw(screen, grid, selected_algorithm, dropdown_open):
    screen.fill(BLACK)
    grid.draw(screen)

    start_button, reset_button, dropdown_rect, option_rects = draw_panel(
        screen,
        selected_algorithm,
        dropdown_open
    )

    pygame.display.flip()

    return start_button, reset_button, dropdown_rect, option_rects

# Runs BFS animation step-by-step
def run_bfs(screen, grid, selected_algorithm, dropdown_open):
    grid.clear_visualization()
    for _ in bfs(grid):
        draw(screen, grid, selected_algorithm, dropdown_open)
        pygame.time.delay(30)

# Runs DFS animation step-by-step
def run_dfs(screen, grid, selected_algorithm, dropdown_open):
    grid.clear_visualization()
    for _ in dfs(grid):
        draw(screen, grid, selected_algorithm, dropdown_open)
        pygame.time.delay(30)

def main():
    pygame.init()

    # Initializes window and grid system
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")

    clock = pygame.time.Clock()
    grid = Grid()

    selected_algorithm = None
    dropdown_open = False

    running = True

    while running:
        clock.tick(FPS)

        # Draws frame and retrieves UI button hitboxes
        start_button, reset_button, dropdown_rect, option_rects = draw(
            screen,
            grid,
            selected_algorithm,
            dropdown_open
        )

        # Event handling loop
        for event in pygame.event.get():

            # Exit application
            if event.type == pygame.QUIT:
                running = False

            # Handles left mouse interactions (UI + grid)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                # Opens/closes dropdown menu
                if dropdown_rect.collidepoint(pos):
                    dropdown_open = not dropdown_open

                # Selects an algorithm
                else:
                    for rect, algorithm in option_rects:

                        if rect.collidepoint(pos):
                            selected_algorithm = algorithm
                            dropdown_open = False

                # UI button interactions
                if start_button.collidepoint(pos):

                    if selected_algorithm == "BFS":
                        run_bfs(screen, grid, selected_algorithm, dropdown_open)
                    elif selected_algorithm == "DFS":
                        run_dfs(screen, grid, selected_algorithm, dropdown_open)

                elif reset_button.collidepoint(pos):
                    grid.reset()
                    selected_algorithm = None
                    dropdown_open = False

                # Grid interaction (only if not clicking UI)
                else:
                    row, col = get_clicked_pos(pos)

                    if 0 <= row < ROWS and 0 <= col < COLS:

                        # Sets start node first click
                        if grid.start is None:
                            grid.set_start(row, col)

                        # Sets end node second click
                        elif grid.end is None and (row, col) != grid.start:
                            grid.set_end(row, col)

                        # Toggles walls after start/end nodes are set
                        elif (row, col) != grid.start and (row, col) != grid.end:
                            grid.toggle_wall(row, col)

            # Handles right click to clear cells
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos)

                if 0 <= row < ROWS and 0 <= col < COLS:
                    grid.clear_cell(row, col)

        # Supports click-and-drag wall placement
        if pygame.mouse.get_pressed()[0]:

            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)

            if 0 <= row < ROWS and 0 <= col < COLS:

                if (
                    grid.start is not None
                    and grid.end is not None
                    and (row, col) != grid.start
                    and (row, col) != grid.end
                ):
                    grid.set_wall(row, col)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()