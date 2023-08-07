import pygame
from pygame.locals import *
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

# ... (rest of the constants and global variables)

# Initialize game variables
paused = False  # Add this line to define the 'paused' variable

# ... (rest of the main menu code)

# Main game loop
def game_loop(level=1):
    global spaceship_x, spaceship_speed, green_squares, green_square_timer, life_bar_value, score, bullets, boss_health
    global yellow_squares, yellow_square_timer, level_duration, level_start_time
    global green_square_speed_multiplier, green_square_speed_increase_counter, paused

    game_exit = False
    move_left = False
    move_right = False
    speed_up = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

            # Check for key press events
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                elif event.key == pygame.K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_UP:
                    speed_up = True
                elif event.key == pygame.K_ESCAPE:
                    if not paused:
                        paused = True
                    else:
                        paused = False

            # Check for key release events
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    move_left = False
                elif event.key == pygame.K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_UP:
                    speed_up = False

            # Check for mouse events
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                bullets.append({'x': spaceship_x + spaceship_width // 2 - bullet_width // 2,
                                'y': spaceship_y - bullet_height})

        if paused:
            pygame.display.set_caption("Space Invaders - Paused")
            continue
        else:
            pygame.display.set_caption("Space Invaders")

        # ... (rest of the game loop code)

    pygame.quit()
    quit()

# Function for level completion
def level_complete():
    global current_level

    if current_level == 1:
        # Display boss dialogue
        for text in boss_dialogue:
            game_display.fill(white)
            dialogue_text = dialogue_font.render(text, True, black)
            game_display.blit(dialogue_text, (display_width // 2 - 200, display_height // 2 - 50))
            pygame.display.update()
            pygame.time.wait(1000)  # Wait for 1 second before showing the next dialogue

    game_display.fill(white)
    level_complete_text = pygame.font.Font(None, 72).render("Level " + str(current_level) + " Complete!", True, black)
    game_display.blit(level_complete_text, (display_width // 2 - 250, display_height // 2 - 50))
    pygame.display.update()
    pygame.time.wait(2000)  # Wait for 2 seconds before returning to main menu

    current_level += 1
    main_menu()

# ... (rest of the code)

# Start the game
def main_menu():
    global current_level, paused
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop(1)
                if event.key == pygame.K_2:
                    game_loop(2)

        # Clear the display
        game_display.fill(white)

        # Display main menu options
        menu_font = pygame.font.Font(None, 48)
        menu_text = menu_font.render("Main Menu", True, black)
        option1_text = menu_font.render("Press 1 for Level 1", True, black)
        option2_text = menu_font.render("Press 2 for Level 2", True, black)
        game_display.blit(menu_text, (display_width // 2 - 150, display_height // 2 - 100))
        game_display.blit(option1_text, (display_width // 2 - 200, display_height // 2))
        game_display.blit(option2_text, (display_width // 2 - 200, display_height // 2 + 50))

        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

# Start the game
main_menu()
