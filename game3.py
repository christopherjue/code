import pygame
from pygame.locals import *
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
ENEMY_SIZE = 20
ENEMY_SPEED = 2
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
OBSTACLE_SIZE = 50

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Game with Obstacles and Enemy")
clock = pygame.time.Clock()

# Player position
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = (HEIGHT - PLAYER_SIZE) // 2

# Enemy position and angle
enemy_x = random.randint(0, WIDTH - ENEMY_SIZE)
enemy_y = random.randint(0, HEIGHT - ENEMY_SIZE)
enemy_angle = 0

# Create obstacles
obstacles = []
for _ in range(10):
    obstacle_x = random.randint(0, WIDTH - OBSTACLE_SIZE)
    obstacle_y = random.randint(0, HEIGHT - OBSTACLE_SIZE)
    obstacles.append(pygame.Rect(obstacle_x, obstacle_y, OBSTACLE_SIZE, OBSTACLE_SIZE))

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and player_x > 0:
        player_x -= PLAYER_SPEED
    if keys[K_RIGHT] and player_x < WIDTH - PLAYER_SIZE:
        player_x += PLAYER_SPEED
    if keys[K_UP] and player_y > 0:
        player_y -= PLAYER_SPEED
    if keys[K_DOWN] and player_y < HEIGHT - PLAYER_SIZE:
        player_y += PLAYER_SPEED

    # Enemy movement
    dx = player_x - enemy_x
    dy = player_y - enemy_y
    enemy_angle = math.atan2(dy, dx)
    enemy_x += math.cos(enemy_angle) * ENEMY_SPEED
    enemy_y += math.sin(enemy_angle) * ENEMY_SPEED

    # Wrap around to the other side of the screen
    if enemy_x < 0:
        enemy_x = WIDTH - ENEMY_SIZE
    elif enemy_x > WIDTH - ENEMY_SIZE:
        enemy_x = 0
    if enemy_y < 0:
        enemy_y = HEIGHT - ENEMY_SIZE
    elif enemy_y > HEIGHT - ENEMY_SIZE:
        enemy_y = 0

    # Collision detection
    player_rect = pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_SIZE, ENEMY_SIZE)
    for obstacle in obstacles:
        if player_rect.colliderect(obstacle):
            # Collision with player detected, handle it here
            print("Player collision detected!")
        if enemy_rect.colliderect(obstacle):
            # Collision with enemy detected, handle it here
            print("Enemy collision detected!")

    # Render
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.circle(screen, RED, (int(enemy_x + ENEMY_SIZE / 2), int(enemy_y + ENEMY_SIZE / 2)), ENEMY_SIZE // 2)
    for obstacle in obstacles:
        pygame.draw.rect(screen, BLACK, obstacle)

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
