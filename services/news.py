import streamlit as st
import yfinance as yf

@st.cache_data(ttl=300)
def get_stock_news(ticker, limit=5):
    try:
        stock = yf.Ticker(ticker)
        raw_news = stock.news
    except Exception:
        return []

    results = []

    for item in raw_news[:limit]:
        content = item.get("content", {})

        results.append({
            "title": item.get("title") or content.get("title") or "제목 없음",
            "publisher": item.get("publisher") or content.get("provider", {}).get("displayName") or "출처 없음",
            "link": item.get("link") or content.get("canonicalUrl", {}).get("url") or "",
            "summary": item.get("summary") or content.get("summary") or content.get("description") or ""
        })

    return results