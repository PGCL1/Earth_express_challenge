import streamlit as st
import requests
import numpy as np
import pandas as pd
import time
import googlemaps
import os

from streamlit_searchbox import st_searchbox
from travel_calculation.calculate_emissions import get_travel_emissions
from travel_calculation.test import random_number
from travel_calculation.layout import circular_image


# header function of Travel Cockpit
header = st.header('Travel Emission Cockpit')

# initializing googlemaps API
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
gmaps = googlemaps.Client(key=GOOGLE_API_KEY)


def get_address_suggestions(query, api_key):
    if not query:
        return []
    url = "https://maps.googleapis.com/maps/api/place/autocomplete/json"
    params = {
        "input": query,
        "key": api_key,
        "types": "geocode",
        "language": "en"
    }
    response = requests.get(url, params=params)
    predictions = response.json().get("predictions", [])
    return [p["description"] for p in predictions]


def get_place_suggestions(searchterm):
    suggestions = get_address_suggestions(searchterm, GOOGLE_API_KEY)
    return suggestions






# starting form
col1, col2 = st.columns(2)
with col1:
    st.write("Enter Depature")
    origin = st_searchbox(get_place_suggestions, key="origin", placeholder="enter departure")
with col2:
    st.write("Enter Destination")
    destination = st_searchbox(get_place_suggestions, key="destination", placeholder="enter destination")

travel_mode = st.selectbox(
        'How are you planning to travel?',
        ('air', 'car', 'rail')
)
flight_class = ""

if travel_mode == 'air':
    flight_class = st.selectbox(
            'How will you be flying?',
            ('economy', 'business', 'first')
    )

# calculate travel emissions
calculate_trip_emissions = st.button("Calculate Emissions")
if calculate_trip_emissions and destination and origin:
    res = get_travel_emissions(origin, destination, travel_mode, flight_class)

    with st.empty():
        with st.spinner("Calculating emissions...", show_time=True):
            time.sleep(2)

    st.write("\n")
    if res['co2e'] > 300:
        col1, col2, col3 = st.columns(3, gap="small", vertical_alignment="center")
        with col1:
            st.write("Are you sure this is the only way? my poor rainforest\
                    (give some text prez team)")
        with col2:
            circular_image('images/sad_sid.png')
        with col3:
            suggestions_alternative = st.button('Suggest Alternatives')
            if suggestions_alternative:
                other_travel_mode = [mode for mode in travel_mode if mode != travel_mode]
                for mode in other_travel_mode:
                    other_emissions = get_travel_emissions(origin, destination, mode)
                    st.write(f"You could also travel by {mode}, it would cost\
                            {other_emissions['co2e']} and save %")
    else:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.write(f"Thank you for thinking of me {st.user.given_name},\
                    I hope you have a great trip to {destination} (give me some text prez team)")
        with col2:
            circular_image('images/happy_sid.png')

    st.write(f"res is {res}")
else:
    st.write("Please input all fields in the form")
