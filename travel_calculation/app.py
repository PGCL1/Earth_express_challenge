import streamlit as st
import requests
import numpy as np
import pandas as pd
from travel_emissions import get_travel_emissions
from test import random_number


def hello():
    print("wazaaaa")


header = st.write('Travel Emission Cockpit')

col1, col2 = st.columns(2)

with col1:
    origin = st.text_input('Enter Departure')
with col2:
    destination = st.text_input('Enter Destination')

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
    st.write(f"Customer will be flying in {flight_class}")

st.write(f"Customer will be travelling from {origin} to {destination} by {travel_mode}")

# calculate_trip_emissions = st.button("Calculate Emissions",
#                                     on_click=get_travel_emissions,
#                                     args=(origin, destination, travel_mode, flight_class))
#    if travel_data['co2e'] > 100:
#        alternative_button = st.button('Suggest Alternatives')

calculate_trip_emissions = st.button("Calculate Emissions")

if calculate_trip_emissions:
    st.write("Customer wants to know what are the total emissions for their trip")
    res = random_number() # get_travel_emissions(origin, destination, travel_mode, flight_class)
    st.write(f"res is {res}")

    if res >= 500:
        suggestions_alternative = st.button('Suggest Alternatives')
        st.image('../images/sad_face.jpg')
    else:
        st.image('../images/happy_face.jpg')
