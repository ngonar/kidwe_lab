from turtle import *

from pygame import color


def draw_star(length=100):
    for i in range(5):
        forward(length)
        right(144)

setup(500, 500,10,10)
penup()
goto(0,0)
print("x")
# penup()
# begin_fill()

# pencolor('red')
# pensize(1)
pendown()
# shape('turtle')
# star_side = 100
# for i in range(1):
#     draw_star(star_side)
#     right(5)
#     star_side += 5
# end_fill()
exitonclick()
#done()