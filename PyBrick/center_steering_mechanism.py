from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

left_end = motor.run_until_stalled(-200, duty_limit=30)
right_end = motor.run_until_stalled(200, duty_limit=30)

motor.reset_angle((right_end-left_end)/2)

motor.run_target(200, 0)

wait(1000)