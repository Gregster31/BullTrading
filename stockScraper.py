import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def scrape_data(tickers):
    # Define headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
    }
    data = []

    for ticker in tickers:
        url = f'https://finance.yahoo.com/quote/{ticker}/'
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status() 
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Stock Ticker
            ticker_name = soup.find("h1", {"class": "yf-xxbei9"}).text.strip()
            # Stock price
            price = soup.find("fin-streamer", {"data-field": "regularMarketPrice"}).text.strip()
            # Price change
            change = soup.find("fin-streamer", {"data-field": "regularMarketChangePercent"}).text.strip()
            # Volume
            volume = soup.find('fin-streamer', {'data-field': 'regularMarketVolume'}).text.strip()
            
            data.append({
                'ticker': ticker_name,
                'price': price,
                'change': change,
                'volume': volume
            })
            
        except Exception as e:
            print(f"Error fetching data for URL {url}: {e}")            
        # try not to get banned by putting a 5 sec between requests
        # time.sleep(5)
    return data
            