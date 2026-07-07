import yfinance as yf


def get_stock_news(ticker, limit=5):
    stock = yf.Ticker(ticker)

    try:
        news_list = stock.news
    except Exception:
        return []

    if not news_list:
        return []

    results = []

    for item in news_list[:limit]:
        results.append({
            "title": item.get("title", "제목 없음"),
            "publisher": item.get("publisher", "출처 없음"),
            "link": item.get("link", ""),
            "summary": item.get("summary", "")
        })

    return results