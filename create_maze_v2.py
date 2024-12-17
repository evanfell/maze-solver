import numpy as np
from PIL import Image

def create_maze(width, height):
    # Create a grid of walls
    maze = np.ones((height, width), dtype=np.uint8) * 255

    # Initialize the stack for backtracking
    stack = [(1, 1)]

    while stack:
        x, y = stack.pop()

        # Mark the current cell as visited
        maze[y, x] = 0

        # Get a list of unvisited neighbors
        neighbors = []
        if x > 2 and maze[y, x - 2] == 255:
            neighbors.append((x - 2, y))
        if x < width - 2 and maze[y, x + 2] == 255:
            neighbors.append((x + 2, y))
        if y > 2 and maze[y - 2, x] == 255:
            neighbors.append((x, y - 2))
        if y < height - 2 and maze[y + 2, x] == 255:
            neighbors.append((x, y + 2))

        if neighbors:
            # Choose a random neighbor
            nx, ny = np.random.choice(neighbors)

            # Remove the wall between the current cell and the neighbor
            maze[ny, nx] = 0
            maze[(y + ny) // 2, (x + nx) // 2] = 0

            # Add the neighbor to the stack
            stack.append((nx, ny))

    return maze

# Create a maze of size 50x50
maze = create_maze(50, 50)

# Save the maze as an image
img = Image.fromarray(maze, 'L')
img.save('mazes/maze2.png')