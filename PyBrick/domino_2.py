from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor, ForceSensor
from pybricks.robotics import DriveBase
from pybricks.tools import wait

from micropython import mem_info

# Print memory usage.
mem_info()

# Set up all devices.
prime_hub = PrimeHub()
motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
motor_2 = Motor(Port.E, Direction.CLOCKWISE)
motor_3 = Motor(Port.F)
drive_base = DriveBase(motor, motor_2, 56, 114)

button = ForceSensor(Port.A)


while True:

    if button.force() >= 0.5:

        for i in range(4):
            #motor_3.reset_angle(0)
            # The main program starts here.
            #prime_hub.display.number(i)
            drive_base.straight(30)
            #drive_base.curve(100,90)
            #drive_base.turn(90)
            motor_3.run(230)
            wait(3000)
            motor_3.run(-230)
            wait(3000)

            motor_3.reset_angle(0)

        #break
