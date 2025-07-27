import pygame, sys, os
from pygame.locals import *

#pygame.init()

print(dir(pygame))

class Punch(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("brick.png")
        self.rect = pygame.image.load("brick.png")
        self.mask = pygame.mask.from_surface(self.image)


p1 = Punch()
p2 = Punch()

if pygame.sprite.spritecollide(p1,p2,False, pygame.sprite.collide_mask):
    print("Sprites have collided")