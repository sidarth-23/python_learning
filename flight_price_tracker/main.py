# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()

# Getting user info
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
email = input("Enter your email: ")
user_database = dataManager.get_user_sheet()['users']
print(user_database)
for item in user_database:
    if (item['firstName'] == first_name or item['lastName'] == last_name) and item['email'] == email:
        print("You're already a member!")
    else:
        dataManager.update_user_sheet(first_name, last_name, email)

# Getting flight data and sending SMS
sheet_data = dataManager.get_flight_sheet()['prices']
for item in sheet_data:
    if item['iataCode'] == '':
        iata_code = flightSearch.get_destination_code(item['city'])
        dataManager.update_flight_sheet(item, iata_code)

i = 0
for item in sheet_data:
    flight = flightSearch.get_prices(item['iataCode'])
    print(flight)
    if item['lowestPrice'] > flight.price:
        message = f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        notificationManager.send_message(message)

# Sending email to all users
user_database = dataManager.get_user_sheet()['users']
for item in sheet_data:
    flight = flightSearch.get_prices(item['iataCode'])
    print(flight)
    if item['lowestPrice'] > flight.price:
        message = f"Subject: Test message from Sid\n\nLow price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        for user in user_database:
            email = user['email']
            notificationManager.send_email(email, message)
