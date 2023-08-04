# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


dataManager = DataManager()
flightSearch = FlightSearch()
notificationManager = NotificationManager()


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
