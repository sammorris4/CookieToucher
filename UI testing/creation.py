from tokenize import group

import pygame
import random
import sys
pygame.init()
pygame.font.init()

screenWidth = 1000
screenHeight = 700

screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 30)


def cookie(x, y):
    pygame.draw.circle(screen, (255, 218, 116), (x, y), 20)
    for n in range(3):
        chipsX = random.randrange(-10, 10)
        chipsY = random.randrange(-10, 10)
        pygame.draw.circle(screen, (123, 63, 0), (x + chipsX, y + chipsY), 5)
def UI():
    pygame.draw.rect(screen, (211, 182, 131), (screenWidth-300, 0, screenWidth, screenHeight))
    y=25
    for i in range(5):
        pygame.draw.rect(screen, (255, 162, 131), (screenWidth - 250, y + 20, 75, 100))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

cookies = []
for i in range(random.randrange(10, 20)):
    cookies.append((random.randrange(10, 690), random.randrange(10, 690)))

#def updateUI():


running = True

while running:

    dt = clock.tick(60) / 1000

    screen.fill((255, 253, 208))

    # draw cookies
    for c in cookies:
        cookie(c[0], c[1])
    UI()
    # move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    player = pygame.draw.circle(screen, (0, 0, 0), player_pos, 30)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
sys.exit()
