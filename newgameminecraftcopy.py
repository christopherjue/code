import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up the game clock
clock = pygame.time.Clock()

# Set up the paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

# Set up the ball dimensions and speed
BALL_RADIUS = 8
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Set up the AI paddle speed
AI_PADDLE_SPEED = 3
AI_PADDLE_SLOWED_SPEED = AI_PADDLE_SPEED // 5
is_slowed = False

# Set up the score
player_score = 0
ai_score = 0
score_font = pygame.font.Font(None, 36)

# Create the paddles
player_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Create the ball
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS, HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
ball_speed_x = random.choice([-1, 1]) * BALL_SPEED_X
ball_speed_y = random.choice([-1, 1]) * BALL_SPEED_Y

# Game loop
running = True
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_paddle.y > 0:
        player_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_paddle.y < HEIGHT - PADDLE_HEIGHT:
        player_paddle.y += PADDLE_SPEED
    if keys[pygame.K_w]:
        is_slowed = not is_slowed

    # AI paddle movement
    if ai_paddle.y < ball.y and ai_paddle.y < HEIGHT - PADDLE_HEIGHT:
        ai_paddle.y += AI_PADDLE_SLOWED_SPEED if is_slowed else AI_PADDLE_SPEED
    if ai_paddle.y > ball.y and ai_paddle.y > 0:
        ai_paddle.y -= AI_PADDLE_SLOWED_SPEED if is_slowed else AI_PADDLE_SPEED

    # Update ball position
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
        ball_speed_x *= -1

    # Ball collision with walls
    if ball.y <= 0 or ball.y >= HEIGHT - BALL_RADIUS * 2:
        ball_speed_y *= -1

    # Ball out of bounds
    if ball.x < 0:
        ai_score += 1
        if ai_score == 10:
            game_result = "You lose!"
            running = False
        else:
            ball.x = WIDTH // 2 - BALL_RADIUS
            ball.y = HEIGHT // 2 - BALL_RADIUS
            ball_speed_x = random.choice([-1, 1]) * BALL_SPEED_X
            ball_speed_y = random.choice([-1, 1]) * BALL_SPEED_Y
    elif ball.x > WIDTH - BALL_RADIUS * 2:
        player_score += 1
        if player_score == 10:
            game_result = "You win!"
            running = False
        else:
            ball.x = WIDTH // 2 - BALL_RADIUS
            ball.y = HEIGHT // 2 - BALL_RADIUS
            ball_speed_x = random.choice([-1, 1]) * BALL_SPEED_X
            ball_speed_y = random.choice([-1, 1]) * BALL_SPEED_Y

    # Draw the game elements
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player_paddle)
    pygame.draw.rect(window, WHITE, ai_paddle)
    pygame.draw.circle(window, WHITE, (ball.x + BALL_RADIUS, ball.y + BALL_RADIUS), BALL_RADIUS)
    score_text = score_font.render(f"{player_score} : {ai_score}", True, WHITE)
    window.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 10))

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

# Game over screen
game_over_font = pygame.font.Font(None, 72)
game_over_text = game_over_font.render(game_result, True, WHITE)
window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
pygame.display.flip()

# Wait for a few seconds before quitting the game
pygame.time.wait(3000)

# Quit the game
pygame.quit()
