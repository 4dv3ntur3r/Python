import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "http://newsapi.org/v2/everything"

STOCK_API_KEY = 'XPGP872OVPIGKNB9'

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yerstaday_price = data_list[0]["4. close"]

day_before_yesterday_price = data_list[1]["4. close"]


difference = abs(float(yerstaday_price) - float(day_before_yesterday_price))
print(difference)

diff_percent = (difference / float(yerstaday_price))* 100
print(diff_percent)

if diff_percent > 0.02:
    print("get_news")