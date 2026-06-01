import pygame
from collections import deque

# Reconstructs the shortest path
def reconstruct_path(parent, end, start, grid, draw_callback):

    current = end

    while current in parent:

        current = parent[current]

        if current != start:
            grid.mark_path(current[0], current[1])

        draw_callback()
        pygame.time.delay(50)

# BFS explores nodes level by level from start
def bfs(grid, draw_callback):

    start = grid.start
    end = grid.end

    if not start or not end:
        return

    queue = deque([start])
    visited = set([start])

    parent = {}

    while queue:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        current = queue.popleft()
        row, col = current

        if current != start and current != end:
            grid.mark_visited(row, col)

        # Stops if we reach the end
        if current == end:
            reconstruct_path(parent, end, start, grid, draw_callback)
            break

        # Checks neighbors (up, down, left, right)
        neighbors = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        for r, c in neighbors:

            if 0 <= r < grid.rows and 0 <= c < grid.cols:

                if (r, c) not in visited and grid.grid[r][c] != 1:
                    queue.append((r, c))
                    visited.add((r, c))
                    parent[(r, c)] = (row, col)

        # Visual update callback (redraws screen)
        draw_callback()

        pygame.time.delay(30)