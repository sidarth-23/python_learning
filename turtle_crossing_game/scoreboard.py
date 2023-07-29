from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.level = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.write("Level : " + str(self.level), font=FONT, align="center")
        self.add_score()

    def add_score(self):
        self.level += 1

    def end_game_screen(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT, align="center")

