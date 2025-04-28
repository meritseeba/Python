import pygame
import sys

# Algatab Pygame'i
pygame.init()

# Ekraani suurus
screen_width = 600
screen_height = 600

# Loo ekraan
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lumemees")

# Värvid
SKY_BLUE = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Funktsioon lumememme joonistamiseks
def draw_snowman(surface):
    surface.fill(SKY_BLUE)

    # Alumine pall
    pygame.draw.circle(surface, WHITE, (300, 450), 60)

    # Keskmine pall
    pygame.draw.circle(surface, WHITE, (300, 330), 45)

    # Ülemine pall
    pygame.draw.circle(surface, WHITE, (300, 230), 30)

    # Silmad
    pygame.draw.circle(surface, BLACK, (290, 220), 5)
    pygame.draw.circle(surface, BLACK, (310, 220), 5)

    # Nina (kolmnurkne porgand)
    pygame.draw.polygon(surface, ORANGE, [(300, 230), (300, 240), (320, 235)])

    # Suu (naeratus kaarega punktidest)
    for i in range(5):
        x = 285 + i * 7
        y = 250 + (i - 2) ** 2 // 2
        pygame.draw.circle(surface, BLACK, (x, y), 2)

# Põhiloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_snowman(screen)
    pygame.display.flip()

# Lõpeta Pygame
pygame.quit()
sys.exit()
