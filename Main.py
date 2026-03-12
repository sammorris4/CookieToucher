from tokenize import group

import pygame
import random
import sys

# define screen dimensions
screenWidth = 1000
screenHeight = 700

# define screen as a variable containing the main display
screen = pygame.display.set_mode((screenWidth, screenHeight))
# define clock as a variable containing the "clock" of the pygame import
clock = pygame.time.Clock()

# define list of chocolate chips coordinates (empty)
chocoChips = []
numberOfChips = 3
# makes a list of coordinates (relative to the cookie base)
for chips in range(numberOfChips):
    chipX = random.randrange(-10, 10)
    chipY = random.randrange(-10, 10)
    chocoChips.append((chipX, chipY))

# makes a cookie at (x, y) with chocolate chips in specified places on the cookie
def cookie(x, y):
    global chipX, chipY
    pygame.draw.circle(screen, (255, 218, 116), (x, y), 20)
    for chipX, chipY in chocoChips:
        pygame.draw.circle(screen, (123, 63, 0), (chipX + x, chipY + y), 5)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# was thinking of using something like this (but actually working)-
# -to spawn in a single cookie at the start of the game
def runOnce(fn):
    global runOnceTemp
    if runOnceTemp == 0:
        return None
    elif runOnceTemp == 1:
        runOnceTemp -= 1
        return fn
    else:
        return None
runOnceTemp = 1



# creates the list of coordinates for the amount of cookies specified in numberOfCookies
cookies = []
numberOfCookies = 10
for i in range(numberOfCookies):
    x = random.randrange(20, 680)
    y = random.randrange(20, screenHeight - 20)
    cookies.append((x, y))

# Action Area (LOOPS OVER AND OVER CONSTANTLY)
running = True
while running:
    # bg (starts the next frame)
    screen.fill((255, 253, 208))

    # creates cookies based on a preset list of coordinates
    if numberOfCookies > 0:
        for x, y in cookies:
            cookie(x, y)
    # declares what the player icon will look like (WIP)
    player = pygame.draw.circle(screen, (0, 0, 0), player_pos, 30)

    # movement
    keys = pygame.key.get_pressed()
    dt = clock.tick(60) / 1000
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # covers up anything below to reset the screen, prepping it for the next frame
    pygame.display.flip()
pygame.quit()