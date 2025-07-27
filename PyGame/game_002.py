import pygame
from math import pi

#Initialize Game
pygame.init()

#Screen configuration
size=[400,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Coding Class")

done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill("white")

    pygame.draw.rect(screen,"green",(50,50,150,150))

    pygame.display.flip()

pygame.quit()