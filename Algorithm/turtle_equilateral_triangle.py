from turtle import *


def draw_triangle(length=100):
    for i in range(3):
        forward(length)
        right(120)

setup(500, 500)
penup()
pencolor('red')
#goto(-100,100)
pendown()
shape('turtle')
for i in range(60):
    draw_triangle(100)
    right(5)


exitonclick()
#done()