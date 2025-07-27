import pygame
from pygame.display import set_caption

set_caption("Coding Class")

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(30, 200)

movement_x = 1
movement_y = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((122, 220, 180))

    pygame.draw.circle(screen, (252, 185, 0), player_pos, 40)

    player_pos.x += 300 * dt * movement_x
    player_pos.y += 300 * dt * movement_y

    if player_pos.y>screen.get_height():
        movement_y *= -1
    if player_pos.y<=0:
        movement_y *= -1
    if player_pos.x>screen.get_width():
        movement_x *= -1
    if player_pos.x<=0:
        movement_x *= -1



    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
