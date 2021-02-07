import requests
import os
from datetime import date

USERNAME = "bobbypalko"
TOKEN = os.environ.get("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# https://pixe.la/@bobbypalko

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": "exercise",
  "name": "Exercise Graph",
  "unit": "minutes",
  "type": "int",
  "color": "ajisai",
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{graph_config.get('id')}"

pixel_config = {
  "date": date.today().strftime("%Y%m%d"),
  "quantity": input("How many minutes did you exercise today?")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# update_endpoint = f"{pixel_endpoint}/{date.today().strftime('%Y%m%d')}"

# update_config = {
#   "quantity": "37"
# }

# # response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# # print(response.text)

# delete_endpoint = f"{pixel_endpoint}/{date.today().strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)