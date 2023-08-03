# Please enter your own user email and app password for the program to run
# email in USER_EMAIL and password in USER_TOKEN
import math
import smtplib
import requests
from datetime import datetime
import time
import os

MY_LAT = 11.016844
MY_LONG = 76.955833


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])

    distance = math.sqrt(math.pow((MY_LAT - iss_lat), 2) + math.pow((MY_LONG - iss_long), 2))

    if -5 < distance < 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lmg": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now.hour > sunset or time_now.hour < sunrise:
        return True


user = os.environ.get('USER_EMAIL')
password = os.environ.get('USER_TOKEN')

while True:
    time.sleep(60)
    if is_night() and is_iss_overhead():
        with open("userinfo.txt", mode="r") as file:
            credentials = file.readlines()
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=user, password=password)
            connection.sendmail(from_addr=user, to_addrs="sidarth158@gmail.com",
                                msg="Subject:ISS Above you\n\nGo out and enjoy the view")
            connection.close()
