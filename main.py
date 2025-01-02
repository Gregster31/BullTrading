import streamlit as st
import yfinance as yf
import pandas as pd

# Set page layout and title
st.set_page_config(page_title="Stock Dashboard", layout="wide")

# CSS for styling the dashboard
st.markdown("""
    <style>
    body {
        background-color: #0E0E0E;
        color: white;
    }
    .stApp {
        background-color: #0E0E0E;
    }
    .css-18e3th9 {
        background-color: #0E0E0E;
    }
    .css-1v0mbdj {
        color: white;
    }
    .css-1c9lclm {
        background-color: #1F1F1F;
    }
    </style>
""", unsafe_allow_html=True)

# Create sidebar navigation
st.sidebar.title("Stock Dashboard")
option = st.sidebar.radio(
    "Select a page",
    ["Home", "Stock Info", "Stock History"]
)

# Home page
if option == "Home":
    st.title("Welcome to the Stock Dashboard!")
    st.write("Use this dashboard to track stock information and view historical data.")

# Stock info page
if option == "Stock Info":
    st.title("Stock Information")

    ticker_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    stock_data = yf.Ticker(ticker_symbol)
    
    try:
        # Display stock info
        st.subheader(f"Information for {ticker_symbol}")
        info = stock_data.info
        st.write(f"**Name:** {info['longName']}")
        st.write(f"**Sector:** {info['sector']}")
        st.write(f"**Industry:** {info['industry']}")
        st.write(f"**Market Cap:** {info['marketCap']}")
        st.write(f"**Current Price:** ${info['currentPrice']}")
        st.write(f"**52-Week High:** ${info['fiftyTwoWeekHigh']}")
        st.write(f"**52-Week Low:** ${info['fiftyTwoWeekLow']}")
    except Exception as e:
        st.write("Error fetching data: ", e)

# Stock history page
if option == "Stock History":
    st.title("Stock Historical Data")

    ticker_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    stock_data = yf.Ticker(ticker_symbol)

    try:
        # Display stock historical data
        st.subheader(f"Historical Data for {ticker_symbol}")
        start_date = st.date_input("Start Date", pd.to_datetime('2020-01-01'))
        end_date = st.date_input("End Date", pd.to_datetime('today'))
        
        # Get historical stock data
        historical_data = stock_data.history(period="1d", start=start_date, end=end_date)
        
        st.write("Stock Data")
        st.dataframe(historical_data)
        
        # Plot stock data
        st.subheader("Stock Price Trend")
        st.line_chart(historical_data['Close'])
    except Exception as e:
        st.write("Error fetching data: ", e)
