import pygame
import sys
import random

pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
BIRD_WIDTH, BIRD_HEIGHT = 40, 30
PIPE_WIDTH, PIPE_HEIGHT = 60, 400
GRAVITY = 0.25
JUMP = -4.5
PIPE_SPACING = 200
PIPE_VELOCITY = -2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Load images
bird_img = pygame.image.load("bird.png")
pipe_img = pygame.image.load("pipe.png")

bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))
pipe_img = pygame.transform.scale(pipe_img, (PIPE_WIDTH, PIPE_HEIGHT))


class Bird:
    def __init__(self):
        self.x = WIDTH // 2 - BIRD_WIDTH // 2
        self.y = HEIGHT // 2 - BIRD_HEIGHT // 2
        self.velocity = 0

    def jump(self):
        self.velocity = JUMP

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def draw(self):
        win.blit(bird_img, (self.x, self.y))

    def collide(self, pipe):
        return pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT).colliderect(pipe)


class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, HEIGHT - PIPE_SPACING - 100)
        self.passed = False

    def move(self):
        self.x += PIPE_VELOCITY

    def draw(self):
        win.blit(pipe_img, (self.x, self.height - PIPE_HEIGHT))
        win.blit(pipe_img, (self.x, self.height + PIPE_SPACING))

    def offscreen(self):
        return self.x + PIPE_WIDTH < 0


def draw_background():
    win.fill(WHITE)


def draw_score(score):
    font = pygame.font.Font(None, 50)
    text = font.render(str(score), True, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))


def game_over(score):
    font = pygame.font.Font(None, 70)
    text = font.render(f"Game Over. Your Score: {score}", True, BLACK)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)


def main():
    bird = Bird()
    pipes = [Pipe(WIDTH + i * PIPE_SPACING) for i in range(3)]
    score = 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        bird.update()

        for pipe in pipes:
            pipe.move()
            if pipe.offscreen():
                pipe.x = pipes[-1].x + PIPE_SPACING
                pipe.height = random.randint(100, HEIGHT - PIPE_SPACING - 100)
                pipe.passed = False

            if bird.collide(pipe):
                game_over(score)
                main()

            if not pipe.passed and pipe.x + PIPE_WIDTH < bird.x:
                score += 1
                pipe.passed = True

        if bird.y <= 0 or bird.y >= HEIGHT - BIRD_HEIGHT:
            game_over(score)
            main()

        draw_background()
        bird.draw()
        for pipe in pipes:
            pipe.draw()
        draw_score(score)

        pygame.display.update()


if __name__ == "__main__":
    main()

    import pygame
import sys
import random
import base64

# Decoded base64 images
bird_img_data = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAA1UlEQVRIDbXBAQEAAAABIP6Pzgpv
0tO2/2k5eV9zZ3p2X1Xem3ZGVX3vYVdF8YIWIYIxYihmGDKIYYMoihgjFiKEYYMohhgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihg
jFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiK
EYYMoihgjFiKEYYM"""
pipe_img_data = """
iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAAVklEQVRIDbXBAQEAAAABIP6Pzgpv
0tO2/2k5eV9zZ3p2X1Xem3ZGVX3vYVdF8YIWIYIxYihmGDKIYYMoihgjFiKEYYMohhgjFiKEYYM
oihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoihgjFiKEYYMoi
