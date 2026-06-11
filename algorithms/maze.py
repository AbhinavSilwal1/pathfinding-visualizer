import random

def generate_maze(grid):
    rows, cols = grid.rows, grid.cols

    # Initializes all cells as walls first
    for r in range(rows):
        for c in range(cols):
            grid.grid[r][c] = 1

    # Directions: up, down, left, right (2-step for maze carving)
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def dfs(r, c):
        grid.grid[r][c] = 0

        random.shuffle(directions)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if in_bounds(nr, nc) and grid.grid[nr][nc] == 1:

                # Carve wall between
                grid.grid[r + dr // 2][c + dc // 2] = 0
                dfs(nr, nc)

    # Start from a safe odd coordinate
    start_r = random.randrange(0, rows, 2)
    start_c = random.randrange(0, cols, 2)

    dfs(start_r, start_c)

    # Restore start/end if they existed
    if grid.start:
        sr, sc = grid.start
        grid.grid[sr][sc] = 0

    if grid.end:
        er, ec = grid.end
        grid.grid[er][ec] = 0