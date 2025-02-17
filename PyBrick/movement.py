from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

motor = Motor(Port.A)

print("Run")
motor.run(500)
wait(1500)
motor.stop()

# wait(1500)

# print("DC")
# motor.dc(50)
# wait(1500)
# motor.stop()
# wait(1500)

# print("Run Time")
# motor.run_time(500,2000)
# wait(1500)

# print("Run angle")
# motor.run_angle(500,90)
# wait(1500)

# print("Run target to 0")
# motor.run_target(500,0)
# wait(1500)

# print("Run target to -90")
# motor.run_target(500, -90)
# wait(1500)

# print("Run until stalled")
# motor.run_until_stalled(500)
# print("Done")
# wait(500)