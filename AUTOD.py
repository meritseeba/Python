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

# Tee ala (vältimaks muru)
tee_algus = 120
tee_lõpp = laius - 120
raja_laius = (tee_lõpp - tee_algus) // 3
rajad = [tee_algus + raja_laius * i + (raja_laius - punane_auto.get_width()) // 2 for i in range(3)]

# Punane auto algab keskmisel rajal
punane_rada = 1
punane_x = rajad[punane_rada]
punane_y = kõrgus - punane_auto.get_height() - 10

# Sinised autod (vältivad punase rada)
sinine_autod = []
for _ in range(3):
    rada = random.choice([i for i in range(3) if i != punane_rada])
    x = rajad[rada]
    y = random.randint(-480, -150)
    sinine_autod.append([x, y, rada])

# Font ja skoor
font = pygame.font.SysFont(None, 36)
skoor = 0
kell = pygame.time.Clock()
kiirus = 4
töötab = True

while töötab:
    for sündmus in pygame.event.get():
        if sündmus.type == pygame.QUIT:
            töötab = False

    # Liikumine rajal
    klahvid = pygame.key.get_pressed()
    if klahvid[pygame.K_LEFT] and punane_rada > 0:
        punane_rada -= 1
        punane_x = rajad[punane_rada]
    if klahvid[pygame.K_RIGHT] and punane_rada < 2:
        punane_rada += 1
        punane_x = rajad[punane_rada]

    # Taust ja punane auto
    ekraan.blit(taust, (0, 0))
    ekraan.blit(punane_auto, (punane_x, punane_y))

    # Sinised autod
    for auto in sinine_autod:
        auto[1] += kiirus
        ekraan.blit(sinine_auto, (auto[0], auto[1]))

        # Kui jõuab alla, ilmub uuesti üles, vältides punase rada
        if auto[1] > kõrgus:
            rada = random.choice([i for i in range(3) if i != punane_rada])
            auto[0] = rajad[rada]
            auto[1] = random.randint(-480, -50)
            auto[2] = rada
            skoor += 1

    # Skoor
    tekst = font.render(f"Skoor: {skoor}", True, (255, 255, 255))
    ekraan.blit(tekst, (10, 10))

    pygame.display.flip()
    kell.tick(60)

pygame.quit()
