import pygame
import sys

# Initsialiseeri PyGame
pygame.init()

# Ekraani mõõdud
screen_width = 640
screen_height = 480

# Funktsioon, mis joonistab ruudustiku fikseeritud mõõtudes
def start_game(tile_size, line_color):
    # Arvuta veergude ja ridade arv ekraani mõõtude põhjal
    cols = screen_width // tile_size
    rows = screen_height // tile_size

    # Loo ekraan
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Ruudustik 640x480 sees")

    # Roheline taust
    green = (0, 128, 0)

    running = True
    while running:
        # Kontrolli sündmusi (nt akna sulgemist)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Täida taust rohelisega
        screen.fill(green)

        # Joonista vertikaaljooned
        for x in range(0, cols * tile_size + 1, tile_size):
            pygame.draw.line(screen, line_color, (x, 0), (x, rows * tile_size))

        # Joonista horisontaaljooned
        for y in range(0, rows * tile_size + 1, tile_size):
            pygame.draw.line(screen, line_color, (0, y), (cols * tile_size, y))

        # Uuenda ekraani
        pygame.display.flip()

    # PyGame lõpetamine
    pygame.quit()
    sys.exit()

# 🔧 Näide: ruudu suurus 20 pikslit, punane ruudustik
start_game(tile_size=20, line_color=(255, 0, 0))
