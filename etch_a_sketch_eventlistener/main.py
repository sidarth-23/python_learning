from turtle import Turtle, Screen

tim = Turtle()
tim.speed(6)


def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def counter_clock():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clock():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_screen():
    tim.home()
    tim.clear()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clock)
screen.onkey(key="d", fun=clock)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
