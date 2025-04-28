import pygame
import sys

# Algatab Pygame'i
pygame.init()

# Ekraani suurus
screen_width = 300
screen_height = 300

# Loo ekraan
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Valgusfoor")

# Värvid
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Funktsioon valgusfoori joonistamiseks
def draw_traffic_light(surface):
    # Taust värviliseks mustaks
    surface.fill(BLACK)

    # Joonista valgusfoori kest (kõrgus 200, laius 60)
    pygame.draw.rect(surface, (150, 150, 150), (120, 50, 60, 200))

    # Punane tuli
    pygame.draw.circle(surface, RED, (150, 80), 25)
    # Kollane tuli
    pygame.draw.circle(surface, YELLOW, (150, 150), 25)
    # Roheline tuli
    pygame.draw.circle(surface, GREEN, (150, 220), 25)

# Põhiloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_traffic_light(screen)
    pygame.display.flip()

# Lõpeta Pygame
pygame.quit()
sys.exit()
