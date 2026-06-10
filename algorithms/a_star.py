import pygame
from heapq import heappush, heappop

# Calculates Manhattan distance heuristic
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Reconstructs the shortest path step-by-step
def reconstruct_path(parent, end, start, grid):
    current = end

    while current in parent:
        current = parent[current]

        if current != start:
            grid.mark_path(current[0], current[1])

        yield True

# A* pathfinding algorithm
def astar(grid):

    start = grid.start
    end = grid.end

    if not start or not end:
        return

    open_set = []
    heappush(open_set, (0, start))

    g_score = {
        start: 0
    }

    parent = {}

    visited = set()

    while open_set:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        current = heappop(open_set)[1]

        if current in visited:
            continue

        visited.add(current)

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

                if grid.grid[r][c] == 1:
                    continue

                tentative_g = g_score[current] + 1

                if (
                    (r, c) not in g_score
                    or tentative_g < g_score[(r, c)]
                ):

                    g_score[(r, c)] = tentative_g

                    f_score = (
                        tentative_g
                        + heuristic((r, c), end)
                    )

                    heappush(
                        open_set,
                        (f_score, (r, c))
                    )

                    parent[(r, c)] = current

        # Yields control after each step
        yield True