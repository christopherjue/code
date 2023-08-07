import pygame
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 800, 600
PLAYER_SIZE = 50
PLAYER_SPEED = 5
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Game")
clock = pygame.time.Clock()

# Player position
player_x = (WIDTH - PLAYER_SIZE) // 2
player_y = (HEIGHT - PLAYER_SIZE) // 2

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

    # Render
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))

    # Update display
    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
