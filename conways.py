import pygame
import math


# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Top-Down Shooter")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Player properties
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_radius = 20
player_speed = 5

# Bullet properties
bullet_radius = 5
bullet_speed = 8
bullets = []

# Enemy properties
enemy_radius = 15
enemy_speed = 3
enemies = []

# Game loop
running = True
while running:
    # Clear the screen
    window.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calculate the angle between the player and the mouse
    angle = math.atan2(mouse_y - player_y, mouse_x - player_x)

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed

    # Draw the player
    pygame.draw.circle(window, RED, (int(player_x), int(player_y)), player_radius)

    # Shoot bullets
    if pygame.mouse.get_pressed()[0]:
        bullet_x = player_x + (player_radius * math.cos(angle))
        bullet_y = player_y + (player_radius * math.sin(angle))
        bullets.append((bullet_x, bullet_y, angle))

    # Move and draw bullets
    for bullet in bullets:
        bullet_x, bullet_y, angle = bullet
        bullet_x += bullet_speed * math.cos(angle)
        bullet_y += bullet_speed * math.sin(angle)
        pygame.draw.circle(window, RED, (int(bullet_x), int(bullet_y)), bullet_radius)
        bullet = (bullet_x, bullet_y, angle)

        # Remove bullets that go off-screen
        if bullet_x < 0 or bullet_x > WIDTH or bullet_y < 0 or bullet_y > HEIGHT:
            bullets.remove(bullet)

    # Spawn enemies
    if len(enemies) < 10:
        enemy_x = random.randint(0, WIDTH)
        enemy_y = random.randint(0, HEIGHT)
        enemies.append((enemy_x, enemy_y))

    # Move and draw enemies
    for enemy in enemies:
        enemy_x, enemy_y = enemy
        angle = math.atan2(player_y - enemy_y, player_x - enemy_x)
        enemy_x += enemy_speed * math.cos(angle)
        enemy_y += enemy_speed * math.sin(angle)
        pygame.draw.circle(window, RED, (int(enemy_x), int(enemy_y)), enemy_radius)
        enemy = (enemy_x, enemy_y)

        # Check for collisions with bullets
        for bullet in bullets:
            bullet_x, bullet_y, _ = bullet
            distance = math.sqrt((enemy_x - bullet_x) ** 2 + (enemy_y - bullet_y) ** 2)
            if distance < enemy_radius + bullet_radius:
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
