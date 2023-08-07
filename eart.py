import pygame
from pygame.locals import *

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SUPERHOT Python Edition")

# Set up the game clock
clock = pygame.time.Clock()

# Player variables
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 5

# Time variables
is_time_stopped = False
time_scale = 1.0

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the player input
    keys = pygame.key.get_pressed()
    for key in keys:
        if key == K_w:
            player_y -= player_speed * time_scale
        if key == K_s:
            player_y += player_speed * time_scale
        if key == K_a:
            player_x -= player_speed * time_scale
        if key == K_d:
            player_x += player_speed * time_scale

    # Check if time is stopped
    if not any(keys):
        is_time_stopped = True
    else:
        is_time_stopped = False

    # Update the display
    window.fill(BLACK)
    pygame.draw.circle(window, WHITE, (player_x, player_y), 10)

    # Draw time indicator
    time_indicator = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    if is_time_stopped:
        pygame.draw.circle(time_indicator, RED, (WIDTH // 2, HEIGHT // 2), 100, 3)
    window.blit(time_indicator, (0, 0))

    pygame.display.flip()
    clock.tick(FPS)

# Quit the game
pygame.quit()
