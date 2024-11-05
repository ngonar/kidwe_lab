from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

distance = UltrasonicSensor(Port.A)

while True:
    print(distance.distance())
    distance.lights.on(distance.distance())
    wait(1000)