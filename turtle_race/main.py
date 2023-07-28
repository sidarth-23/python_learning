import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which color turtle do you think will win?: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = True
winner = ""

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(x=-230, y=y_positions[turtle_index])
    tim.speed(8)
    all_turtles.append(tim)

while is_race_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0, 20))
        position = turtle.pos()
        if position[0] >= 200:
            winner = turtle.color()
            is_race_on = False

if user_bet == winner[0]:
    print("You win")
else:
    print(f"You lose, the winner is {winner[0]}")
screen.exitonclick()

