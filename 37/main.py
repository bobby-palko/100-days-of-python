import requests
import os
from datetime import datetime as dt

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")

headers = {
  "x-app-id": APP_ID,
  "x-app-key": API_KEY,
}

exercises = input("Tell me what exercises you did today: ")

now = dt.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_data = {
  "query": exercises
}

response = requests.post(url=exercise_endpoint, json=exercise_data, headers=headers)
data = response.json().get('exercises')

headers = {
  "Authorization": f"Bearer {API_KEY}"
}

for exercise in data:
  name = exercise.get("name")
  duration = exercise.get("duration_min")
  calories = exercise.get("nf_calories")

  payload = {
    "workout": {
      "date": date,
      "time": time,
      "exercise": name.title(),
      "duration": duration,
      "calories": calories,
    }
  }
  response = requests.post(url=SHEETY_ENDPOINT, json=payload, headers=headers)
  print(response.text)

