from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="File not found", message="Please enter the first usename password to start the "
                                                            "search")
    else:
        web = website_entry.get().title()
        if web in data:
            messagebox.showinfo(title=f"{web}",
                                message=f"Email/Username: {data[web]['email']} \nPassword: {data[web]['password']}")
        elif len(web) == 0:
            messagebox.showinfo(title="Does not Exist", message="Please enter a website to search")
        else:
            messagebox.showinfo(title="Does not Exist", message="Data for this website is not there")

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if website and password and email:
        messagebox.showinfo(title="Added password", message=f"Your password for {website} has been added "

                                                            f"successfully")

        try:
            with open("data.json", mode="r") as file:
                # Read the data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Update the data
            data.update(new_data)

            with open("data.json", mode="w") as file:
                # Save the updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

    else:
        messagebox.showerror(title="Info missing", message="Please enter all the fields")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas()
canvas.config(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label()
website_label.config(text="Website: ")
website_label.grid(row=1, column=0)

email_label = Label()
email_label.config(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password: ")
password_label.grid(row=3, column=0)

# Entires
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=42)
email_entry.insert(END, "sidarth157gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
search_button = Button(width=15)
search_button.config(text="Search", command=search_password)
search_button.grid(row=1, column=2)

generate_button = Button()
generate_button.config(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button()
add_button.config(text="Add", width=36, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
