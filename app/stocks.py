# this is the app/stocks.py file

print("STOCKS REPORT...")

from app.alphavantage_service import fetch_stocks_data

symbol = input("Please input a stock ticker (default: 'NFLX'): ") or "NFLX"

fetch_stocks_data(symbol)