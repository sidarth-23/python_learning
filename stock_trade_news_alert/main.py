import math
import os
import requests
import datetime as dt
from twilio.rest import Client

# General details for the whole code
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get('STOCK_API_KEY')
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
TWILIO_ACC_SID = os.environ.get('TWILIO_ACC_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')

today = dt.datetime.now().strftime('%Y-%m-%d')
yesterday = (dt.datetime.now() - dt.timedelta(days=1)).strftime('%Y-%m-%d')
day_bf_yesterday = (dt.datetime.now() - dt.timedelta(days=2)).strftime('%Y-%m-%d')

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_parameters = {
    'q': COMPANY_NAME,
    'sortBy': 'relevancy',
    'apiKey': NEWS_API_KEY,
}


def get_news():
    news_response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    news_data = news_response.json()['articles']
    top_news = news_data[:3]
    return top_news


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
account_sid = os.environ.get(TWILIO_ACC_SID)
auth_token = os.environ.get(TWILIO_AUTH_TOKEN)


def send_news(content: list, difference: float):
    for new in content:
        title = new['title']
        desc = new['description']
        header = ""
        if difference > 0:
            header = f"TSLA 🔺{math.floor(difference)}%"
        else:
            header = f"TSLA 🔻{math.floor(difference)}%"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            from_='+16672880397',
            body=f'{header}\nTitle:{title}\n Brief:{desc}',
            to='+918098230245'
        )


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY,
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
stock_response.raise_for_status()
stock_data = stock_response.json()['Time Series (Daily)']

data_list = [value for (key, value) in stock_data.items()]
# yesterday_price = float(stock_data[yesterday]['4. close'])
# day_bf_yesterday_price = float(stock_data[day_bf_yesterday]['4. close'])
# print(yesterday_price, day_bf_yesterday_price)
yesterday_price = float(data_list[0]['4. close'])
day_bf_yesterday_price = float(data_list[1]['4. close'])
price_difference = ((yesterday_price - day_bf_yesterday_price) / yesterday_price) * 100
print(price_difference)
if price_difference > 5:
    news = get_news()
    send_news(news, price_difference)
