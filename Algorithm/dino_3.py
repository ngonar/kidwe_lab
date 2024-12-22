import pygame
from pygame.display import set_caption


def draw_the_dino(screen, dino_pos):

    x = dino_pos.x
    y = dino_pos.y

    #############body##############

    #tail
    pygame.draw.rect(screen, "green", (50 + x, 50 + y, 50, 20))

    #rear leg
    fr_leg_x = 105 + x
    fr_leg_y = 50 + y
    fr_leg_w = 20
    fr_leg_h = 60
    move_fr = x % 25
    limit_fr = 25
    if (move_fr > limit_fr):
        move_fr *= -1

    pygame.draw.polygon(screen, "green",
                        [(fr_leg_x, fr_leg_y), (fr_leg_x + fr_leg_w, fr_leg_y),
                         (fr_leg_x + fr_leg_w - move_fr, fr_leg_y + fr_leg_h),
                         (fr_leg_x - move_fr, fr_leg_y + fr_leg_h)])

    #body
    pygame.draw.rect(screen, "green", (130 + x, 50 + y, 20, 40))

    #front leg
    bk_leg_x = 155 + x
    bk_leg_y = 50 + y
    bk_leg_w = 20
    bk_leg_h = 60
    move_bk = x % 25
    limit_bk = 25
    if (move_bk < limit_bk):
        move_bk *= -1
    #pygame.draw.rect(screen, "green", (155 + x, 50 + y, 20, 60))
    pygame.draw.polygon(screen, "green",
                        [(bk_leg_x, bk_leg_y), (bk_leg_x + bk_leg_w, bk_leg_y),
                         (bk_leg_x + bk_leg_w - move_bk, bk_leg_y + bk_leg_h),
                         (bk_leg_x - move_bk, bk_leg_y + bk_leg_h)])

    #head
    pygame.draw.rect(screen, "green", (180 + x, 50 + y, 50, 35))

    #eyes
    pygame.draw.rect(screen, "red", (190 + x, 60 + y, 10, 10))
    pygame.draw.rect(screen, "red", (210 + x, 60 + y, 10, 10))


if __name__ == '__main__':
    set_caption("KidWe Lab - Coding Class")

    pygame.init()
    screen = pygame.display.set_mode((700, 400))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    dino_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))

        draw_the_dino(screen, dino_pos)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dino_pos.y -= 300 * dt
        if keys[pygame.K_DOWN]:
            dino_pos.y += 300 * dt
        if keys[pygame.K_LEFT]:
            dino_pos.x -= 300 * dt
        if keys[pygame.K_RIGHT]:
            dino_pos.x += 300 * dt

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()
