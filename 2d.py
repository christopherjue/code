import pygame
import pymunk

# Initialize Pygame
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Initialize Pygame physics engine (Pymunk)
space = pymunk.Space()
space.gravity = (0, 1000)

# Create a static ground body
ground = pymunk.Body(body_type=pymunk.Body.STATIC)
ground.position = (width // 2, height - 20)
ground_shape = pymunk.Segment(ground, (-width // 2, 0), (width // 2, 0), 0)
space.add(ground, ground_shape)

# Rope variables
rope_length = 200
rope_anchor = (width // 2, height // 2)
rope_bodies = []

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                # Create a ball on the rope
                x, y = event.pos
                body = pymunk.Body(1, 1)
                body.position = x, y
                shape = pymunk.Circle(body, 10)
                space.add(body, shape)

                rope_bodies.append(body)

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            # Create multiple balls while holding the left mouse button
            x, y = event.pos
            body = pymunk.Body(1, 1)
            body.position = x, y
            shape = pymunk.Circle(body, 10)
            space.add(body, shape)

        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[2]:
            # Create walls while holding the right mouse button
            x, y = event.pos
            body = pymunk.Body(body_type=pymunk.Body.STATIC)
            body.position = x, y
            shape = pymunk.Poly.create_box(body, (40, 40))
            space.add(body, shape)

    # Update physics
    dt = 1.0 / 60.0
    for _ in range(10):
        space.step(dt)

    # Draw the scene
    screen.fill((255, 255, 255))

    for body in space.bodies:
        for shape in body.shapes:
            if isinstance(shape, pymunk.Circle):
                x, y = map(int, body.position)
                pygame.draw.circle(screen, (0, 0, 255), (x, y), int(shape.radius))
            elif isinstance(shape, pymunk.Poly):
                points = shape.get_vertices()
                points = [(body.position + p).int_tuple for p in points]
                pygame.draw.polygon(screen, (0, 0, 0), points)

    # Draw the rope
    if len(rope_bodies) > 0:
        prev_pos = rope_anchor
        for body in rope_bodies:
            pos = body.position.int_tuple
            pygame.draw.line(screen, (0, 0, 0), prev_pos, pos)
            prev_pos = pos

        # Attach the last ball to the rope anchorPlease note that the code provided above is a simplified example and may not fully meet your requirements. It demonstrates basic concepts of creating balls, walls, and a rope-like structure using a physics engine. To run this code, you'll need to have the `pygame` and `pymunk` libraries installed.

