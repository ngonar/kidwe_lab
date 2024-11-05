from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

motor.run(700)
wait(1500)
motor.stop()
wait(1500)

motor.run(700)
wait(1500)
motor.brake()
wait(1500)

motor.run(700)
wait(1500)
motor.hold()
wait(1500)

motor.run(700)
wait(1500)
motor.run(0)
wait(1500)