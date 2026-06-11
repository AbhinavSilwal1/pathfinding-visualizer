import pygame
from constants import *

# Draws control panel and returns UI hitboxes
def draw_panel(screen, grid, selected_algorithm, dropdown_open, slider_x):
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
        algorithms = ["BFS", "DFS", "Dijkstra", "A*"]

        for i, algorithm in enumerate(algorithms):
            rect = pygame.Rect(GRID_WIDTH + 20, 130 + (i * 45), 160, 40)

            pygame.draw.rect(screen, WHITE, rect)

            text = small_font.render(algorithm, True, BLACK)
            screen.blit(text, (GRID_WIDTH + 40, 142 + (i * 45)))

            option_rects.append((rect, algorithm))

    # Speed slider
    speed_text = small_font.render("Speed", True, WHITE)
    screen.blit(speed_text, (GRID_WIDTH + 20, 320))

    slider_rect = pygame.Rect(GRID_WIDTH + 20, 350, 160, 6)
    pygame.draw.rect(screen, WHITE, slider_rect)

    knob_rect = pygame.Rect(slider_x - 6, 343, 12, 20)
    pygame.draw.rect(screen, GRAY, knob_rect)

    # Statistics panel
    stats_title = small_font.render("Statistics", True, WHITE)
    screen.blit(stats_title, (GRID_WIDTH + 20, 380))

    visited_text = small_font.render(f"Visited: {grid.visited_count}", True, WHITE)
    screen.blit(visited_text, (GRID_WIDTH + 20, 410))

    path_text = small_font.render(f"Path Length: {grid.path_length}", True, WHITE)
    screen.blit(path_text, (GRID_WIDTH + 20, 440))

    start_button = pygame.Rect(GRID_WIDTH + 20, 490, 160, 40)
    reset_button = pygame.Rect(GRID_WIDTH + 20, 550, 160, 40)

    pygame.draw.rect(screen, GRAY, start_button)
    pygame.draw.rect(screen, GRAY, reset_button)

    screen.blit(small_font.render("Start", True, BLACK), (GRID_WIDTH + 72, 502))
    screen.blit(small_font.render("Reset", True, BLACK), (GRID_WIDTH + 70, 562))

    return start_button, reset_button, dropdown_rect, option_rects, slider_rect, knob_rect

# Draws full frame
def draw(screen, grid, selected_algorithm, dropdown_open, slider_x):
    screen.fill(BLACK)
    grid.draw(screen)

    ui_elements = draw_panel(screen, grid, selected_algorithm, dropdown_open, slider_x)

    pygame.display.flip()

    return ui_elements