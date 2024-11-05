from pybricks.hubs import PrimeHub
from pybricks.parameters import Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase

from micropython import mem_info

# Print memory usage.
mem_info()

# Set up all devices.
prime_hub = PrimeHub()
motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_2 = Motor(Port.B, Direction.CLOCKWISE)
drive_base = DriveBase(motor, motor_2, 56, 114)


# The main program starts here.
prime_hub.display.number(42)
drive_base.straight(250)
drive_base.curve(100,90)
drive_base.turn(90)