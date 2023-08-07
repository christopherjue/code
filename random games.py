import pygame
import sys
import random
# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("2D Platformer")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Player properties
player_size = 30
player_x = width // 2
player_y = height - player_size * 2
player_speed = 5
player_jump = 10
player_is_jumping = False

# Platform properties
platform_width = 200
platform_height = 20
platform_x = width // 2 - platform_width // 2
platform_y = height - platform_height * 3

# Lava properties
lava_x = 0
lava_y = height - platform_height

# Timer properties
timer_total = 120  # 2 minutes
timer = timer_total
lava_rise_interval = 30  # 30 seconds
lava_rise_speed = 1
lava_rise_counter = 0

# Game loop
clock = pygame.time.Clock()
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_d] and player_x < width - player_size:
        player_x += player_speed
    if keys[pygame.K_SPACE] and not player_is_jumping:
        player_is_jumping = True

    if player_is_jumping:
        player_y -= player_jump
        player_jump -= 1
        if player_jump < -10:
            player_is_jumping = False
            player_jump = 10

    # Update timer
    timer -= 1
    if timer == 0:
        timer = timer_total
        lava_rise_counter += 1
        if lava_rise_counter % 2 == 0:
            lava_rise_speed *= 2

    # Update lava position
    if lava_y > 0:
        lava_y -= lava_rise_speed

    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))

    # Draw platform
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, platform_width, platform_height))

    # Draw lava
    pygame.draw.rect(screen, YELLOW, (lava_x, lava_y, width, height - lava_y))

    # Check collision
    if player_y + player_size >= platform_y and player_y + player_size <= platform_y + platform_height:
        if player_x + player_size >= platform_x and player_x <= platform_x + platform_width:
            player_is_jumping = False

    # Game over condition
    if player_y + player_size >= lava_y:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Display timer
    font = pygame.font.SysFont(None, 36)
    text = font.render("Time: " + str(timer // 60) + ":" + str(timer % 60).zfill(2), True, RED)
    screen.blit(text, (10, 10))

    pygame.display.flip()
