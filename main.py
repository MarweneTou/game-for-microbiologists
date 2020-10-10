import pygame
import random
import math
from pygame import mixer


pygame.init()

screen = pygame.display.set_mode((800, 600))
# Backgrounds
background = pygame.image.load("/home/marwene/Downloads/background_water.jpg")
background = pygame.transform.scale(background, (800, 600))
mixer.music.load("/home/marwene/Downloads/background_music.mp3")
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("The Invader")
# icon = pygame.image.load("/home/marwene/Downloads/icon.png")
# pygame.display.set_icon(icon)

# monsters
monster_image = pygame.image.load("/home/marwene/Downloads/monster.png")
monster_image = pygame.transform.scale(monster_image, (210, 206))
monsterX = random.randint(0, 600)
monsterY = random.randint(50, 150)
monsterX_change = 2
monsterY_change = 40

# player
player_image = pygame.image.load("/home/marwene/Downloads/bacteria.png")
player_image = pygame.transform.scale(player_image, (60, 56))
playerX = 370
playerY = 510
playerX_change = 0

# enemies 1
enemy_image = []
enemy_image1 = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
type_of_enemy = ["virus.png", "virus1.png", "virus2.png", "virus3.png", "virus4.png", "virus5.png"]

for i, j in zip(range(num_of_enemies), type_of_enemy):
    enemy_image.append((pygame.image.load("/home/marwene/Downloads/{}".format(j))))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(40)

for enem in enemy_image:
    enemy_image1.append(pygame.transform.scale(enem, (70, 66)))

# enemies 2
enemy2_image = []
enemy2_image1 = []
enemy2X = []
enemy2Y = []
enemy2X_change = []
enemy2Y_change = []
num_of_enemies2 = 6
type_of_enemy2 = ["AB.png", "AB1.png", "AB2.png", "AB3.png", "AB4.png", "AB5.png"]

for i, j in zip(range(num_of_enemies2), type_of_enemy2):
    enemy2_image.append((pygame.image.load("/home/marwene/Downloads/{}".format(j))))
    enemy2X.append(random.randint(0, 735))
    enemy2Y.append(random.randint(50, 150))
    enemy2X_change.append(2)
    enemy2Y_change.append(40)

for enem in enemy2_image:
    enemy2_image1.append(pygame.transform.scale(enem, (40, 36)))

# weapon 1
weapon_image = pygame.image.load("/home/marwene/Downloads/crisper.svg")
weapon_image = pygame.transform.scale(weapon_image, (40, 36))
weaponX = 0
weaponY = 480
weaponX_change = 0
weaponY_change = 4
weapon_state = "ready"

score_monster = 0
score_value = 0
font = pygame.font.Font("/home/marwene/Downloads/Cartoon Comic.ttf", 32)
over_font = pygame.font.Font("/home/marwene/Downloads/Cartoon Comic.ttf", 64)
wonfont = pygame.font.Font("/home/marwene/Downloads/Cartoon Comic.ttf", 64)
textX = 10
textY = 10


def monster(x, y):
    screen.blit(monster_image, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (189, 250))

def won_text():
    won_text = wonfont.render("YOU WON", True, (255, 255, 255))
    screen.blit(won_text, (189, 250))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (textX, textY))


def player(x, y):
    screen.blit(player_image, (playerX, playerY))


def enemy(x, y, i):
    screen.blit(enemy_image1[i], (x, y))


def enemy2(x, y, i):
    screen.blit(enemy2_image1[i], (x, y))


def fire_weapon(x, y):
    global weapon_state
    weapon_state = "fire"
    screen.blit(weapon_image, (x + 10, y + 10))


def is_collision(enemyX, enemyY, weaponX, weaponY):
    distance = math.sqrt((math.pow(enemyX - weaponX, 2)) + (math.pow(enemyY-weaponY, 2)))
    if distance < 27:
        return True
    return False


def is_collision_monster(monsterX, monsterY, weaponX, weaponY):
    distance_monster = math.sqrt((math.pow(monsterX - weaponX, 2)) + (math.pow(monsterY - weaponY, 2)))
    if distance_monster < 87:
        return True
    return False




# game loop
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 3.2

            if event.key == pygame.K_SPACE:
                if weapon_state == "ready":
                    shot_sound = mixer.Sound("/home/marwene/Downloads/bullet_sound.wav")
                    shot_sound.play()
                    weaponX = playerX
                    fire_weapon(weaponX, weaponY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # monster
    if score_value == 15:
        monster(monsterX, monsterY)
        for j in range(num_of_enemies):
            enemyY[j] = -2000
        monsterX += monsterX_change
        if monsterX <= 0:
            monsterX_change = 4
            monsterY += monsterY_change
        elif monsterX >= 600:
            monsterX_change = -2
            monsterY += monsterY_change
        if monsterY > 308:
            monsterX = 2000
            monsterY = 0
            game_over_text()

    for i in range(num_of_enemies):
        # game over
        if enemyY[i] > 468:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = is_collision(enemyX[i], enemyY[i], weaponX, weaponY)
        if collision:
            col_sound = mixer.Sound("/home/marwene/Downloads/kill.wav")
            col_sound.play()
            weaponY = 480
            weapon_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)

        # collision Monster
        collision_monster = is_collision_monster(monsterX, monsterY, weaponX, weaponY)

        if collision_monster:
            col_sound = mixer.Sound("/home/marwene/Downloads/monster.wav")
            col_sound.play()
            weaponY = 480
            weapon_state = "ready"
            score_monster += 1
            if score_monster == 3:
                score_value += 10
            # wave two of enemies
    if score_value == 25:
        won_text()



    # weapon movement
    if weaponY <= 0:
        weaponY = 480
        weapon_state = "ready"
    if weapon_state == "fire":
        fire_weapon(weaponX, weaponY)
        weaponY -= weaponY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()