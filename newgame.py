import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Space Invaders")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
light_blue = (173, 216, 230)
green = (0, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)

# Clock for FPS
clock = pygame.time.Clock()

# Player spaceship properties
spaceship_width = 50
spaceship_height = 50
spaceship_x = display_width // 2 - spaceship_width // 2
spaceship_y = display_height - spaceship_height - 10
spaceship_speed = 5

# Green square properties
green_square_size = 20
green_square_speed = 3
green_squares = []
green_square_cooldown = 60
green_square_timer = green_square_cooldown

# Boss properties
boss_width = 100
boss_height = 100
boss_x = display_width // 2 - boss_width // 2
boss_y = 50
boss_health = 100

# Life bar properties
life_bar_width = 200
life_bar_height = 20
life_bar_x = display_width // 2 - life_bar_width // 2
life_bar_y = 30
life_bar_value = 100

# Score properties
score = 0
score_font = pygame.font.Font(None, 36)

# Bullet properties
bullet_width = 5
bullet_height = 10
bullet_color = red
bullet_speed = 7
bullets = []

# Red stone properties
stone_width = 10
stone_height = 10
stone_size_increase = 2
stone_speed = 3

# Game state
game_over = False
game_win = False

# Main game loop
def game_loop():
    global spaceship_x, spaceship_speed, green_squares, green_square_timer, life_bar_value, score, bullets, boss_health, game_over, game_win

    move_left = False
    move_right = False

    while not game_over and not game_win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Check for key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_UP:
                    bullets.append({'x': spaceship_x + spaceship_width // 2 - bullet_width // 2,
                                    'y': spaceship_y - bullet_height})

            # Check for key release events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False

        # Move the spaceship
        if move_left:
            spaceship_x -= spaceship_speed
        if move_right:
            spaceship_x += spaceship_speed

        # Clear the display
        game_display.fill(light_blue)

        # Draw the spaceship
        pygame.draw.rect(game_display, black, [spaceship_x, spaceship_y, spaceship_width, spaceship_height])

        # Update and draw the green squares
        for square in green_squares:
            square['y'] += green_square_speed

            # Check for collision with the spaceship
            if (spaceship_x < square['x'] + green_square_size and
                    spaceship_x + spaceship_width > square['x'] and
                    spaceship_y < square['y'] + green_square_size and
                    spaceship_y + spaceship_height > square['y']):
                if square['color'] == green:
                    life_bar_value -= 20  # Reduce the life bar value
                square['color'] = blue

            pygame.draw.rect(game_display, square['color'], [square['x'], square['y'], green_square_size, green_square_size])

        # Update and draw the boss
        pygame.draw.rect(game_display, yellow, [boss_x, boss_y, boss_width, boss_height])

        # Update and draw the life bar
        pygame.draw.rect(game_display, black, [life_bar_x, life_bar_y, life_bar_width, life_bar_height])
        pygame.draw.rect(game_display, green, [life_bar_x, life_bar_y,
                                                (life_bar_value / 100) * life_bar_width, life_bar_height])

        # Check if life bar is empty
        if life_bar_value <= 0:
            game_over = True

        # Update and draw the score
        score_text = score_font.render("Score: " + str(score), True, black)
        game_display.blit(score_text, (10, 10))

        # Generate new green square
        green_square_timer -= 1
        if green_square_timer <= 0:
            green_squares.append({'x': random.randint(0, display_width - green_square_size),
                                  'y': 0 - green_square_size,
                                  'color': green})
            green_square_timer = green_square_cooldown

        # Update and draw the bullets
        for bullet in bullets:
            bullet['y'] -= bullet_speed
            pygame.draw.rect(game_display, bullet_color, [bullet['x'], bullet['y'], bullet_width, bullet_height])

            # Check for collision with the boss
            if (bullet['x'] > boss_x and bullet['x'] < boss_x + boss_width and
                    bullet['y'] > boss_y and bullet['y'] < boss_y + boss_height):
                bullets.remove(bullet)
                boss_health -= 10
                if boss_health <= 0:
                    score += 100
                    boss_health = 100

        # Update and draw the boss health bar
        pygame.draw.rect(game_display, black, [boss_x, boss_y - 20, boss_width, 10])
        pygame.draw.rect(game_display, red, [boss_x, boss_y - 20, (boss_health / 100) * boss_width, 10])

        # Increase red stone size after reaching 1000 points
        if score >= 1000:
            stone_width = 20
            stone_height = 20

        # Increase green square speed after reaching 1500 points
        if score >= 1500:
            green_square_speed = 5

        # Increase green square speed and red stone size after reaching certain score thresholds
        if score >= 2000:
            green_square_speed = 7
            stone_width = 30
            stone_height = 30

        # Increase green square speed and red stone size after reaching certain score thresholds
        if score >= 5000:
            green_square_speed = 10
            stone_width = 40
            stone_height = 40

        # Check for winning condition
        if score >= 10000:
            game_win = True

        # Draw the stones
        for stone in stones:
            stone['y'] += stone_speed
            pygame.draw.rect(game_display, red, [stone['x'], stone['y'], stone_width, stone_height])

            # Check for collision with the spaceship
            if (spaceship_x < stone['x'] + stone_width and
                    spaceship_x + spaceship_width > stone['x'] and
                    spaceship_y < stone['y'] + stone_height and
                    spaceship_y + spaceship_height > stone['y']):
                life_bar_value -= 20  # Reduce the life bar value

            # Check for collision with the bullets
            for bullet in bullets:
                if (bullet['x'] < stone['x'] + stone_width and
                        bullet['x'] + bullet_width > stone['x'] and
                        bullet['y'] < stone['y'] + stone_height and
                        bullet['y'] + bullet_height > stone['y']):
                    bullets.remove(bullet)
                    stones.remove(stone)
                    score += 10

        # Generate new stones
        stone_timer -= 1
        if stone_timer <= 0:
            stones.append({'x': random.randint(0, display_width - stone_width),
                           'y': 0 - stone_height})
            stone_timer = stone_cooldown

        # Update the display
        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

    if game_over:
        game_over()

    if game_win:
        game_win()


# Function to end the game
def game_over():
    global game_display

    game_display.fill(white)
    game_over_text = pygame.font.Font(None, 72).render("Game Over", True, black)
    game_display.blit(game_over_text, (display_width // 2 - 150, display_height // 2 - 50))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before quitting the game

    pygame.quit()
    quit()


# Function to display win message
def game_win():
    global game_display

    game_display.fill(white)
    win_text = pygame.font.Font(None, 72).render("You Win!", True, black)
    game_display.blit(win_text, (display_width // 2 - 150, display_height // 2 - 50))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before quitting the game

    pygame.quit()
    quit()


# Start the game
game_loop()
