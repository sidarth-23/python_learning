from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)

user_value = Entry()
user_value.grid(row=0, column=1)

converted_value = Label()
converted_value.config(text='0', pady=10, padx=10)
converted_value.grid(row=1, column=1)

miles_text = Label()
miles_text.config(text="Miles", padx=10, pady=10)
miles_text.grid(row=0, column=2)

is_equal_text = Label()
is_equal_text.config(text="is equal to", padx=10, pady=10)
is_equal_text.grid(column=0, row=1)


def to_km_value():
    to_km = int(user_value.get()) * 1.60934
    converted_value.config(text=f"{to_km}")


calculate_button = Button()
calculate_button.config(text="Calculate", command=to_km_value)
calculate_button.grid(row=2, column=1)

window.mainloop()
