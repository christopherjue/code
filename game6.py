import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pac-Man")

# Define colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

# Set up Pac-Man
pacman_radius = 20
pacman_x = window_width // 2
pacman_y = window_height // 2
pacman_speed = 5
pacman_direction = "right"  # Starting direction

# Set up ghosts
ghost_radius = 15
ghosts = []
for _ in range(4):
    ghost_x = random.randint(0, window_width)
    ghost_y = random.randint(0, window_height)
    ghosts.append([ghost_x, ghost_y, 2, 2])

# Set up the maze
maze_width = 20
maze_height = 15
cell_size = 40
maze = [[random.choice([0, 1]) for _ in range(maze_width)] for _ in range(maze_height)]

# Game loop
running = True
clock = pygame.time.Clock()

def respawn_pacman():
    # Find the nearest available position to respawn
    min_distance = float("inf")
    nearest_x, nearest_y = None, None

    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 0:
                distance = ((x * cell_size) - pacman_x) ** 2 + ((y * cell_size) - pacman_y) ** 2
                if distance < min_distance:
                    min_distance = distance
                    nearest_x = x * cell_size
                    nearest_y = y * cell_size

    return nearest_x, nearest_y

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check for key press events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman_direction = "left"
            elif event.key == pygame.K_RIGHT:
                pacman_direction = "right"
            elif event.key == pygame.K_UP:
                pacman_direction = "up"
            elif event.key == pygame.K_DOWN:
                pacman_direction = "down"

    # Update Pac-Man's position based on the current direction
    if pacman_direction == "left":
        pacman_x -= pacman_speed
    elif pacman_direction == "right":
        pacman_x += pacman_speed
    elif pacman_direction == "up":
        pacman_y -= pacman_speed
    elif pacman_direction == "down":
        pacman_y += pacman_speed

    # Ghost movement
    for ghost in ghosts:
        possible_moves = []
        ghost_x, ghost_y, dx, dy = ghost

        if ghost_x - dx >= 0 and maze[ghost_y // cell_size][(ghost_x - dx) // cell_size] == 0:
            possible_moves.append((-1, 0))  # Left

        if ghost_x + dx < window_width and maze[ghost_y // cell_size][(ghost_x + dx) // cell_size] == 0:
            possible_moves.append((1, 0))  # Right

        if ghost_y - dy >= 0 and maze[(ghost_y - dy) // cell_size][ghost_x // cell_size] == 0:
            possible_moves.append((0, -1))  # Up

        if ghost_y + dy < window_height and maze[(ghost_y + dy) // cell_size][ghost_x // cell_size] == 0:
            possible_moves.append((0, 1))  # Down

        if possible_moves:
            dx, dy = random.choice(possible_moves)

        ghost[0] += dx
        ghost[1] += dy

    # Collision detection with walls
    pacman_cell_x = pacman_x // cell_size
    pacman_cell_y = pacman_y // cell_size
    if maze[pacman_cell_y][pacman_cell_x] == 1:
        pacman_x, pacman_y = respawn_pacman()

    # Wrap Pac-Man's position to the opposite side of the screen
    pacman_x = (pacman_x + window_width) % window_width
    pacman_y = (pacman_y + window_height) % window_height

    # Clear the screen
    window.fill(BLACK)

    # Draw the maze
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                pygame.draw.rect(window, BLUE, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Draw Pac-Man
    pygame.draw.circle(window, YELLOW, (pacman_x, pacman_y), pacman_radius)

    # Draw ghosts
    for ghost in ghosts:
        pygame.draw.circle(window, WHITE, (ghost[0], ghost[1]), ghost_radius)

    # Update the display
    pygame.display.flip()
    clock.tick(30)

# Quit the game
pygame.quit()
