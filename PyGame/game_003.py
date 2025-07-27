import pygame, sys, random
from pygame.locals import *
from spritesheet import SpriteSheet
#from pygame_functions import *
 
pygame.init()
 
clock = pygame.time.Clock()
fps = 30
 
DisplaySurface_Width = 480
DisplaySurface_Height = 640
DisplaySurface = pygame.display.set_mode((DisplaySurface_Height, DisplaySurface_Width))
pygame.display.set_caption("Boat Game")
 

boat_ss = SpriteSheet("rowboat.bmp")

boat_rect = (97,12,100,50)

boatIMG = boat_ss.image_at(boat_rect)

#boatIMG = pygame.Surface(boatIMG.get_size()).convert_alpha()
#boatIMG.fill((0,0,0))

backgroundIMG = pygame.image.load("Ocean.png")
backgroundIMG = pygame.transform.scale(backgroundIMG, (DisplaySurface_Height, DisplaySurface_Width))


heartIMG = pygame.image.load("00_items.png")
enemy_bullet = pygame.image.load("M484BulletCollection2.png")


 
 
 
def bullet(bX, bY):
    DisplaySurface.blit(enemy_bullet, (bX,bY))
 
 
def boat(x, y):
    DisplaySurface.blit(boatIMG,(x,y))
 
game_Exit = False
 
def game_loop():
 
    boatx = 400
    boaty = 400
    bulletX = random.randint(200, 500)
    bulletY = -100
    bullet_Speed = 5
 
    while not game_Exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys, exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                boatx -= 5
            elif event.key == pygame.K_RIGHT:
                boatx += 5
            elif event.key == pygame.K_UP:
                boaty -= 5
            elif event.key == pygame.K_DOWN:
                boaty += 5
 
            if boatx == 120:
                boatx = 125
            elif boatx == 460:
                boatx = 455
            elif boaty == 300:
                boaty = 305
            elif boaty == 410:
                boaty = 405
 
        DisplaySurface.blit(backgroundIMG, (0, 0))
        boat(boatx, boaty)
        #bullet(bulletX, bulletY)
        hit = False #pygame.sprite.spritecollide(boatIMG, enemy_bullet, False)
 
        if hit:
            pass #Game over
 
        #if bulletY == 480:
        #    bulletX = random.randint(200, 500)
        #    bulletY = -100
 
 
        bulletY += bullet_Speed
        pygame.display.update()
        clock.tick(fps)
 
game_loop()
pygame.quit()
quit()