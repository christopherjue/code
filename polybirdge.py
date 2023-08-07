import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Advanced Poly Bridge 2")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Bridge properties
bridge_length = 200
bridge_height = 20
bridge_x = (width - bridge_length) // 2
bridge_y = height - bridge_height - 50

# Physics properties
gravity = 0.5

# Level properties
current_level = 1
max_level = 5

# Rope properties
ropes = []

# Support beam properties
support_beams = []

# Car properties
car_width = 50
car_height = 30
car_x = bridge_x + bridge_length - car_width
car_y = bridge_y - car_height

# Create a bridge segment
def create_bridge_segment(x, y, length):
    segment = pygame.Rect(x, y, length, bridge_height)
    return segment

# Create a rope
def create_rope(x, y, length):
    rope = pygame.Rect(x, y, bridge_x - x, length)
    return rope

# Create a support beam
def create_support_beam(x, y, length):
    beam = pygame.Rect(x, y, length, bridge_y - y)
    return beam

# Load level
def load_level(level):
    global bridge_length, bridge_x, bridge_y
    # Update bridge properties based on level
    if level == 1:
        bridge_length = 200
    elif level == 2:
        bridge_length = 250
    elif level == 3:
        bridge_length = 300
    elif level == 4:
        bridge_length = 350
    elif level == 5:
        bridge_length = 400

    # Reset bridge position
    bridge_x = (width - bridge_length) // 2
    bridge_y = height - bridge_height - 50

    # Reset car position
    global car_x, car_y
    car_x = bridge_x + bridge_length - car_width
    car_y = bridge_y - car_height

    # Clear ropes and support beams
    global ropes, support_beams
    ropes = []
    support_beams = []

# Level selection screen
def level_selection():
    selected_level = None
    font = pygame.font.SysFont(None, 40)

    while selected_level is None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    selected_level = 1
                elif event.key == pygame.K_2:
                    selected_level = 2
                elif event.key == pygame.K_3:
                    selected_level = 3
                elif event.key == pygame.K_4:
                    selected_level = 4
                elif event.key == pygame.K_5:
                    selected_level = 5

        screen.fill(WHITE)
        text = font.render("Select Level (1-5):", True, BLACK)
        screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
        pygame.display.flip()

    return selected_level

# Start level selection
current_level = level_selection()
load_level(current_level)

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Place a rope
                if bridge_x > event.pos[0] > 0 and bridge_y > event.pos[1] > 0:
                    ropes.append(create_rope(event.pos[0], event.pos[1], 10))
                # Place a support beam
                elif event.pos[0] > bridge_x and event.pos[1] < bridge_y:
                    support_beams.append(create_support_beam(event.pos[0], event.pos[1], 10))

    # Clear the screen
    screen.fill(WHITE)

    # Draw the bridge
    pygame.draw.rect(screen, BLACK, create_bridge_segment(bridge_x, bridge_y, bridge_length))

    # Draw ropes
    for rope in ropes:
        pygame.draw.rect(screen, GREEN, rope)

    # Draw support beams
    for beam in support_beams:
        pygame.draw.rect(screen, BLACK, beam)

    # Draw the car
    pygame.draw.rect(screen, RED, pygame.Rect(car_x, car_y, car_width, car_height))

    # Apply physics
    bridge_y += gravity

    # Check for collisions
    if bridge_y + bridge_height >= height:
        pygame.draw.rect(screen, RED, create_bridge_segment(bridge_x, bridge_y, bridge_length))
        bridge_y = height - bridge_height

    # Check for level completion
    if bridge_y + bridge_height <= 0:
        # Load next level
        if current_level < max_level:
            current_level += 1
            current_level = level_selection()
            load_level(current_level)
        else:
            print("Congratulations! You have completed all levels.")
            pygame.quit()
            sys.exit()

    # Update the display
    pygame.display.flip()
