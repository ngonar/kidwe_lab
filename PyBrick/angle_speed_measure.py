from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

motor.run(300)

for i in range(5):
    angle = motor.angle()
    speed = motor.speed()

    print(angle, speed)

    wait(200)

motor.reset_angle(100)

for i in range(5):
    angle = motor.angle()
    speed = motor.speed()

    print(angle, speed)

    wait(200)