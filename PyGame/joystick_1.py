import pygame

def test_joysticks():
    pygame.init()
    pygame.joystick.init()

    num_joysticks = pygame.joystick.get_count()
    if num_joysticks == 0:
        print("No joysticks found.")
        return

    print(f"Found {num_joysticks} joystick(s).")

    joysticks = [pygame.joystick.Joystick(i) for i in range(num_joysticks)]
    for joystick in joysticks:
        joystick.init()
        print(f"\nJoystick Name: {joystick.get_name()}")
        print(f"Number of Axes: {joystick.get_numaxes()}")
        print(f"Number of Buttons: {joystick.get_numbuttons()}")
        print(f"Number of Hats: {joystick.get_numhats()}")
        print(f"Number of Balls (Trackballs): {joystick.get_numballs()}")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} on joystick {event.joy} moved to {event.value:.2f}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} on joystick {event.joy} pressed.")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} on joystick {event.joy} released.")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} on joystick {event.joy} moved to {event.value}.")
            elif event.type == pygame.JOYBALLMOTION:
                print(f"Trackball {event.ball} on joystick {event.joy} moved by {event.rel}.")

        pygame.time.Clock().tick(60) # Limit frame rate

    pygame.quit()

if __name__ == "__main__":
    test_joysticks()