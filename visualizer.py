import pygame
from constants import *

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
        algorithms = ["BFS", "DFS", "Dijkstra", "A*"]

        for i, algorithm in enumerate(algorithms):
            rect = pygame.Rect(GRID_WIDTH + 20, 130 + (i * 45), 160, 40)
            
            pygame.draw.rect(screen, WHITE, rect)

            text = small_font.render(algorithm, True, BLACK)
            screen.blit(text, (GRID_WIDTH + 40, 142 + (i * 45)))

            option_rects.append((rect, algorithm))

    start_button = pygame.Rect(GRID_WIDTH + 20, 350, 160, 40)
    reset_button = pygame.Rect(GRID_WIDTH + 20, 410, 160, 40)

    pygame.draw.rect(screen, GRAY, start_button)
    pygame.draw.rect(screen, GRAY, reset_button)

    screen.blit(small_font.render("Start", True, BLACK), (GRID_WIDTH + 72, 362))
    screen.blit(small_font.render("Reset", True, BLACK), (GRID_WIDTH + 70, 422))

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