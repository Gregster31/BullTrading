import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
}

# URLs to search through
urls = [
    'https://finance.yahoo.com/quote/NKE/',  # Nike Stock
    'https://finance.yahoo.com/quote/AAPL/'  # Apple Stock
]

# Stock infos
infos = []

for url in urls:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Stock Ticker
        ticker = soup.find("h1", {"class": "yf-xxbei9"}).text.strip()
        # Stock price
        price = soup.find("fin-streamer", {"data-field": "regularMarketPrice"}).text.strip()
        # Price change
        change = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"}).text.strip()
        # Volume
        volume = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'}).text.strip()
        
        current_infos = [ticker, price, change, volume]
        infos.append(current_infos)
        
        print(f"Ticker: {ticker}")
        print(f"Price: {price}")
        print(f"Change: {change}")
        print(f"Volume: {volume}")
        print("-" * 50)
        
    except Exception as e:
        print(f"Error fetching data for URL {url}: {e}")
        