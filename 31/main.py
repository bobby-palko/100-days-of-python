import pandas as pd
import smtplib
import datetime as dt
import random

MY_EMAIL = "" # this is the email the content will be sent from
MY_PASSWORD = ""
NUM_TEMPLATES = 3

# load initial data
birthdays = pd.read_csv("birthdays.csv").to_dict(orient="records")
todays_birthdays = []
now = dt.datetime.now()


def get_templates():
    templates = []
    for i in range(NUM_TEMPLATES):
        with open(f"letter_templates/letter_{i+1}.txt") as file:
            letter = file.read()
            templates.append(letter)
    return templates

def send_email(to_addr, email_body):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=to_addr,
            msg=f"Subject:Happy Birthday!\n\n{email_body}"
        )

def send_birthday_wishes():
    templates = get_templates()
    # for every birthday today, grab a random template and replace [NAME] with the person's name, then send them an email
    for person in todays_birthdays:
        letter = random.choice(templates)
        letter = letter.replace("[NAME]", person["name"])
        send_email(person["email"], letter)

todays_birthdays = [birthday for birthday in birthdays if birthday["month"] == now.month and birthday["day"] == now.day]

if todays_birthdays:
    send_birthday_wishes()