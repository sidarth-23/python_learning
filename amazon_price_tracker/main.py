import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

# The code is currently not working as amazon has disabled web scraping and introduced API

# Adding new items on choice
try:
    with open('items.txt', mode='r') as file:
        data = file.read().split()
except FileNotFoundError:
    with open('items.txt', mode='w') as file:
        item = input("Enter an item in the list")
        file.write(item)
    with open('items.txt', mode='r') as file:
        data = file.read().split()

check = int(input('Enter 1 to enter a new item or anything else to ignore'))

while check == 1:
    with open('items.txt', mode='a') as file:
        item = input("Enter an item in the list")
        if item not in data:
            file.write(item)

    check = int(input('Enter 1 to enter a new item or anything else to ignore'))

# Reading the links
with open('items.txt', mode='r') as file:
    data = file.read().split()


def send_email(msg):
    user = os.environ.get('USER_ID')
    password = os.environ.get('USER_TOKEN')
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=user, password=password)
        connection.send_message(from_addr=user,
                                to_addrs='sidarth158@gmail.com',
                                msg=msg)
        connection.close()


for item in data:
    print(item)
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(url=item, headers=header)
    response.raise_for_status()
    page = response.text

    soup = BeautifulSoup(page, 'lxml')
    print(soup)
    price = soup.find(class_='a-offscreen')
    print(price)

    title = soup.find(name='span', id='productTitle').get_text()

    # message = f'Subject:Price Alert\n\n{title} is now at a price of ${price}'
    # send_email(message)