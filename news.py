import yfinance as yf


def get_stock_news(ticker, limit=5):
    stock = yf.Ticker(ticker)

    try:
        raw_news = stock.news
    except Exception:
        return []

    results = []

    for item in raw_news[:limit]:
        content = item.get("content", {})

        title = (
            item.get("title")
            or content.get("title")
            or "제목 없음"
        )

        publisher = (
            item.get("publisher")
            or content.get("provider", {}).get("displayName")
            or "출처 없음"
        )

        link = (
            item.get("link")
            or content.get("canonicalUrl", {}).get("url")
            or ""
        )

        summary = (
            item.get("summary")
            or content.get("summary")
            or content.get("description")
            or ""
        )

        results.append({
            "title": title,
            "publisher": publisher,
            "link": link,
            "summary": summary
        })

    return results