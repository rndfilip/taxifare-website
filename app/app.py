import streamlit as st
# import pandas as pd
import requests
import datetime

'''
# TaxiFareModel front
'''
st.title('Taxi Fare Prediction')

st.sidebar.header('Input Parameters')

pickup_datetime = st.date_input('Pickup Date',datetime.date(2023, 12, 12))
time_input = st.time_input('bullshit need', datetime.time(8, 45))
pickup_longitude = st.sidebar.number_input('Pickup Longitude', value=75.88)
pickup_latitude = st.sidebar.number_input('Pickup Latitude', value=75.12)
dropoff_longitude = st.sidebar.number_input('Dropoff Longitude', value=77.12)
dropoff_latitude = st.sidebar.number_input('Dropoff Latitude', value=77.83)
passenger_count = st.sidebar.number_input('Passenger Count', value=2)

# Prepare input data for prediction
input_data = {
    'pickup_datetime': datetime.datetime.combine(pickup_datetime,time_input).strftime("%Y-%m-%d %H:%M:%S"),
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

# Display the input data
st.write(input_data)

url = 'https://taxifare.lewagon.ai/predict'

# Make a POST request to the model API
response = requests.get(url, params= input_data)
st.write(response.url)


st.markdown('## Prediction')
st.write("Fare ride price",response.json()["fare"])
st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''