import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="5d")

    if data.empty or len(data) < 2:
        return None

    latest = data.iloc[-1]
    previous = data.iloc[-2]

    close = latest["Close"]
    prev_close = previous["Close"]
    change = ((close - prev_close) / prev_close) * 100
    volume = latest["Volume"]

    return {
        "price": close,
        "change": change,
        "volume": volume
    }