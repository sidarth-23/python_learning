import requests
import os
import datetime as dt
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.kiwi_endpoint = 'https://tequila-api.kiwi.com'
        self.api_key = os.environ.get('KIWI_API_KEY')
        self.from_time = dt.datetime.now() + dt.timedelta(days=1)
        self.to_time = dt.datetime.now() + dt.timedelta(days=(6 * 30))

    def get_destination_code(self, name):
        location_endpoint = f'{self.kiwi_endpoint}/locations/query'
        headers = {'apiKey': self.api_key}
        query = {'term': name, 'location_types': 'city'}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]['code']
        return code

    def get_prices(self, city):
        search_endpoint = f'{self.kiwi_endpoint}/search'
        header = {
            'apiKey': self.api_key,
        }
        get_params = {
            "fly_from": 'LON',
            "fly_to": city,
            "date_from": self.from_time.strftime("%d/%m/%Y"),
            "date_to": self.to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=search_endpoint, params=get_params, headers=header)

        try:
            get_data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {city}.")
            return None
        print(get_data)
        flight_data = (FlightData(
            price=get_data["price"],
            origin_city=get_data["route"][0]["cityFrom"],
            origin_airport=get_data["route"][0]["flyFrom"],
            destination_city=get_data["route"][0]["cityTo"],
            destination_airport=get_data["route"][0]["flyTo"],
            out_date=dt.datetime.utcfromtimestamp(get_data["route"][0]["dTimeUTC"]),
            return_date=dt.datetime.utcfromtimestamp(get_data["route"][1]["dTimeUTC"]),
        ))

        return flight_data
