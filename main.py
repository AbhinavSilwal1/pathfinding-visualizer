import pygame
import sys
from grid import Grid
from visualizer import draw
from constants import *
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.dijkstra import dijkstra
from algorithms.a_star import astar
from algorithms.maze import generate_maze

# Converts mouse position into grid coordinates
def get_clicked_pos(pos):
    x, y = pos
    return (y - GRID_Y_OFFSET) // CELL_SIZE, x // CELL_SIZE

# Runs BFS animation step-by-step
def run_bfs(screen, grid, selected_algorithm, dropdown_open, slider_x, delay):
    grid.clear_visualization()
    for _ in bfs(grid):
        draw(screen, grid, selected_algorithm, dropdown_open, slider_x)
        pygame.time.delay(delay)

# Runs DFS animation step-by-step
def run_dfs(screen, grid, selected_algorithm, dropdown_open, slider_x, delay):
    grid.clear_visualization()
    for _ in dfs(grid):
        draw(screen, grid, selected_algorithm, dropdown_open, slider_x)
        pygame.time.delay(delay)

# Runs Dijkstra animation step-by-step
def run_dijkstra(screen, grid, selected_algorithm, dropdown_open, slider_x, delay):
    grid.clear_visualization()
    for _ in dijkstra(grid):
        draw(screen, grid, selected_algorithm, dropdown_open, slider_x)
        pygame.time.delay(delay)

# Runs A* animation step-by-step
def run_astar(screen, grid, selected_algorithm, dropdown_open, slider_x, delay):
    grid.clear_visualization()
    for _ in astar(grid):
        draw(screen, grid, selected_algorithm, dropdown_open, slider_x)
        pygame.time.delay(delay)

# Runs Maze generation
def run_maze(screen, grid, selected_algorithm, dropdown_open, slider_x, delay):
    grid.clear_visualization()
    generate_maze(grid)
    draw(screen, grid, selected_algorithm, dropdown_open, slider_x)
    pygame.time.delay(delay)

def main():
    pygame.init()

    # Initializes window and grid system
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pathfinding Visualizer")

    clock = pygame.time.Clock()
    grid = Grid()

    selected_algorithm = None
    dropdown_open = False

    slider_x = GRID_WIDTH + 100
    dragging_slider = False
    animation_delay = DEFAULT_DELAY

    running = True

    while running:
        clock.tick(FPS)

        # Draws frame and retrieves UI button hitboxes
        start_button, reset_button, maze_button, dropdown_rect, option_rects, slider_rect, knob_rect = draw(
            screen, 
            grid, 
            selected_algorithm, 
            dropdown_open,
            slider_x
        )

        # Event handling loop
        for event in pygame.event.get():

            # Exit application
            if event.type == pygame.QUIT:
                running = False

            # Handles left mouse interactions (UI + grid)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()

                # Starts dragging speed slider
                if knob_rect.collidepoint(pos):
                    dragging_slider = True

                # Opens/closes dropdown menu
                elif dropdown_rect.collidepoint(pos):
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
                        run_bfs(screen, grid, selected_algorithm, dropdown_open, slider_x, animation_delay)
                    elif selected_algorithm == "DFS":
                        run_dfs(screen, grid, selected_algorithm, dropdown_open, slider_x, animation_delay)
                    elif selected_algorithm == "Dijkstra":
                        run_dijkstra(screen, grid, selected_algorithm, dropdown_open, slider_x, animation_delay)
                    elif selected_algorithm == "A*":
                        run_astar(screen, grid, selected_algorithm, dropdown_open, slider_x, animation_delay)

                elif maze_button.collidepoint(pos):
                    run_maze(screen, grid, selected_algorithm, dropdown_open, slider_x, animation_delay)

                elif reset_button.collidepoint(pos):
                    grid.reset()
                    selected_algorithm = None
                    dropdown_open = False

                    slider_x = GRID_WIDTH + 100
                    dragging_slider = False
                    animation_delay = DEFAULT_DELAY

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

            # Stops dragging slider
            if event.type == pygame.MOUSEBUTTONUP:
                dragging_slider = False

            # Updates slider position while dragging
            if event.type == pygame.MOUSEMOTION and dragging_slider:
                slider_x = max(slider_rect.left, min(event.pos[0], slider_rect.right))
                percentage = ((slider_x - slider_rect.left) / slider_rect.width)
                animation_delay = int(MAX_DELAY - percentage * (MAX_DELAY - MIN_DELAY))

        # Supports click-and-drag wall placement
        if pygame.mouse.get_pressed()[0]:

            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)

            if 0 <= row < ROWS and 0 <= col < COLS:

                if (grid.start is not None and grid.end is not None and (row, col) != grid.start and (row, col) != grid.end):
                    grid.set_wall(row, col)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()