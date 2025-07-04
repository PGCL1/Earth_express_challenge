import streamlit as st
import requests
import numpy as np
import pandas as pd
import os

header = st.write('Travel Emission Cockpit')

origin = st.text_input('Enter Departure')
destination = st.text_input('Enter Destination')
travel_mode = st.selectbox(
        'How are you planning to travel?',
        ('air', 'car', 'rail')
)
flight_class = ""
st.write(f"Customer will be travelling in {travel_mode}")

if travel_mode == 'air':
    flight_class = st.selectbox(
            'How will you be flying?',
            ('economy', 'business', 'first')
    )
    st.write(f"Customer will be flying in {flight_class}")

st.write(f"Departure Location: {origin}")
st.write(f"Destination Location: {destination}")


# Climatiq Calculate Emissions Part
API_URL = os.environ('CLIMATIQ_URL')
API_KEY = os.environ('CLIMATIQ_API_KEY')

headers = {
        "Authorization": f"Bearer {API_KEY.strip()}",
        "Content-type": "application/json"
        }


def get_travel_emissions():

    data = {
        "origin": {"query": origin},
        "destination": {"query": destination},
        "travel_mode": travel_mode
    }

    if travel_mode == 'air':
        data['air_details'] = flight_class

    response = requests.post(API_URL, json=data, headers=headers)
    return response

# if response['co2e'] >
