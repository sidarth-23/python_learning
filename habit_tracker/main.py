import requests
import datetime as dt
import os

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = os.environ.get('USER_NAME')
TOKEN = os.environ.get('USER_TOKEN')
GRAPH_ID = 'graph1'
DATE = dt.datetime.now().strftime("%Y%m%d")

user_params = {
    "token": TOKEN,
    'username': 'sidarth',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    'id': 'graph1',
    'name': 'Cycling',
    'unit': 'km',
    'type': 'float',
    'color': 'ichou'
}

header = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

pixel_params = {
    'date': DATE,
    'quantity': '2',
}

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=header)

pixel_remove_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

response = requests.put(url=pixel_remove_endpoint, json={'quantity': '10'}, headers=header)
print(response.text)