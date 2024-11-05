import pygame

#Initialize Game
pygame.init()

#Screen configuration
size=[300,300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Kidwe Lab Coding Class")

done = False
clock = pygame.time.Clock()

while not done:

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill("white")

    #Draw your shapes here
    pygame.draw.rect(screen,"green",(50,150,30,75))

    #Finish your drawing

    pygame.display.flip()

pygame.quit()