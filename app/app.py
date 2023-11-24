import streamlit as st
import pandas as pd
import requests

'''
# TaxiFareModel front
'''
st.title('Taxi Fare Prediction')

st.sidebar.header('Input Parameters')

pickup_datetime = st.date_input('Pickup Date', value=None)
pickup_longitude = st.sidebar.number_input('Pickup Longitude', value=0.0)
pickup_latitude = st.sidebar.number_input('Pickup Latitude', value=0.0)
dropoff_longitude = st.sidebar.number_input('Dropoff Longitude', value=0.0)
dropoff_latitude = st.sidebar.number_input('Dropoff Latitude', value=0.0)
passenger_count = st.sidebar.number_input('Passenger Count', value=1)

# Prepare input data for prediction
input_data = {
    'pickup_datetime': str(pickup_datetime),
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
response = requests.post(url, json=input_data)
# Check if the request was successful
if response.status_code == 200:
    # Extract the prediction from the response
    prediction = response.json().get('prediction')
    # Display the predicted fare
    st.markdown('## Prediction')
    st.write(f'Predicted Fare: ${prediction:.2f}')
else:
    st.error(f"Error making prediction. Status code: {response.status_code}")
    st.text(response.text)  # Display the error response for debugging
# Display the prediction
st.markdown('## Prediction')
st.write(response.json())
st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''