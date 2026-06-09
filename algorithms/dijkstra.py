import pygame
import heapq

# Reconstructs the shortest path step-by-step
def reconstruct_path(parent, end, start, grid):
    current = end

    while current in parent:
        current = parent[current]

        if current != start:
            grid.mark_path(current[0], current[1])

        yield True

# Dijkstra explores nodes using lowest distance first
def dijkstra(grid):

    start = grid.start
    end = grid.end

    if not start or not end:
        return

    priority_queue = [(0, start)]

    distances = {
        start: 0
    }

    parent = {}

    visited = set()

    while priority_queue:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        current_distance, current = heapq.heappop(priority_queue)

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

            if (
                0 <= r < grid.rows
                and 0 <= c < grid.cols
                and grid.grid[r][c] != 1
            ):

                new_distance = current_distance + 1

                if (
                    (r, c) not in distances
                    or new_distance < distances[(r, c)]
                ):

                    distances[(r, c)] = new_distance
                    parent[(r, c)] = current

                    heapq.heappush(
                        priority_queue,
                        (new_distance, (r, c))
                    )

        # Yields control after each step
        yield True