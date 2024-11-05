from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

motor = Motor(Port.A)

motor.run_angle(700, 360)
wait(1000)

motor.run_angle(700, 360, then=Stop.HOLD)
wait(1000)

motor.run_angle(700, 360, then=Stop.BRAKE)
wait(1000)

motor.run_angle(700, 360, then=Stop.COAST)
wait(1000)