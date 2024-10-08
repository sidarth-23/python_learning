import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    topic.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 2 == 1:
        topic.config(text="Work Time", fg=GREEN)
        count_down(work_secs)
    elif reps % 8 == 0:
        topic.config(text="Long Break", fg=RED)
        count_down(long_break_secs)
    else:
        topic.config(text="Short Break", fg=PINK)
        count_down(short_break_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    check_mark_text = "✔️"
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        temp_check_mark = ""
        for _ in range(math.floor(reps / 2)):
            temp_check_mark += check_mark_text
        check_marks.config(text=temp_check_mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

topic = Label()
topic.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
topic.grid(row=0, column=1)

start_button = Button()
start_button.config(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button()
reset_button.config(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(row=3, column=1)

window.mainloop()
