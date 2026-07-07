import streamlit as st
import yfinance as yf

@st.cache_data(ttl=300)
def get_market_data():
def get_market_data():
    markets = {
        "코스피": "^KS11",
        "코스닥": "^KQ11",
        "나스닥": "^IXIC",
        "S&P500": "^GSPC",
        "원/달러 환율": "KRW=X",
        "필라델피아 반도체": "^SOX",
    }

    result = {}

    for name, ticker in markets.items():
        data = yf.Ticker(ticker).history(period="5d")

        if data.empty or len(data) < 2:
            result[name] = None
            continue

        latest = data.iloc[-1]
        previous = data.iloc[-2]

        close = latest["Close"]
        prev_close = previous["Close"]
        change = ((close - prev_close) / prev_close) * 100

        result[name] = {
            "value": close,
            "change": change,
        }

    return result


def format_market_value(name, value):
    if value is None:
        return "N/A"

    if "환율" in name:
        return f"{value:,.2f}원"

    return f"{value:,.2f}"