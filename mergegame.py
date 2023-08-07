import pygame

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 400
HEIGHT = 400
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Merging Game")

# Define colors
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Game variables
squares = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Spawn a blue square at the mouse position
            x, y = pygame.mouse.get_pos()
            square = pygame.Rect(x, y, 50, 50)
            squares.append(square)

    # Clear the window
    window.fill((255, 255, 255))

    # Draw the squares
    for square in squares:
        if square in squares:
            pygame.draw.rect(window, BLUE, square)
        else:
            pygame.draw.rect(window, YELLOW, square)

    # Check for merging squares
    if len(squares) >= 2:
        for i in range(len(squares)):
            for j in range(i + 1, len(squares)):
                if squares[i].colliderect(squares[j]):
                    # Merge two squares into a yellow square
                    merged_square = squares[i].union(squares[j])
                    squares.remove(squares[i])
                    squares.remove(squares[j-1])
                    squares.append(merged_square)
                    break

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
