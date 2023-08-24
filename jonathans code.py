import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
# ... (same as before)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galactic Gliders")

# Game loop
def game_loop():
    # ... (same as before)

    while not game_over:
        # ... (same as before)

        # Move projectiles
        for projectile in projectiles[:]:
            projectile[1] -= 5  # Move upwards

            # Check if projectile is out of screen
            if projectile[1] < 0:
                projectiles.remove(projectile)

            # Check for collisions between projectiles and enemies
            for hazard in hazards[:]:
                if (
                    hazard[0] < projectile[0] + PROJECTILE_WIDTH
                    and hazard[0] + HAZARD_WIDTH > projectile[0]
                    and hazard[1] < projectile[1] + PROJECTILE_HEIGHT
                    and hazard[1] + HAZARD_HEIGHT > projectile[1]
                ):
                    hazards.remove(hazard)
                    projectiles.remove(projectile)

        # ... (same as before)

        # Draw the ship, enemy, hazards, and projectiles
        pygame.draw.rect(screen, RED, (ship_x, ship_y, SHIP_WIDTH, SHIP_HEIGHT))
        pygame.draw.rect(screen, RED, (enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT))

        for hazard in hazards:
            pygame.draw.rect(
                screen,
                hazard[2],  # Color of the hazard
                (hazard[0], hazard[1], HAZARD_WIDTH, HAZARD_HEIGHT),
            )

        for projectile in projectiles:
            pygame.draw.rect(
                screen,
                projectile[2],  # Color of the projectile
                (projectile[0], projectile[1], PROJECTILE_WIDTH, PROJECTILE_HEIGHT),
            )

        # ... (same as before)

# ... (same as before)
