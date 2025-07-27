import pygame

pygame.init()
pygame.joystick.init()

num_joysticks = pygame.joystick.get_count()
if num_joysticks == 0:
    print("No joysticks found.")
else:
    print(f"Found {num_joysticks} joystick(s).")

    joysticks = [pygame.joystick.Joystick(i) for i in range(num_joysticks)]
    for joystick in joysticks:
        joystick.init()
        print(f"\nJoystick Name: {joystick.get_name()}")
        print(f"Number of Axes: {joystick.get_numaxes()}")
        print(f"Number of Buttons: {joystick.get_numbuttons()}")
        print(f"Number of Hats: {joystick.get_numhats()}")
        print(f"Number of Balls (Trackballs): {joystick.get_numballs()}")


window_width = 600
window_height = 300
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

rect = pygame.Rect(135, 220, 30, 30)
vel = 5


jumpMax = 15
jump = False
jumpCount = 0


run = True
while run:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                jump = True
                jumpCount = jumpMax
        if event.type == pygame.KEYDOWN :
            if not jump and event.key == pygame.K_SPACE:
                jump = True
                jumpCount = jumpMax

    keys = pygame.key.get_pressed()
    rect.centerx = (rect.centerx + (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * vel) % window_width

    if jump:
        rect.y -= jumpCount
        if jumpCount > -jumpMax:
            jumpCount -= 1
        else:
            jump = False

    window.fill((0, 0, 64))
    pygame.draw.rect(window, (64, 64, 64), (0, 250, window_width, 100))
    pygame.draw.circle(window, (255, 0, 0), rect.center, 15)
    pygame.display.flip()

pygame.quit()
exit()