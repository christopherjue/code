import pygame
import pymunk

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Create a Pygame space
space = pymunk.Space()
space.gravity = (0, 500)

# Function to create a round oval
def create_oval(position):
    moment = pymunk.moment_for_circle(1, 0, 20, (0, 0))
    body = pymunk.Body(1, moment)
    body.position = position
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.8
    space.add(body, shape)
    return body

# Function to create stairs
def create_stairs(position):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Poly.create_box(body, (100, 20), 0)
    body.position = position
    shape.elasticity = 0.8
    space.add(body, shape)
    return body

# List to store the ovals
ovals = []

# List to store the stairs
stairs = []

# Collision type for stairs
STAIR_COLLISION_TYPE = 1

# Collision callback for ovals and stairs
def collision_callback(arbiter, space, _):
    return True

# Add collision handler
space.add_collision_handler(STAIR_COLLISION_TYPE, 0).begin = collision_callback

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:  # Right-click to spawn oval
                oval_body = create_oval(event.pos)
                ovals.append(oval_body)
            elif event.button == 1:  # Left-click to spawn stairs
                stair_body = create_stairs(event.pos)
                stairs.append(stair_body)
                for shape in stair_body.shapes:
                    shape.filter = pymunk.ShapeFilter(categories=STAIR_COLLISION_TYPE)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the ovals
    for oval_body in ovals:
        position = oval_body.position
        pygame.draw.circle(screen, (0, 0, 255), position, 20)

    # Draw the stairs
    for stair_body in stairs:
        for shape in stair_body.shapes:
            vertices = shape.get_vertices()
            vertices = [(v[0] + stair_body.position[0], v[1] + stair_body.position[1]) for v in vertices]
            pygame.draw.polygon(screen, (0, 255, 0), vertices)

    # Update the physics simulation
    space.step(1 / 60.0)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
