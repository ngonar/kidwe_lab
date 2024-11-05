from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

sensor = ColorSensor(Port.C)

def wait_for_color(desired_color):
    while sensor.color() != desired_color:
        wait(20)


while True:
    print("Waiting for red")
    wait_for_color(Color.RED)

    print("waiting for blue")
    wait_for_color(Color.BLUE)