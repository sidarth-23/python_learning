import turtle
from turtle import Turtle, Screen
import random


tim = Turtle()
turtle.colormode(255)
tim.shape("arrow")
tim.speed(0)
tim.pensize(5)

turning = [0, 90, 270, 360]
size_of_walk = int(input("Enter the size of the walk: "))


def color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final = (r, g, b)
    return final


for _ in range(size_of_walk):
    tim.color(color())
    tim.forward(50)
    tim.right(random.choice(turning))

screen = Screen()
screen.screensize(3000, 3000)
screen.exitonclick()
