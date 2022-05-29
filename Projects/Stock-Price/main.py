import datetime
import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXX"
NEWS_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILLO_PHONE_NO = "+1XXXXXXXXXX"
MY_PHONE_NO = "+1XXXXXXXXXX"

parameters_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

response_stock = requests.get(url=STOCK_ENDPOINT, params=parameters_stock)
response_stock.raise_for_status()

current_date = datetime.date.today()

data_stock = response_stock.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data_stock.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

# TODO 2. - Get the day before yesterday's closing stock price

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(day_before_yesterday_closing_price)

# TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
print(difference)

# TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(diff_percent)

# TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").


## STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
if abs(diff_percent) > 5:
    news_params = {
        "apikey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response_news.raise_for_status()

    articles = response_news.json()["articles"]

    # TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    three_articles = articles[:3]
    print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.

    # TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}Headline: {article['title']}. \nBrief: {article['description']}" for article in
                          three_articles]

# TODO 9. - Send each article as a separate message via Twilio.


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(ACCOUNT_SID, AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=TWILLO_PHONE_NO,
        to=MY_PHONE_NO
    )

print(message.sid)
# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
