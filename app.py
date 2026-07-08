import streamlit as st

from components.styles import load_css

from views.dashboard import show_dashboard
from views.stock_page import show_stock_page
from views.news_page import show_news_page
from views.portfolio_page import show_portfolio_page
from views.settings_page import show_settings_page


st.set_page_config(
    page_title="SoyTrader",
    page_icon="🤖",
    layout="wide"

)

load_css()

menu = st.sidebar.radio(
    "메뉴",
    [
        "🏠 Dashboard",
        "📊 종목 분석",
        "📰 뉴스 분석",
        "💼 포트폴리오",
        "⚙️ 설정"
    ]
)

if menu == "🏠 Dashboard":
    show_dashboard()

elif menu == "📊 종목 분석":
    show_stock_page()

elif menu == "📰 뉴스 분석":
    show_news_page()

elif menu == "💼 포트폴리오":
    show_portfolio_page()

elif menu == "⚙️ 설정":
    show_settings_page()