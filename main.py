import streamlit as st
import yfinance as yf
import pandas as pd  # Import pandas for DataFrame operations
from streamlit_option_menu import option_menu

# Set Streamlit configuration
st.set_page_config(page_title="Stock Dashboard", layout="wide")

# CSS for the sleek black design and sidebar layout
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
    }
    .stApp {
        background-color: #121212;
    }
    .sidebar .css-1v3fvcr {
        background-color: #1E1E1E;
        color: white;
    }
    .css-1v3fvcr a {
        color: white;
    }
    .css-qbe2hs {
        padding-top: 10px;
    }
    .navigation-title {
        font-size: 18px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation with emojis and titles
st.sidebar.image("./img/logo.png", use_container_width=True)

with st.sidebar:
    selected=option_menu(
        menu_title="Menu",
        options=[
            "🏠 Home",
            "🌍 Broad Markets",
            "📊 Sector Analysis",
            "📈 Stock Analysis",
            "⭐ Favorites List"
        ], 
        default_index=0,   
    )

# Home view: Display favorites and broad markets
if selected == "🏠 Home":
    st.title("🏠 Home")
    st.header("⭐ Favorite Stocks")
    favorite_stocks = ["AAPL", "TSLA", "MSFT", "AMZN"]
    
    # Display a table for favorite stocks
    favorite_data = []
    for stock in favorite_stocks:
        data = yf.Ticker(stock).history(period="1d")
        favorite_data.append([stock, data['Open'][0], data['Close'][0]])
    st.table(pd.DataFrame(favorite_data, columns=["Ticker", "Open", "Close"]))

    st.header("🌍 Broad Markets")
    broad_markets = {"S&P 500": "^GSPC", "Dow Jones": "^DJI", "Nasdaq": "^IXIC"}
    broad_data = []
    for name, ticker in broad_markets.items():
        data = yf.Ticker(ticker).history(period="1d")
        broad_data.append([name, data['Open'][0], data['Close'][0]])
    st.table(pd.DataFrame(broad_data, columns=["Market", "Open", "Close"]))

# Broad Markets view: Small charts for indices
elif selected == "🌍 Broad Markets":
    st.title("🌍 Broad Markets")
    indices = ["^GSPC", "^DJI", "^IXIC"]
    for index in indices:
        data = yf.Ticker(index).history(period="1mo")
        st.subheader(f"{index} Trend")
        st.line_chart(data["Close"])

# Sector Analysis view: Small charts for sectors
elif selected == "📊 Sector Analysis":
    st.title("📊 Sector Analysis")
    sectors = {"Consumer": "XLY", "Energy": "XLE", "Technology": "XLK"}
    for sector, ticker in sectors.items():
        data = yf.Ticker(ticker).history(period="1mo")
        st.subheader(f"{sector} Sector Trend")
        st.line_chart(data["Close"])

# Stock Analysis view: Search bar to fetch stock info
elif selected == "📈 Stock Analysis":
    st.title("📈 Stock Analysis")
    ticker = st.text_input("Enter Stock Ticker:", value="AAPL").upper()
    if ticker:
        stock = yf.Ticker(ticker)
        info = stock.info
        st.write(f"**Name:** {info['longName']}")
        st.write(f"**Industry:** {info.get('industry', 'N/A')}")
        st.write(f"**Market Cap:** {info.get('marketCap', 'N/A')}")
        st.write(f"**Previous Close:** {info['previousClose']}")
        st.write(f"**Open:** {info['open']}")
        st.line_chart(stock.history(period="1mo")["Close"])

# Favorites List view
elif selected == "⭐ Favorites List":
    st.title("⭐ Favorites List")
    st.write("This page can allow users to manage their favorite stocks.")
