import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 43.761539
MY_LNG = -79.411079
MY_EMAIL = "t3st.drag0n@gmail.com"
PASSWORD = "Killershark@098"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    longitude = float(data['iss_position']['longitude'])
    latitude = float(data['iss_position']['latitude'])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        'lat': MY_LAT,
        'lng': MY_LNG,
        'formatted': 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up ☝️.\n\n The ISS is above you in the sky.")
