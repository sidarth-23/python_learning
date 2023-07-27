import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.speed(0)
turtle.colormode(255)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


no_of_circles = int(input("Enter the no. of circles in spirograph: "))
increment = 360 / no_of_circles
angle = 0

while angle < 360:
    tim.right(increment)
    tim.color(colors())
    tim.circle(100)
    angle += increment




screen = Screen()
screen.exitonclick()
