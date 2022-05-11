import requests
import os
from twilio.rest import Client

api_key = "{YOUR_API_KEY_FOR_OPEN_WEATHER_MAP}"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = '{YOUR_SID_IN_TWILIO}'
auth_token = '{YOUR_AUTH_TOKEN_TWILIO}'

parameters = {
    'lat': 35.207008,
    'lon': -101.832008,
    'exclude': 'current,minutely,daily',
    'appid': api_key,
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

####################### My Code ##################################
# for x in range(0, 12):
#     hourly_data = weather_data['hourly'][x]['weather'][0]['id']
#     if hourly_data < 700:
#         print("Bring an Umbrella")
#         break

will_rain = False

weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an Umbrella ☔",
        from_='+15484890643',
        to='+14168549407'
    )

    print(message.sid)
