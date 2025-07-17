import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping-Pong Game")

# Colors
BACKGROUND_COLOR = (200, 200, 200)
FONT_COLOR = (0, 0, 0)

# Load images
paddle_png = pygame.image.load("pad.png")
ball_png = pygame.image.load("ball.png")

# Resize images
paddle_width, paddle_height = 120, 20
ball_size = 20
paddle_png = pygame.transform.scale(paddle_png, (paddle_width, paddle_height))
ball_png = pygame.transform.scale(ball_png, (ball_size, ball_size))

# Paddle initial position and speed
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = int(HEIGHT / 1.5)
paddle_speed = 4
paddle_direction = 1  # 1 for right, -1 for left

# Ball initial position and speed
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_speed_x = 3
ball_speed_y = 3

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move paddle
    paddle_x += paddle_speed * paddle_direction
    if paddle_x <= 0 or paddle_x + paddle_width >= WIDTH:
        paddle_direction *= -1

    # Move ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Ball collision with walls
    if ball_x <= 0 or ball_x + ball_size >= WIDTH:
        ball_speed_x *= -1
    if ball_y <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    if (paddle_y < ball_y + ball_size <= paddle_y + paddle_height and
        paddle_x < ball_x + ball_size and ball_x < paddle_x + paddle_width and
        ball_speed_y > 0):
        ball_speed_y *= -1
        score += 1

    # Ball missed paddle
    if ball_y + ball_size >= HEIGHT:
        score -= 1
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Draw paddle and ball
    screen.blit(paddle_png, (paddle_x, paddle_y))
    screen.blit(ball_png, (ball_x, ball_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, FONT_COLOR)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
