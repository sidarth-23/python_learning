import requests
from twilio.rest import Client
import os

# Twilio SMS API Section
# Please do not abuse this api keys
account_sid = os.environ.get('TWILIO_ACC_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

# Weather API Section
base_api_page = "https://api.openweathermap.org/data/2.8/onecall"

api_category = ""

api_key = os.environ.get('OWM_API_KEY')
lat = 23.181467
long = 79.986404

parameters = {
    'lat': lat,
    'lon': long,
    'exclude': "current,minutely,daily",
    'appid': api_key,
}

response = requests.get(f"{base_api_page}{api_category}", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
weather_data = data['hourly'][:12]
for i in weather_data:
    condition = i['weather'][0]['id']
    print(condition)
    if condition < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(body="It's going to rain today in Jabalpur 😍",
                from_='+16672880397',
                to='+918098230245')


