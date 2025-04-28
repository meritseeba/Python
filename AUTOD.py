import pygame
import random

# Algväärtustamine
pygame.init()
laius, kõrgus = 640, 480
ekraan = pygame.display.set_mode((laius, kõrgus))
pygame.display.set_caption("Autode mäng")

# Pildid
taust = pygame.image.load("bg_rally.jpg")
punane_auto = pygame.image.load("f1_red.png")
sinine_auto = pygame.image.load("f1_blue.png")

# Punase auto asukoht
punane_x = laius // 2 - punane_auto.get_width() // 2
punane_y = kõrgus - punane_auto.get_height() - 10

# Siniste autode algväärtused
sinine_autod = []
for i in range(2):  # 3 sinist autot
    x = random.randint(100, laius - 100)
    y = random.randint(-350, -100)
    sinine_autod.append([x, y])

# Font ja skoor
font = pygame.font.SysFont(None, 36)
skoor = 0

# Kella taimer
kell = pygame.time.Clock()
kiirus = 4
töötab = True

while töötab:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            töötab = False

    # Taust
    ekraan.blit(taust, (0, 0))

    # Punane auto
    ekraan.blit(punane_auto, (punane_x, punane_y))

    # Sinised autod
    for auto in sinine_autod:
        auto[1] += kiirus
        ekraan.blit(sinine_auto, (auto[0], auto[1]))

        # Kui auto jõuab alla, liigub uuesti üles ja lisab skoori
        if auto[1] > kõrgus:
            auto[1] = random.randint(-400, -100)
            auto[0] = random.randint(100, laius - 100)
            skoor += 1

    # Skoori kuvamine
    skoori_tekst = font.render("Skoor: " + str(skoor), True, (255, 255, 255))
    ekraan.blit(skoori_tekst, (10, 10))

    pygame.display.flip()
    kell.tick(60)

pygame.quit()
