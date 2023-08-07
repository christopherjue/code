import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()
width, height = 800, 600
pygame.display.set_mode((width, height))

# Game variables
cookies = 0
cookie_per_click = 1
cookie_per_second = 0
clicker_cost = 10
clicker_multiplier = 2
clicker_count = 0
win_condition = 1000000

# Set up fonts
font = pygame.font.SysFont("Arial", 30)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Clicked on the cookie
                cookies += cookie_per_click

                # Check if player can afford a clicker upgrade
                if cookies >= clicker_cost:
                    cookies -= clicker_cost
                    cookie_per_second += 50
                    clicker_cost *= clicker_multiplier
                    clicker_count += 1

    # Update game logic
    cookies += cookie_per_second / 60  # Increment cookies per second

    # Check if player wins
    if cookies >= win_condition:
        print("You win!")
        running = False

    # Clear the screen
    pygame.display.get_surface().fill((255, 255, 255))

    # Render text
    text = font.render(f"Cookies: {int(cookies)}", True, (0, 0, 0))
    clicker_text = font.render(f"Clicker Cost: {clicker_cost}", True, (0, 0, 0))
    count_text = font.render(f"Clicker Count: {clicker_count}", True, (0, 0, 0))
    pygame.display.get_surface().blit(text, (10, 10))
    pygame.display.get_surface().blit(clicker_text, (10, 50))
    pygame.display.get_surface().blit(count_text, (10, 90))

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
