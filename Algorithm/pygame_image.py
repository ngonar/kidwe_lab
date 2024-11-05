import pygame
import os

#Initialize Game
pygame.init()

#Screen configuration
size=[400,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Kidwe Lab Coding Class")

done = False
clock = pygame.time.Clock()

star = pygame.image.load(os.path.join('img', 'star.png'))

# Set the size for the image
DEFAULT_IMAGE_SIZE = (50, 50)

# Scale the image to your needed size
star = pygame.transform.scale(star, DEFAULT_IMAGE_SIZE)

while not done:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill("white")

    screen.blit(star, (screen.get_width()/2, screen.get_height()/2))
    pygame.draw.rect(screen, "green", (50, 50, 150, 150))

    pygame.display.flip()

pygame.quit()