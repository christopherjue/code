import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player
player_width = 64
player_height = 64
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Enemy
enemy_width = 64
enemy_height = 64
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = 50
enemy_speed = 2

# Bullet
bullet_width = 8
bullet_height = 16
bullet_x = 0
bullet_y = HEIGHT - bullet_height - 10
bullet_speed = 10
bullet_state = "ready"  # ready: not fired, fire: bullet is moving

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

# Game over
game_over_font = pygame.font.Font("freesansbold.ttf", 64)


def player(x, y):
    window.blit(pygame.image.load("player.png"), (x, y))


def enemy(x, y):
    window.blit(pygame.image.load("enemy.png"), (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    window.blit(pygame.image.load("bullet.png"), (x, y))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = ((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2) ** 0.5
    if distance < 27:
        return True
    return False


def show_score(x, y):
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (x, y))


def game_over_text():
    game_over_text = game_over_font.render("GAME OVER", True, RED)
    window.blit(game_over_text, (WIDTH // 2 - 200, HEIGHT // 2 - 50))


# Game loop
running = True
while running:
    # Clear the window
    window.fill(bLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            if event.key == pygame.K_RIGHT:
                player_x += player_speed
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_change = 0

    # Player boundaries
    if player_x <= 0:
        player_x = 0
    elif player_x >= WIDTH - player_width:
        player_x = WIDTH - player_width

    # Enemy movement
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= WIDTH - enemy_width:
        enemy_speed *= -1
        enemy_y += enemy_height

    # Bullet movement
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_state = "ready"
            bullet_y = HEIGHT - bullet_height - 10

    # Collision detection
    if is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
        bullet_state = "ready"
        bullet_y = HEIGHT - bullet_height - 10
        score += 1
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = 50

    # Draw player, enemy, and bullet
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)

    # Draw score
    show_score(text_x, text_y)

    # Check for game over
    if enemy_y > HEIGHT - enemy_height:
        game_over_text()
        break

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
