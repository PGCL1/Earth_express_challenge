from dotenv import load_dotenv
import os
import requests

# Climatiq Calculate Emissions Part
load_dotenv()

API_URL = os.environ.get('CLIMATIQ_URL')
API_KEY = os.environ.get('CLIMATIQ_API_KEY')

print(f"Climatiq API URL is: {API_URL}")
headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-type": "application/json"
        }


def get_travel_emissions(origin, destination, travel_mode, flight_class=None):

    data = {
        "origin": {"query": origin},
        "destination": {"query": destination},
        "travel_mode": travel_mode
    }

    if travel_mode == 'air':
        data['air_details'] = flight_class

    response = requests.post(API_URL, json=data, headers=headers)
    return response
