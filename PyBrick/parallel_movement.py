from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

track_motor = Motor(Port.A)
gripper_motor = Motor(Port.B)

track_motor.run_angle(500, 360, wait=False)
gripper_motor.run_angle(200, 720, wait=False)

#wait to complete
while not track_motor.done() or not gripper_motor.done():
    wait(10)

print("Both motors are done")