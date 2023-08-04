import requests
import os
import datetime as dt

# API INFO
API_KEY = os.environ.get('NUTRI_API_KEY')
USER_ID = os.environ.get('NUTRI_APP_ID')
EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

# PERSONAL INFO
WEIGHT_KG = 66
HEIGHT_CM = 180
AGE = 23
GENDER = 'male'

activity = input("Tell me the exercises you did ")

parameters = {
    'query': activity,
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE,
}

header = {
    'x-app-id': USER_ID,
    'x-app-key': API_KEY,
}

nutri_response = requests.post(url=EXERCISE_ENDPOINT, json=parameters, headers=header)
data = nutri_response.json()['exercises']

# SHEETY API INFO
SH_USER_ID = os.environ.get('SHEETY_USER_ID')
SH_PROJECT_NAME = 'myWorkout'
SH_SHEET_NAME = 'sheet1'
SH_ENDPOINT = f"https://api.sheety.co/{SH_USER_ID}/{SH_PROJECT_NAME}/{SH_SHEET_NAME}"
for items in data:
    sh_parameters = {
        'sheet1': {'date': dt.datetime.now().strftime('%d/%m/%y'),
                   'time': dt.datetime.now().strftime('%H:%M:%S'),
                   'exercise': items['name'],
                   'duration': items['duration_min'],
                   'calories': items['nf_calories'],
                   }
    }

    sh_header = {
        'Authorization': os.environ.get('SHEETY_BEARER_TOKEN'),
    }

    sh_response = requests.post(url=SH_ENDPOINT, json=sh_parameters, headers=sh_header)
    print(sh_response.text)
