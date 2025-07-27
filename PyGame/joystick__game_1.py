import pygame


window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

screen_width, screen_height = window.get_size()
rect = pygame.Rect(screen_width/2, screen_height/2, 20, 20)

move_threshold = 0.01

def test_joysticks():
    pygame.init()
    pygame.joystick.init()

    num_joysticks = pygame.joystick.get_count()
    if num_joysticks == 0:
        print("No joysticks found.")
        return

    print(f"Found {num_joysticks} joystick(s).")
    joystick = None
    joysticks = [pygame.joystick.Joystick(i) for i in range(num_joysticks)]
    for joystick in joysticks:
        joystick.init()
        joystick = pygame.joystick.Joystick(0)
        print(f"\nJoystick Name: {joystick.get_name()}")
        print(f"Number of Axes: {joystick.get_numaxes()}")
        print(f"Number of Buttons: {joystick.get_numbuttons()}")
        print(f"Number of Hats: {joystick.get_numhats()}")
        print(f"Number of Balls (Trackballs): {joystick.get_numballs()}")

    running = True
    move = "center"
    x, y = 0, 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} on joystick {event.joy} moved to {event.value:.2f}")
                # if event.axis == 0: #X
                # #    rect.x += event.value
                #     if event.value < move_threshold * -1:
                #         move = "left"
                #     elif event.value > move_threshold:
                #         move = "right"
                #     else:
                #         move = "center"
                #
                #     #print("move x axis ",event.value)
                # elif event.axis == 1: #Y
                #     if event.value < move_threshold * -1:
                #         move = "up"
                #     elif event.value > move_threshold:
                #         move = "down"
                #     else:
                #         move = "center"
                #     #print("move y axis ",event.value)
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} on joystick {event.joy} pressed.")

            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} on joystick {event.joy} released.")

            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} on joystick {event.joy} moved to {event.value}.")
                x , y = event.value
                #rect.x  += x
                #rect.y += y

                if x == 1:
                    move = "right"
                elif x == -1:
                    move = "left"
                elif y == 1:
                    move = "up"
                elif y == -1:
                    move = "down"
                else:
                    move = "center"

            elif event.type == pygame.JOYBALLMOTION:
                print(f"Trackball {event.ball} on joystick {event.joy} moved by {event.rel}.")


        # if move == "left":
        #     rect.x -= 1
        # elif move == "right":
        #     rect.x += 1
        # elif move == "up":
        #     rect.y -= 1
        # elif move == "down":
        #     rect.y += 1
        rect.x += x
        rect.y -= y



        pygame.time.Clock().tick(60) # Limit frame rate

        window.fill((0, 0, 64))
        pygame.draw.rect(window, (255, 64, 64), rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    test_joysticks()