import os
from dotenv import load_dotenv
import requests
import json
from app.utils import to_usd
from pandas import read_csv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")


def fetch_crypto_data(symbol):
    url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&market=USD&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    tsd = parsed_response["Time Series (Digital Currency Daily)"]
    dates = list(tsd.keys())
    latest_date = dates[0]
    latest = tsd[latest_date]
    print(symbol)
    print(latest_date)
    print(to_usd(float(latest['4a. close (USD)'])))



def fetch_stocks_data(symbol):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"
    df = read_csv(url)
    latest = df.iloc[0]
    print(symbol)
    print(latest["timestamp"])
    print(to_usd(latest["close"]))
  


def fetch_unemployment_data():
   url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
   response = requests.get(url)
   parsed_response = json.loads(response.text)
   data = parsed_response["data"]
   latest = data[0]
   print(latest) #> {'date': '2022-02-01', 'value': '3.8'}