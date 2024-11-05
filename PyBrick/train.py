from pybricks.parameters import Color, Direction, Port
from pybricks.pupdevices import ColorDistanceSensor, DCMotor
from pybricks.tools import wait

# Set up custom colors.
Color.RED_TILE = Color(356, 96, 84)
Color.BLUE_TILE = Color(222, 92, 75)
Color.TRACKS = Color(240, 30, 30)
Color.FLOOR = Color(359, 20, 42)

# Set up all devices.
sensor = ColorDistanceSensor(Port.A)
sensor.detectable_colors((Color.RED_TILE, Color.BLUE_TILE, Color.TRACKS, Color.FLOOR))
train = DCMotor(Port.B, Direction.CLOCKWISE)


# The main program starts here.
while True:
    train.dc(40)
    while not sensor.color() == Color.RED_TILE:
        wait(1)
    train.stop()
    wait(500)
    train.dc(-40)
    while not sensor.color() == Color.BLUE_TILE:
        wait(1)
    train.stop()
    wait(500)