from turtle import *


def draw_square(length=100):
    for i in range(4):
        forward(length)
        right(90)

setup(500, 500)
penup()
pencolor('red')
#goto(-100,100)
pendown()
shape('turtle')
square_side = 100
for i in range(60):
    draw_square(square_side)
    right(5)
    square_side+=5


exitonclick()
#done()