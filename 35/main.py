import requests
from twilio.rest import Client
import os


STOCK = "GME"
COMPANY_NAME = "GameStop"
STOCK_API = os.environ.get("STOCK_API")
NEWS_API = os.environ.get("NEWS_API")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

## STEP 1: Use https://www.alphavantage.co
parameters = {
  "function": "TIME_SERIES_DAILY_ADJUSTED",
  "symbol": STOCK,
  "apikey": STOCK_API,
}

response = requests.get("https://www.alphavantage.co/query", params=parameters)
response.raise_for_status()
data = response.json().get("Time Series (Daily)")

data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data.get("4. close")
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data.get("4. close")

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
difference = (float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
up_or_down = None
if difference > 0:
  up_or_down = "🚀 🚀 🚀"
else:
  up_or_down = "🔻"
diff_percent = round((difference / float(yesterday_closing_price)) * 100)

if (abs(diff_percent) > 5):
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
  parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
  }
  response = requests.get("http://newsapi.org/v2/everything", params=parameters)
  response.raise_for_status()
  data = response.json().get("articles")
  three_articles = data[:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
  formatted_articles = [f"{COMPANY_NAME}: {up_or_down}{diff_percent}%\nHeadline: {article.get('title')}.\nBrief: {article.get('description')}" for article in three_articles]

  client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

  for article in formatted_articles:
    message = client.messages.create(
      body = article,
      from_ = "+14158811085",
      to = "+16109147702"
    )
