import requests
from datetime import datetime


EXERCISE_ENDPOIT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SPREAD_SHEET_ENDPOINT = "https://api.sheety.co/2d17e3d29490fa3ab224e5888fc877ce/workoutTracking/workouts"

user_input = input("What did you do today?")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


exercise_params = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 145,
    "age": 27,
}

response = requests.post(url=EXERCISE_ENDPOIT, json=exercise_params, headers=headers)
result = response.json()

now_date_time = datetime.now()

today_date = now_date_time.strftime("%Y-%m-%d")
now_time = now_date_time.strftime("%H:%M:%S")

for exercise in result["exercises"]:
    spread_sheet_params = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response_sheet = requests.post(url=SPREAD_SHEET_ENDPOINT, json=spread_sheet_params, headers=headers_sheet)
    print(response_sheet.text)

#
# HINT 1: You'll need to import the os module.
#
# Here's how you would set environment variables
#
# APP_ID = os.environ["APP_ID"]
# API_KEY = os.environ["API_KEY"]
# and here is how you would get an environment variable
#
# APP_ID = os.environ.get("APP_ID")
# API_KEY = os.environ.get("API_KEY")