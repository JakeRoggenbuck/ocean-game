import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Ocean Game")

X = 200
Y = 200

WIDTH = 10
HEIGHT = 10

HORIZONTAL_VEL = 2
VERTICAL_VEL = 1.5

RUN = True

DARK_BLUE = "#1D3557"
MID_BLUE = "#457B9D"
LIGHT_BLUE = "#A8DADC"
WHITE = "#F1FAEE"
RED = "#E63946"

RIGHT_FISH = pygame.image.load("./fish.png")
RIGHT_FISH = pygame.transform.scale(RIGHT_FISH, (80, 80))
LEFT_FISH = pygame.transform.flip(RIGHT_FISH, True, False)

LEFT = 1
RIGHT = 2

DIRECTION = RIGHT

while RUN:
    pygame.time.delay(10)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RUN = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and X > 0:
        X -= HORIZONTAL_VEL
        DIRECTION = LEFT

    if keys[pygame.K_RIGHT] and X < 500 - WIDTH:
        X += HORIZONTAL_VEL
        DIRECTION = RIGHT

    if keys[pygame.K_UP] and Y > 0:
        Y -= VERTICAL_VEL

    if keys[pygame.K_DOWN] and Y < 500 - HEIGHT:
        Y += VERTICAL_VEL

    win.fill(DARK_BLUE)
    fish = RIGHT_FISH if DIRECTION == RIGHT else LEFT_FISH
    win.blit(fish, (X, Y))

    pygame.display.update()

pygame.quit()
