import pygame
import math
import random

# initialise pygame
pygame.init()
# creating window of game
screen = pygame.display.set_mode((600, 600))
# title & image
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load('spacecraft.png')
pygame.display.set_icon(icon)
# player and stars
playerimg = pygame.image.load('player.png')
PX = 280
PY = 450
player_horizontal = 0
player_vertical = 0
# bullet
bulletimg = pygame.image.load('bullet.png')
BX = 0
BY = 445
B_Y = 0.5
Bulletstate = "ready"
# enemy
enemyimg = []
AX = []
AY = []
enemy_H = []
enemy_Y = []
no_of_enemy = 6
for i in range(no_of_enemy):
    enemyimg.append(pygame.image.load('alien.png'))
    AX.append(random.randint(70, 530))
    AY.append(random.randint(30, 100))
    enemy_H.append(0.3)
    enemy_Y.append(30)
# scoring
score = 0
font = pygame.font.Font("freesansbold.ttf", 28)
TX = 10
TY = 10


def score_val(x, y):
    scoring = font.render("SCORE: " + str(score), True, (255, 255, 0))
    screen.blit(scoring, (x, y))


# calling player and enemy
def player(x, y):
    screen.blit(playerimg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))


def fire(x, y):
    global Bulletstate
    Bulletstate = "fire"
    screen.blit(bulletimg, (x + 5, y + 6))


def collision(AX, AY, BX, BY):
    distance = math.sqrt((math.pow(AX - BX, 2)) + (math.pow(AY - BY, 2)))
    if distance <= 40:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # screen colour
    screen.fill((17, 0, 51))
    # BACKGROUND
    # background = pygame.image.load('2474216.jpg')
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # keystrokes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_horizontal -= 0.3
            if event.key == pygame.K_RIGHT:
                player_horizontal += 0.3
            if event.key == pygame.K_SPACE:
                if Bulletstate == "ready":
                    BX = PX
                    fire(BX, BY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_horizontal = 0

    PX += player_horizontal
    if PX <= 0:
        PX = 0
    elif PX >= 567:
        PX = 567
    # enemy movement
    for i in range(no_of_enemy):

        AX[i] += enemy_H[i]
        if AX[i] <= 0:
            enemy_H[i] = 0.3
            AY[i] += enemy_Y[i]

        elif AX[i] >= 550:
            enemy_H[i] = -0.3
            AY[i] += enemy_Y[i]
        enemy(AX[i], AY[i], i)

        coll = collision(AX[i], AY[i], BX, BY)
        if coll:
            BY = 445
            Bulletstate = "ready"
            score += 10
            AX[i] = random.randint(70, 530)
            AY[i] = random.randint(30, 100)
    # bullet movement
    if BY <= 0:
        BY = 445
        Bulletstate = "ready"
    if Bulletstate == "fire":
        fire(BX, BY)
        BY -= B_Y
    score_val(TX, TY)
    player(PX, PY)
    pygame.display.update()
