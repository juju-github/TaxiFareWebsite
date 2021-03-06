import streamlit as st
import requests
from datetime import datetime
import pytz



'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride
'''
pickup_datetime = st.text_input('date and time of pick up', '2012-10-06 12:10:20')
pickup_longitude = st.text_input('pick up longitud', '-73.9798156')
pickup_latitude = st.text_input('pick up latitud', '40.7614327 ')
dropoff_longitude = st.text_input('drop off longitud', '73.8803331')
dropoff_latitude = st.text_input('dropoff latitud', '40.6513111')
passenger_count = st.text_input('how many passengers?', '2')
'''

'''
'''
## Once we have these, let's call our API in order to retrieve a prediction
'''

'''
See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

    """    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
    # localize the user datetime with NYC timezone
    eastern = pytz.timezone("US/Eastern")
    localized_pickup_datetime = eastern.localize(pickup_datetime, is_dst=None)
    # localize the datetime to UTC
    utc_pickup_datetime = localized_pickup_datetime.astimezone(pytz.utc)
    formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")"""

    params = {
        'key': '2013-07-06 17:18:00.000000119',
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count
    }

    if st.button('Get price prediction'):
        # print is visible in the server output, not in the page
        print('button clicked!')
        response = requests.get(url=url, params=params).json()
        st.markdown(response['fare'])

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
