import requests
from datetime import datetime
import smtplib

MY_LAT = 39.952583
MY_LONG = -75.165222

MY_EMAIL = ""
MY_PASSWORD = ""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_is_close():
    lat_diff = abs(MY_LAT - iss_latitude)
    long_diff = abs(MY_LONG - iss_longitude)

    if lat_diff < 5 and long_diff < 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.utcnow()


if iss_is_close() and (time_now.hour < sunrise or time_now.hour > sunset):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:ISS Overhead!\n\nLook up!!!"
        )
        
