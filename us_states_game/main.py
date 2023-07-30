import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
found_states = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(found_states)}/{len(states_list)} States found", prompt="What's another state name?").title()

    if len(found_states) >= 50 or answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in found_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list and answer_state not in found_states:
        found_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        temp_answer = data[data.state == answer_state]
        t.goto(int(temp_answer.x), int(temp_answer.y))
        t.write(answer_state)

screen.mainloop()
