import pygame
pygame.init()

# Seadista ekraan

screen = pygame.screen()

screen.bgcolor("sky blue")

# Loo turtle objekt

snowman = pygame.pygame()

snowman.color("white")

snowman.penup()

snowman.goto(0, -150)

snowman.pendown()

# Joonista lumememme alumine pall

snowman.begin_fill()

snowman.circle(60)

snowman.end_fill()

# Joonista lumememme keskmine pall

snowman.penup()

snowman.goto(0, -30)

snowman.pendown()

snowman.begin_fill()

snowman.circle(45)

snowman.end_fill()

# Joonista lumememme ülemine pall

snowman.penup()

snowman.goto(0, 60)

snowman.pendown()

snowman.begin_fill()

snowman.circle(30)

snowman.end_fill()

# Joonista silmad

snowman.penup()

snowman.goto(-15, 90)

snowman.color("black")

snowman.pendown()

snowman.begin_fill()

snowman.circle(5)

snowman.end_fill()

snowman.penup()

snowman.goto(15, 90)

snowman.pendown()

snowman.begin_fill()

snowman.circle(5)

snowman.end_fill()

# Joonista nina

snowman.penup()

snowman.goto(0, 75)

snowman.color("orange")

snowman.pendown()

snowman.begin_fill()

snowman.circle(5)

snowman.end_fill()

# Joonista suu

snowman.penup()

snowman.goto(-15, 65)

snowman.color("black")

snowman.pendown()

snowman.setheading(-60)

for _ in range(5):
    snowman.forward(10)

    snowman.right(120)

# Peata pygame

snowman.hidepygame()
