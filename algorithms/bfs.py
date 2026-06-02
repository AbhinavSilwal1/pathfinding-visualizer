import pygame
from collections import deque

# Reconstructs the shortest path step-by-step
def reconstruct_path(parent, end, start, grid):
    current = end

    while current in parent:
        current = parent[current]

        if current != start:
            grid.mark_path(current[0], current[1])

        yield True

# BFS as a generator for step-by-step visualization
def bfs(grid):

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

        # Stops when target is found
        if current == end:
            yield from reconstruct_path(parent, end, start, grid)
            return

        # Explores neighbors
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

        # Yields control after each step
        yield True