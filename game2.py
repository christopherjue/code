import pygame
from pygame.locals import *
import random

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
ENEMY_SIZE = 30
ENEMY_SPEED = 2
FPS = 60
WHITE = (255, 255, 255)
PLAYER = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")
clock = pygame.time.Clock()

# Player position
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = (HEIGHT - PLAYER_SIZE) // 2

# Enemy position and direction
enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
enemy_y = random.randint(0, HEIGHT - ENEMY_SIZE)
enemy_dx = 0
enemy_dy = 0

# Generate random obstacles
obstacles = []
for _ in range(10):
    obstacle_x = random.randint(0, WIDTH - PLAYER_SIZE)
    obstacle_y = random.randint(0, HEIGHT - PLAYER_SIZE)
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, PLAYER_SIZE, PLAYER_SIZE))

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[K_RIGHT]:
        player_x += PLAYER_SPEED
    if keys[K_UP]:
        player_y -= PLAYER_SPEED
    if keys[K_DOWN]:
        player_y += PLAYER_SPEED

    # Enemy movement (chasing player)
    if player_x < enemy_x:
        enemy_dx = -ENEMY_SPEED
    elif player_x > enemy_x:
        enemy_dx = ENEMY_SPEED
    else:
        enemy_dx = 0

    if player_y < enemy_y:
        enemy_dy = -ENEMY_SPEED
    elif player_y > enemy_y:
        enemy_dy = ENEMY_SPEED
    else:
        enemy_dy = 0

    enemy_x += enemy_dx
    enemy_y += enemy_dy

    # Check for collisions with obstacles
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            player_x, player_y = (WIDTH - PLAYER_SIZE) // 2, (HEIGHT - PLAYER_SIZE) // 2

    # Render
    screen.fill(WHITE)
    pygame.draw.rect(screen, PLAYER, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE))
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
