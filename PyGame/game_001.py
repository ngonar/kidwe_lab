import pygame
from pygame.display import set_caption

set_caption("Coding Class")

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
dt = 0

wall_touched = False

player_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((122, 220, 180))

    player = pygame.draw.circle(screen, (252, 185, 0), player_pos, 40)

    if not wall_touched:
        wall = pygame.draw.rect(screen,"green",(50,50,100,100))

    if player.colliderect(wall) and not wall_touched:
        print("collision")
        wall_touched = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
