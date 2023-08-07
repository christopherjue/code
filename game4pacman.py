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
        dx = pacman_x - ghost[0]
        dy = pacman_y - ghost[1]
        dist = max(abs(dx), abs(dy))
        if dist > 0:
            ghost[0] += int(dx / dist)
            ghost[1] += int(dy / dist)

    # Collision detection with walls
    pacman_cell_x = pacman_x // cell_size
    pacman_cell_y = pacman_y // cell_size
    if maze[pacman_cell_y][pacman_cell_x] == 1:
        pacman_x -= pacman_speed
        pacman_y -= pacman_speed

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
