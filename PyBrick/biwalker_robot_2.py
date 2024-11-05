from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

#initial
left_leg = Motor(Port.A)
right_leg = Motor(Port.B)
tail = Motor(Port.F)

print("Reset")
tail.run_target(200,0)
left_leg.run_target(200,0)
right_leg.run_target(200,0)


while(True):
    tail.run_target(100,-60)
    left_leg.run_target(100,30)

    tail.run_target(100,60)
    left_leg.run_target(100,0)

    tail.run_target(100,60)
    right_leg.run_target(100, -30)

    tail.run_target(100,-60)
    right_leg.run_target(100,0)