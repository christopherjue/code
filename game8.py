import pygame
from pygame.locals import *

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Clicker Game with Factory Purchase")
clock = pygame.time.Clock()

# Game variables
score = 0
score_per_second = 0
clicker_cost = 10
clicker_multiplier = 5
clicker_purchased = False
factory_cost = 30
factory_multiplier = 100
factory_count = 0

# Timers
score_timer = pygame.time.get_ticks()
clicker_timer = pygame.time.get_ticks()

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                score += 1

    # Update score per second
    current_time = pygame.time.get_ticks()
    if clicker_purchased and current_time - score_timer >= 1000:
        score += score_per_second
        score_timer = current_time

    # Clear the screen
    screen.fill(WHITE)

    # Draw score
    font = pygame.font.Font(None, 36)
    score_text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Draw clicker purchase button
    clicker_button_text = "Buy Clicker (" + str(clicker_cost) + ")"
    clicker_button = pygame.Rect(10, 50, 200, 50)
    pygame.draw.rect(screen, BLACK, clicker_button)
    clicker_button_font = pygame.font.Font(None, 24)
    clicker_button_text_render = clicker_button_font.render(clicker_button_text, True, WHITE)
    screen.blit(clicker_button_text_render, (20, 60))

    # Draw factory purchase button
    factory_button_text = "Buy Factory (" + str(factory_cost) + ")"
    factory_button = pygame.Rect(10, 120, 200, 50)
    pygame.draw.rect(screen, BLACK, factory_button)
    factory_button_font = pygame.font.Font(None, 24)
    factory_button_text_render = factory_button_font.render(factory_button_text, True, WHITE)
    screen.blit(factory_button_text_render, (20, 130))

    # Handle clicker purchase
    mouse_pos = pygame.mouse.get_pos()
    if clicker_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
        if score >= clicker_cost and not clicker_purchased:
            score -= clicker_cost
            clicker_purchased = True
            score_per_second = clicker_multiplier

    # Handle factory purchase
    if factory_button.collidepoint(mouse_pos) and event.type == pygame.MOUSEBUTTONDOWN:
        if score >= factory_cost:
            score -= factory_cost
            factory_count += 1
            score_per_second += factory_multiplier

    # Draw factory count
    factory_count_text = "Factories: " + str(factory_count)
    factory_count_render = factory_button_font.render(factory_count_text, True, BLACK)
    screen.blit(factory_count_render, (20, 190))

    # Update display
   
