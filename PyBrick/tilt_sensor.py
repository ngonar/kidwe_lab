from pybricks.hubs import PrimeHub
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

while True:
    pitch, roll = hub.imu.tilt()

    print("Pitch:", pitch, "Roll:",roll)

    wait(100)