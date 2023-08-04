import os
import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sh_user = os.environ.get('SHEETY_USERNAME')
        self.project_name = 'flightDeals'
        self.sh_endpoint = ""

    def get_flight_sheet(self):
        data = self.get_sheet('prices')
        return data


    def update_flight_sheet(self, item, city):
        sheet = 'prices'
        self.sh_endpoint = f"https://api.sheety.co/{self.sh_user}/{self.project_name}/{sheet}"
        print(item)
        sh_params = {
            'price': {
                'iataCode': city,
            }
        }
        objects = item['id']
        endpoint = f'{self.sh_endpoint}/{objects}'
        update_response = requests.put(url=endpoint, json=sh_params)
        update_response.raise_for_status()
        print(update_response.text)

    def get_sheet(self, sheet):
        self.sh_endpoint = f"https://api.sheety.co/{self.sh_user}/{self.project_name}/{sheet}"
        get_response = requests.get(url=self.sh_endpoint)
        get_response.raise_for_status()
        data = get_response.json()
        return data
