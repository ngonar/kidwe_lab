from pybricks.pupdevices import Motor
from pybricks.parameters import Port

motor = Motor(Port.A)
motor.reset_angle(0)
motor.reset_angle(1234)

motor.reset_angle()