import os
import time
import sys

ALIVE = chr(0x2588) 
DEAD = ' '           

def create_map(rows, cols):
    return [[DEAD for _ in range(cols)] for _ in range(rows)]

def place_glider(grid, r, c):
    coords = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for dr, dc in coords:
        grid[r + dr][c + dc] = ALIVE

def count_neighbors_torus(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0: continue
            # Use modulo to wrap coordinates 
            if grid[(r + i) % rows][(c + j) % cols] == ALIVE:
                count += 1
    return count

def evolve(grid):
    rows, cols = len(grid), len(grid[0])
    new_grid = create_map(rows, cols)

    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors_torus(grid, r, c)
            
            if grid[r][c] == ALIVE:
                # Rule: Stay alive if 2 or 3 neighbors are alive
                new_grid[r][c] = ALIVE if neighbors in [2, 3] else DEAD
            else:
                # Rule: Become alive if exactly 3 neighbors
                new_grid[r][c] = ALIVE if neighbors == 3 else DEAD
    return new_grid

def display_map(grid, gen):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Generation: {gen}") # Displaying the # of generations
    print("-" * len(grid[0]))
    for row in grid:
        print("".join(row)) 
    print("-" * len(grid[0]))

def main():
    rows, cols = 20, 60
    world = create_map(rows, cols)
    generation = 0 # Initialize counter
    
    place_glider(world, 2, 2)
    
    try:
        while True: 
            display_map(world, generation)
            world = evolve(world) 
            generation += 1       # Increment generation count
            time.sleep(0.05)      # Map stays up for x seconds 
    except KeyboardInterrupt:
        print(f"\nStopped at Generation {generation}")

if __name__ == "__main__":
    main()