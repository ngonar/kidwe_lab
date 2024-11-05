from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

sensor = ColorSensor(Port.C)

while True:
    color = sensor.color()

    reflection = sensor.reflection()

    print(color, reflection)

    wait(100)