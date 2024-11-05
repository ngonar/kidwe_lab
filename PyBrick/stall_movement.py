from pybricks.pupdevices import Motor
from pybricks.parameters import Port

motor = Motor(Port.A)

speed = 200

motor.run_until_stalled(-speed, duty_limit=30)

motor.reset_angle(0)

for count in range(10):
    motor.run_target(speed,180)
    motor.run_target(speed, 90)
