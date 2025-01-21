import math
from turtle import *


def draw_circle(radis):
    circumfrence = 2 * math.pi * radis
    step_size = circumfrence / 360
    for _ in range(360):
        forward(step_size)
        left(1)

setup(500, 500)
penup()
pencolor('red')
goto(-100,100)
pendown()
shape('turtle')
for i in range(1):
    draw_circle(100)
    right(5)


exitonclick()