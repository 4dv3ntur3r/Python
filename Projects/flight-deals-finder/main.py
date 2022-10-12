# This file will need to use the DataManager,
# FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from twilio.rest import Client

# https://sheety.co/
# https://partners.kiwi.com/
# https://tequila.kiwi.com/portal/login
# https://www.twilio.com/docs/sms

SHEET_ENDPOINT = "https://api.sheety.co/2d17e3d29490fa3ab224e5888fc877ce/flightDeals/prices"
AIRPLACE_PRICES_ENDPOINT = "https://tequila-api.kiwi.com"

sheet_token = {
    "Authorization": "Bearer ihfd67BU&*@JION*f39n89(*H@B)(nb78(*HG(",
}

response_sheet = requests.get(url=SHEET_ENDPOINT, headers=sheet_token)
print(response_sheet.text)
