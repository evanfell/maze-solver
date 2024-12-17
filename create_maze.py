from PIL import Image, ImageDraw
import random

# Maze dimensions
width = 100
height = 100
cell_size = 1

# Create a new image with a white background
img = Image.new("RGB", (width * cell_size, height * cell_size), "white")
draw = ImageDraw.Draw(img)

# Generate the maze using a randomized Prim's algorithm
maze = [[1 for _ in range(width)] for _ in range(height)]  # 1 represents walls
visited = [[False for _ in range(width)] for _ in range(height)]
walls = []

def add_walls(x, y):
    if x > 0 and not visited[y][x - 1]:
        walls.append((x, y, x - 1, y))
    if x < width - 1 and not visited[y][x + 1]:
        walls.append((x, y, x + 1, y))
    if y > 0 and not visited[y - 1][x]:
        walls.append((x, y, x, y - 1))
    if y < height - 1 and not visited[y + 1][x]:
        walls.append((x, y, x, y + 1))

# Start with a random cell
x, y = random.randint(0, width - 1), random.randint(0, height - 1)
visited[y][x] = True
add_walls(x, y)

while walls:
    wall = random.choice(walls)
    x1, y1, x2, y2 = wall
    if not visited[y2][x2]:
        maze[y1][x1] = 0  # Remove wall
        maze[y2][x2] = 0
        visited[y2][x2] = True
        add_walls(x2, y2)
    walls.remove(wall)

# Draw the maze
for y in range(height):
    for x in range(width):
        if maze[y][x] == 1:
            draw.rectangle(
                (x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size),
                fill="black"
            )

# Save the image
img.save("mazes/maze1.png")