import pygame
import random
import sys
import math

# Initialize Pygame
pygame.init()

# Define the window size
window_width, window_height = 1000, 800
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Your .io Game')

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Define player constants
INITIAL_SIZE = 50
PLAYER_SPEED = 5
FOOD_RADIUS = 5
FOOD_COUNT = 100
OPPONENT_COUNT = 3

class Player:
    def __init__(self):
        self.x = window_width // 2
        self.y = window_height // 2
        self.size = INITIAL_SIZE
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.body = []
        self.body.append((self.x, self.y))

    def move(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.x += int(PLAYER_SPEED * math.cos(angle))
        self.y += int(PLAYER_SPEED * math.sin(angle))

    def grow(self):
        self.size += 1
        self.body.append((self.x, self.y))

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)
        for part in self.body:
            pygame.draw.circle(window, self.color, part, self.size)

class Opponent:
    def __init__(self):
        self.x = random.randint(50, window_width - 50)
        self.y = random.randint(50, window_height - 50)
        self.size = random.randint(30, 60)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.body = []
        self.body.append((self.x, self.y))

    def move(self, target_x, target_y):
        angle = math.atan2(target_y - self.y, target_x - self.x)
        self.x += int(PLAYER_SPEED * math.cos(angle))
        self.y += int(PLAYER_SPEED * math.sin(angle))

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.size)
        for part in self.body:
            pygame.draw.circle(window, self.color, part, self.size)

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw(self):
        pygame.draw.circle(window, self.color, (self.x, self.y), FOOD_RADIUS)

def main():
    player = Player()
    foods = [Food(random.randint(50, window_width - 50), random.randint(50, window_height - 50)) for _ in range(FOOD_COUNT)]
    opponents = [Opponent() for _ in range(OPPONENT_COUNT)]

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Move the player towards the mouse position
        player.move(mouse_x, mouse_y)

        # Move opponents to follow the player
        for opponent in opponents:
            opponent.move(player.x, player.y)

        # Check collision with food
        for food in foods:
            distance = math.hypot(player.x - food.x, player.y - food.y)
            if distance < player.size + FOOD_RADIUS:
                player.grow()
                foods.remove(food)

        # Check collision with own body
        for part in player.body[:-1]:
            distance = math.hypot(player.x - part[0], player.y - part[1])
            if distance < player.size:
                game_over = True

        # Move and draw opponents
        for opponent in opponents:
            opponent.draw()

        # Clear the screen
        window.fill(white)

        # Draw the food
        for food in foods:
            food.draw()

        # Draw the player
        player.draw()

        # Update the display
        pygame.display.update()

        # Control the frame rate
        clock.tick(60)

    # Game over - Show "Game Over" message and wait for a keypress to restart
    font = pygame.font.Font(None, 36)
    text = font.render("Game Over! Press any key to restart.", True, black)
    text_rect = text.get_rect(center=(window_width // 2, window_height // 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                main()  # Restart the game

        window.fill(white)
        window.blit(text, text_rect)
        pygame.display.update()

if __name__ == "__main__":
    main()
