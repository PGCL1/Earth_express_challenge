from dotenv import load_dotenv
import os
import requests

# climatiq Calculate Emissions Part
load_dotenv()

API_URL = os.environ.get('CLIMATIQ_URL')
API_KEY = os.environ.get('CLIMATIQ_API_KEY')

print(f"Climatiq API URL is: {API_URL}")
headers = {
        "Authorization": f"Bearer {API_KEY.strip()}",
        "Content-type": "application/json"
        }


def get_travel_emissions(origin, destination, travel_mode, flight_class=None):

    data = {
        "origin": {"query": origin},
        "destination": {"query": destination},
        "travel_mode": travel_mode
    }

    if travel_mode == 'air':
        data['class'] = flight_class

    try:
        response = requests.post(API_URL, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"An unexcepted error occured: {e}")
        return {"error": "Unexpected Error", "details": str(e)}


