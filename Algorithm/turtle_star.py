from turtle import *


def draw_star(length=100):
    for i in range(5):
        forward(length)
        right(144)

setup(500, 500)
penup()
pencolor('red')

pendown()
shape('turtle')
star_side = 100
for i in range(60):
    draw_star(star_side)
    right(5)
    star_side += 5

exitonclick()
#done()