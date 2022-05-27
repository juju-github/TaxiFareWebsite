import streamlit as st
import datetime
import requests


'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
d = st.date_input(
    "date",
    datetime.date('1979, 06, 10'))
st.write('date:', d)

t = st.time_input('time', datetime.time(8, 45))
st.write('time', t)

pickup_longitude = st.text_input('pickup_longitude')
st.write('pickup_longitude')

pickup_latitude = st.text_input('pickup_latitude')
st.write('pickup_latitude')

dropoff_longitude = st.text_input('dropoff_longitude')
st.write('pickup_latitude')
dropoff_latitude = st.text_input('dropoff_latitude')
st.write('pickup_latitude')
passenger_count = st.number_input('passenger_count')
st.write('The current passenger_count is ', passenger_count)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'


#2. Let's build a dictionary containing the parameters for our API...
dict = {"date":[d],
        "time": [t],
        "pickup_longitude": [float(pickup_longitude)],
        "pickup_latitude": [float(pickup_latitude)],
        "dropoff_longitude": [float(dropoff_longitude)],
        "dropoff_latitude": [float(dropoff_latitude)],
        "passenger_count": [int(passenger_count)],
            }

#3. Let's call our API using the `requests` package...
result = requests.get(url, params = dict)

#4. Let's retrieve the prediction from the **JSON** returned by the API...
print({"fare":result})
## Finally, we can display the prediction to the user
