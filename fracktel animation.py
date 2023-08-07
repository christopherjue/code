import numpy as np
import pygame

# Define the fractal function (You can choose different fractals)
def fractal_function(c, z, max_iter):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z**2 + c
    return max_iter

# Initialize the fractal parameters
width, height = 800, 600
x_min, x_max = -2.0, 2.0
y_min, y_max = -2.0, 2.0
z_min, z_max = -2.0, 2.0
max_iter = 100

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("3D Fractal Explorer")
clock = pygame.time.Clock()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    camera_speed = 0.1
    if keys[pygame.K_w]:
        y_min += camera_speed
        y_max += camera_speed
    if keys[pygame.K_s]:
        y_min -= camera_speed
        y_max -= camera_speed
    if keys[pygame.K_a]:
        x_min += camera_speed
        x_max += camera_speed
    if keys[pygame.K_d]:
        x_min -= camera_speed
        x_max -= camera_speed
    if keys[pygame.K_SPACE]:
        z_min += camera_speed
        z_max += camera_speed

    # Update the fractal
    zoom = np.exp((z_min + z_max) / 2)
    X = np.linspace(x_min / zoom, x_max / zoom, width)
    Y = np.linspace(y_min / zoom, y_max / zoom, height)
    C = X[:, np.newaxis] + Y[np.newaxis, :] * 1j
    fractal = np.zeros((height, width))
    for i in range(height):
        for j in range(width):
            z = C[i, j]
            fractal[i, j] = fractal_function(z, z, max_iter)

    # Normalize the iterations for coloring
    fractal_norm = fractal / max_iter

    # Display the fractal using Pygame
    fractal_surface = pygame.surfarray.make_surface(np.flipud(fractal_norm * 255).astype(np.uint8))
    screen.blit(fractal_surface, (0, 0))
    pygame.display.flip()

    # Limit to 60 FPS
    clock.tick(60)

pygame.quit()
