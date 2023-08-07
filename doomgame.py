import pygame
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Player variables
player_radius = 20
player_x = width // 2
player_y = height // 2
player_speed = 5
player_lives = 3

# Bullet variables
bullet_radius = 5
bullet_speed = 10
bullets = []

# Enemy variables
enemy_radius = 15
enemy_speed = 3
enemies = []

# Generate a random level
def generate_level():
    for _ in range(10):
        x = random.randint(enemy_radius * 2, width - enemy_radius * 2)
        y = random.randint(enemy_radius * 2, height - enemy_radius * 2)
        enemies.append([x, y])

# Draw player and bullets
def draw_player():
    pygame.draw.circle(screen, WHITE, (player_x, player_y), player_radius)
    pygame.draw.rect(screen, GREEN, (player_x - 5, player_y - 5, 10, 10))

def draw_bullets():
    for bullet in bullets:
        pygame.draw.circle(screen, BLACK, (bullet[0], bullet[1]), bullet_radius)

def move_bullets():
    for bullet in bullets:
        bullet[0] += bullet[2]
        bullet[1] += bullet[3]

def remove_bullet(bullet):
    bullets.remove(bullet)

# Draw enemies
def draw_enemies():
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0] - enemy_radius, enemy[1] - enemy_radius, enemy_radius * 2, enemy_radius * 2))

def move_enemies():
    for enemy in enemies:
        enemy[0] += random.randint(-enemy_speed, enemy_speed)
        enemy[1] += random.randint(-enemy_speed, enemy_speed)

def check_collision():
    for enemy in enemies:
        if abs(enemy[0] - player_x) < enemy_radius + player_radius and abs(enemy[1] - player_y) < enemy_radius + player_radius:
            return True
    return False

# Game loop
running = True
generate_level()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x
                bullet_y = player_y
                bullet_direction = pygame.mouse.get_pos()
                bullet_dx = bullet_direction[0] - player_x
                bullet_dy = bullet_direction[1] - player_y
                bullet_distance = (bullet_dx ** 2 + bullet_dy ** 2) ** 0.5
                bullet_dx /= bullet_distance
                bullet_dy /= bullet_distance
                bullets.append([bullet_x, bullet_y, bullet_dx * bullet_speed, bullet_dy * bullet_speed])

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_w]:
        player_y -= player_speed
    if pressed_keys[pygame.K_a]:
        player_x -= player_speed
    if pressed_keys[pygame.K_s]:
        player_y += player_speed
    if pressed_keys[pygame.K_d]:
        player_x += player_speed

    screen.fill(GREEN)  # Background color

    draw_player()
    draw_bullets()
    move_bullets()

    draw_enemies()
    move_enemies()

    if check_collision():
        player_lives -= 1
        player_x = width // 2
        player_y = height // 2

    # Draw lives
    for i in range(player_lives):
        pygame.draw.rect(screen, YELLOW, (10 + i * 30, 10, 20, 20))

    if player_lives <= 0:
        running = False

    pygame.display.flip()

# Clean up
pygame.quit()
