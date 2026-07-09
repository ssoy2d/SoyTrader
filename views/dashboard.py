import streamlit as st
from datetime import datetime

from services.market import get_market_data, format_market_value
from services.briefing import create_daily_briefing
from components.cards import score_card, watch_card


def show_dashboard():
    today = datetime.now().strftime("%Y.%m.%d")

    st.markdown(f"""
    <div class="hero-card">
        <h1>🤖 SoyTrader</h1>
        <p>Good Morning, 소영님 ☀️</p>
        <p>AI Investment Assistant · {today}</p>
    </div>
    """, unsafe_allow_html=True)

    with st.spinner("📈 최신 시장 데이터를 불러오는 중..."):
        market_data = get_market_data()

    kospi = market_data.get("코스피")
    kosdaq = market_data.get("코스닥")
    nasdaq = market_data.get("나스닥")
    sp500 = market_data.get("S&P500")
    sox = market_data.get("필라델피아 반도체")
    exchange = market_data.get("원/달러 환율")

    score_card(
        "AI MARKET SCORE",
        84,
        "오늘은 미국 기술주와 반도체 업종 흐름을 우선 확인하는 장입니다."
    )

    st.markdown("## 🌍 실시간 시장")

    col1, col2, col3 = st.columns(3)
    col1.metric("🇰🇷 코스피", format_market_value("코스피", kospi["value"]) if kospi else "N/A", f'{kospi["change"]:.2f}%' if kospi else None)
    col2.metric("🇰🇷 코스닥", format_market_value("코스닥", kosdaq["value"]) if kosdaq else "N/A", f'{kosdaq["change"]:.2f}%' if kosdaq else None)
    col3.metric("🇺🇸 나스닥", format_market_value("나스닥", nasdaq["value"]) if nasdaq else "N/A", f'{nasdaq["change"]:.2f}%' if nasdaq else None)

    col4, col5, col6 = st.columns(3)
    col4.metric("🇺🇸 S&P500", format_market_value("S&P500", sp500["value"]) if sp500 else "N/A", f'{sp500["change"]:.2f}%' if sp500 else None)
    col5.metric("💾 SOX 반도체", format_market_value("필라델피아 반도체", sox["value"]) if sox else "N/A", f'{sox["change"]:.2f}%' if sox else None)
    col6.metric("💵 원/달러", format_market_value("원/달러 환율", exchange["value"]) if exchange else "N/A", f'{exchange["change"]:.2f}%' if exchange else None)

    st.markdown("## 🔥 오늘 관심종목")

    a, b, c = st.columns(3)

    with a:
        watch_card("삼성전자", "AI 메모리 · HBM", 84, "반도체 업황과 HBM 이슈 체크")

    with b:
        watch_card("현대차", "자동차 · 환율 수혜", 82, "환율과 미국 판매 흐름 체크")

    with c:
        watch_card("SK하이닉스", "HBM · AI 반도체", 88, "AI 서버 수요와 SOX 흐름 체크")

    st.markdown("## 🌅 오늘의 AI 브리핑")

    if st.button("🤖 오늘 브리핑 생성", use_container_width=True):
        with st.spinner("SoyTrader가 오늘 시장을 분석 중이에요..."):
            daily_briefing = create_daily_briefing(market_data)

        st.markdown(f"""
        <div class="ai-box">
            {daily_briefing}
        </div>
        """, unsafe_allow_html=True)