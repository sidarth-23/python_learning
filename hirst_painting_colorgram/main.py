import turtle

import colorgram
from turtle import Turtle, Screen

tim = Turtle()
turtle.colormode(255)
tim.speed(0)
tim.penup()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_colors.append(color.rgb)

print(rgb_colors)

i = 0
for _ in range(3):
    for _ in range(10):
        tim.forward(20)
        tim.dot(10, rgb_colors[i])
        i += 1
    tp = tim.pos()
    pos_y = tp[1]
    tim.sety(pos_y + 20)
    tim.right(180)


screen = Screen()
screen.exitonclick()