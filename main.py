import time
import os
import copy

def clear():
    # Clear the console (works on Replit and most terminals)
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    for row in grid:
        print(' '.join(['█' if cell else ' ' for cell in row]))

def count_neighbors(grid, x, y):
    neighbors = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            ni, nj = x + i, y + j
            if 0 <= ni < rows and 0 <= nj < cols:
                neighbors += grid[ni][nj]
    return neighbors

def next_generation(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = copy.deepcopy(grid)
    for i in range(rows):
        for j in range(cols):
            alive = grid[i][j]
            neighbors = count_neighbors(grid, i, j)
            if alive:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i][j] = 0
            else:
                if neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid

def main():
    # Example: Blinker pattern
    grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

    # Pad the grid for more space
    size = 10
    padded_grid = [[0]*size for _ in range(size)]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            padded_grid[i+3][j+3] = grid[i][j]
    grid = padded_grid

    generations = 20
    for gen in range(generations):
        clear()
        print(f"Generation {gen}")
        print_grid(grid)
        grid = next_generation(grid)
        time.sleep(0.5)

if __name__ == "__main__":
    main()
