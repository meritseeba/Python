import pygame
import sys

# Initsialiseerime PyGame
pygame.init()

# Aken
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 2")

# Laeme pildid
bg_image = pygame.image.load("bg_shop.png")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")

# Skaalame vajadusel
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
seller = pygame.transform.scale(seller, (255, 304))
chat = pygame.transform.scale(chat, (257, 200))
# Font
font = pygame.font.SysFont('arial', 24)
name_text = font.render("Tere, Merit olen!", True, (255, 255, 255))  # Muuda siia oma nimi

# Põhiline tsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joonistame kõik elemendid
    screen.blit(bg_image, (0, 0))  # taust
    screen.blit(seller, (105, 160))  # poemüüja
    screen.blit(chat, (245, 70))  # jutumull
    screen.blit(name_text, (280, 140))  # tekst jutumulli sees

    pygame.display.flip()

# Lõpetame
pygame.quit()
sys.exit()
