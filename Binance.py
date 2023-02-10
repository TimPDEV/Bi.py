import requests
import json
from datetime import datetime, timedelta

def get_price():
   url = 'https://api.binance.com/api/v1/klines?symbol=XRPUSDT&interval=1h'
   response = requests.get(url)
   data = json.loads(response.text)
   return float(data[-1][4])


def get_max_price():
   url = 'https://api.binance.com/api/v1/klines?symbol=XRPUSDT&interval=1h'
   response = requests.get(url)
   data = json.loads(response.text)
   max_price = 0
   for item in data:
       if float(item[4]) > max_price:
           max_price = float(item[4])
   return max_price

def check_price_drop(max_price, current_price):
   if (max_price - current_price) > (max_price * 0.01):
       print('Price dropped by 1%!')

if __name__ == '__main__':
   max_price = get_max_price()
   while True:
       current_price = get_price()
       check_price_drop(max_price, current_price)
       max_price = max(max_price, current_price)


