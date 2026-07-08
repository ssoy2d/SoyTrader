import streamlit as st

from config import STOCKS
from services.stock import get_stock_data
from services.gpt import ask_gpt
from services.news import get_stock_news
from components.charts import show_advanced_chart


def show_stock_page():
    st.title("📊 종목 분석")
    stock_names = [company for company, ticker in STOCKS.values()]
    selected_name = st.selectbox("🔍 종목 선택", stock_names)

    selected_ticker = None
    for company, ticker in STOCKS.values():
        if company == selected_name:
            selected_ticker = ticker

    st.divider()
    st.subheader("📈 전문가 차트")
    show_advanced_chart(selected_ticker, selected_name)

    if st.button("🤖 AI 분석하기", use_container_width=True):
        with st.spinner("AI가 종목을 분석하는 중입니다..."):
            stock = get_stock_data(selected_ticker)

            if stock is None:
                st.error("주가 데이터를 가져오지 못했습니다.")
                return

            col1, col2, col3 = st.columns(3)

            col1.metric("현재가", f'{stock["price"]:,.0f}원')
            col2.metric("등락률", f'{stock["change"]:.2f}%')
            col3.metric("거래량", f'{stock["volume"]:,.0f}')

            prompt = f"""
너는 대한민국 최고의 주식 애널리스트다.

종목: {selected_name}
현재가: {stock["price"]:,.0f}원
등락률: {stock["change"]:.2f}%
거래량: {stock["volume"]:,.0f}

아래 형식으로 설명해줘.

1. 오늘 흐름
2. 투자 포인트
3. 리스크
4. 한줄 요약

매수/매도는 단정하지 말 것.
"""

            answer = ask_gpt(prompt)

        st.divider()
        st.subheader("🤖 AI 종목 분석")
        st.info(answer)

        st.divider()
        st.subheader("📰 관련 뉴스")

        news_list = get_stock_news(selected_ticker)

        if not news_list:
            st.warning("관련 뉴스를 가져오지 못했습니다.")
        else:
            for i, news in enumerate(news_list):
                st.markdown(f"### {news['title']}")
                st.caption(news["publisher"])

                if news["link"]:
                    st.link_button("기사 보기", news["link"])

                st.divider()