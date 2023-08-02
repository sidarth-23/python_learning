##################### Extra Hard Starting Project ######################
import random

import pandas
import datetime as dt
import smtplib

# 1. Update the birthdays.csv
try:
    data = pandas.read_csv("birthdays.csv")
except FileNotFoundError:
    print("Sorry the birthday list was not found")
    exit(-1)
else:
    birthday_list = data.to_dict(orient="records")


def count_to_add():
    while True:
        try:
            temp = int(input("How many birthdays to add: "))
            return temp
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


for i in range(count_to_add()):
    name = input("Enter the name of the person")
    email = input("Enter the email of the person")
    date = list(input("Enter the DOB of the person in DD/MM/YYYY format").split('/'))
    dob_person_to_add = {'name': name, 'email': email, 'year': date[2], 'month': date[1], 'day': date[0]}
    birthday_list.append(dob_person_to_add)

# Convert the updated list to dataframe and save to csv
df = pandas.DataFrame(birthday_list)
df.to_csv("birthdays.csv", mode='w', index=False)

# Read the updated csv and display records
updated_data = pandas.read_csv("birthdays.csv")
updated_birthday_list = updated_data.to_dict(orient="records")

print(updated_birthday_list)


# 4. Send the letter generated in step 3 to that person's email address.
def send_email(to_email, msg, name_temp):
    with open("userinfo.txt", mode="r") as file:
        credentials = file.readlines()
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=credentials[0], password=credentials[1])
        connection.sendmail(from_addr=credentials[0], to_addrs=to_email, msg=f"Subject: Happy birthday {name_temp}\n\n{msg}")
        connection.close()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
def read_template():
    choice = random.randint(1, 3)
    with open(f"letter_templates/letter_{choice}.txt", mode="r") as file:
        letter = file.read()
    return letter


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
for key in updated_birthday_list:
    if key['day'] == now.day and key['month'] == now.month:
        letter_temp = read_template()
        letter_temp.replace("[NAME]", key['name'])
        send_email(key['email'], letter_temp, key['name'])
