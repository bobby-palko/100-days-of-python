import requests
from twilio.rest import Client
import os

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API")
LAT = 47.035530
LONG = -122.900833

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH")
TWILIO_NUMBER = os.environ.get("TWILIO_NUM")
MY_PHONE = ""

parameters = {
    "lat": LAT,
    "lon": LONG,
    "exclude": "current,minutely,daily,alerts",
    "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()

hourly_data = [weather for weather in data.get("hourly")[:12]]

is_raining = False

for weather_data in hourly_data:
    condition_code = weather_data.get("weather")[0].get("id")
    if int(condition_code) < 700:
        is_raining = True

if is_raining:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages \
        .create(
            body="Shit's wet outside. Bring an umbrella.",
            from_=TWILIO_NUMBER,
            to=MY_PHONE
    )
    print(message.status)


