from turtle import *


def draw_square(length=100):
    for i in range(4):
        forward(length)
        right(90)

setup(500, 500)
penup()
pencolor('red')
goto(-100,100)
pendown()
shape('turtle')
for i in range(1):
    draw_square(100)
    right(5)


exitonclick()