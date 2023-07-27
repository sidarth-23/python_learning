import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("arrow")
tim.pendown()

num_sides = int(input("Enter the number of sides of the final shape: "))


def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        tim.forward(100)
        tim.right(angle)


for i in range(3, num_sides + 1):
    tim.color(random.choice(["blue", "red", "green", "black"]))
    draw_shape(i)

screen = Screen()
screen.exitonclick()
