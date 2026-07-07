import streamlit as st

from stock import get_stock_data
from gpt import ask_gpt
from config import STOCKS
from market import get_market_data, format_market_value
from news import get_stock_news

st.set_page_config(
    page_title="SoyTrader",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 SoyTrader")
st.write("소영이의 AI 투자비서")

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
    st.header("🏠 Dashboard")
    st.success("좋은 오후입니다, 소영님 😊")

    with st.spinner("시장 데이터를 가져오는 중이에요..."):
        market_data = get_market_data()

    col1, col2, col3 = st.columns(3)

    kospi = market_data.get("코스피")
    nasdaq = market_data.get("나스닥")
    exchange = market_data.get("원/달러 환율")

    col1.metric(
        "KR 코스피",
        format_market_value("코스피", kospi["value"]) if kospi else "N/A",
        f'{kospi["change"]:.2f}%' if kospi else None
    )

    col2.metric(
        "US 나스닥",
        format_market_value("나스닥", nasdaq["value"]) if nasdaq else "N/A",
        f'{nasdaq["change"]:.2f}%' if nasdaq else None
    )

    col3.metric(
        "원/달러 환율",
        format_market_value("원/달러 환율", exchange["value"]) if exchange else "N/A",
        f'{exchange["change"]:.2f}%' if exchange else None
    )

    st.divider()

    st.subheader("📌 주요 시장 지표")

    col4, col5, col6 = st.columns(3)

    kosdaq = market_data.get("코스닥")
    sp500 = market_data.get("S&P500")
    sox = market_data.get("필라델피아 반도체")

    col4.metric(
        "KR 코스닥",
        format_market_value("코스닥", kosdaq["value"]) if kosdaq else "N/A",
        f'{kosdaq["change"]:.2f}%' if kosdaq else None
    )

    col5.metric(
        "US S&P500",
        format_market_value("S&P500", sp500["value"]) if sp500 else "N/A",
        f'{sp500["change"]:.2f}%' if sp500 else None
    )

    col6.metric(
        "SOX 반도체",
        format_market_value("필라델피아 반도체", sox["value"]) if sox else "N/A",
        f'{sox["change"]:.2f}%' if sox else None
    )

    st.divider()

    st.subheader("🔥 오늘 관심 종목")
    st.write("• 삼성전자")
    st.write("• 현대차")
    st.write("• SK하이닉스")

    st.divider()

    st.subheader("🤖 AI 시장 브리핑")

if st.button("🧠 AI 브리핑 생성하기"):
    market_prompt = f"""
너는 개인 투자자를 위한 시장 전략가야.

아래 시장 데이터를 바탕으로 오늘 시장을 쉽게 브리핑해줘.

[시장 데이터]
코스피: {format_market_value("코스피", kospi["value"]) if kospi else "N/A"} / 등락률 {kospi["change"]:.2f}% if kospi else "N/A"
코스닥: {format_market_value("코스닥", kosdaq["value"]) if kosdaq else "N/A"} / 등락률 {kosdaq["change"]:.2f}% if kosdaq else "N/A"
나스닥: {format_market_value("나스닥", nasdaq["value"]) if nasdaq else "N/A"} / 등락률 {nasdaq["change"]:.2f}% if nasdaq else "N/A"
S&P500: {format_market_value("S&P500", sp500["value"]) if sp500 else "N/A"} / 등락률 {sp500["change"]:.2f}% if sp500 else "N/A"
필라델피아 반도체: {format_market_value("필라델피아 반도체", sox["value"]) if sox else "N/A"} / 등락률 {sox["change"]:.2f}% if sox else "N/A"
원/달러 환율: {format_market_value("원/달러 환율", exchange["value"]) if exchange else "N/A"} / 등락률 {exchange["change"]:.2f}% if exchange else "N/A"

아래 형식으로 작성해줘.

1. 오늘 시장 분위기
2. 반도체 업종 해석
3. 국내 증시 주의점
4. 오늘 소영이가 봐야 할 포인트
5. 한줄 요약

단, 확정적인 매수/매도 지시는 하지 말고 신중하게 말해줘.
"""

    with st.spinner("GPT가 시장을 분석 중이에요..."):
        briefing = ask_gpt(market_prompt)

    st.write(briefing)

elif menu == "📊 종목 분석":
    st.header("📊 종목 분석")

    stock_names = [company for company, ticker in STOCKS.values()]
    selected_name = st.selectbox("종목 선택", stock_names)

    selected_ticker = None
    for company, ticker in STOCKS.values():
        if company == selected_name:
            selected_ticker = ticker

    if st.button("🔍 AI 분석하기"):
        with st.spinner("주가 데이터를 가져오고 GPT가 분석 중이에요..."):
            stock = get_stock_data(selected_ticker)

            if stock is None:
                st.error("주가 데이터를 가져오지 못했어요.")
            else:
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

위 정보를 바탕으로 아래 형식으로 쉽게 분석해줘.

1. 오늘 흐름
2. 투자 포인트
3. 리스크
4. 한줄 요약

단, 확정적인 매수/매도 지시는 하지 말고 신중하게 말해줘.
"""

                answer = ask_gpt(prompt)

                st.subheader("🤖 GPT 분석 결과")
                st.write(answer)
                st.divider()
                st.subheader("📰 관련 뉴스")

                news_list = get_stock_news(selected_ticker)

                if not news_list:
                    st.info("관련 뉴스를 가져오지 못했어요.")
                else:
                    for news in news_list:
                        st.markdown(f"**{news['title']}**")
                        st.caption(news["publisher"])

                        if news["link"]:
                            st.markdown(f"[기사 보기]({news['link']})")

                        st.write("---")

elif menu == "📰 뉴스 분석":
    st.header("📰 뉴스 분석")
    st.info("뉴스 분석 기능은 다음 단계에서 만들 예정!")

elif menu == "💼 포트폴리오":
    st.header("💼 포트폴리오")
    st.info("소영이 보유 종목 분석 기능은 다음 단계에서 만들 예정!")

elif menu == "⚙️ 설정":
    st.header("⚙️ 설정")
    st.write("SoyTrader v0.4")