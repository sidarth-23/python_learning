from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
temp_data = {}
to_learn = {}

# ------------------------ PICK RANDOM WORD ----------------------#
try:
    data = pandas.read_csv("data/words-to-learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
print(to_learn)


# ------------------------ TICK AND CROSSMARK --------------------#
def remember():
    to_learn.remove(temp_data)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words-to-learn.csv", index=False)
    next_card()


# ------------------------- GLOBAL CHANGE CARD -------------------#
def next_card():
    global temp_data, flip_timer
    window.after_cancel(flip_timer)
    temp_data = random.choice(to_learn)
    canvas.itemconfig(canvas_img, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=temp_data["French"], fill="black")
    flip_timer = window.after(3000, english_word)


def english_word():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=temp_data["English"], fill="white")


# ------------------------ UI SETUP ------------------------------ #

window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=english_word)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remember)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

next_card()

window.mainloop()
