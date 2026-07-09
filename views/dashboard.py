import streamlit as st
from datetime import datetime
from services.briefing import create_daily_briefing

from services.market import get_market_data, format_market_value
from services.gpt import ask_gpt


def show_dashboard():
    today = datetime.now().strftime("%Y.%m.%d")

    st.markdown(f"""
<div class="hero-card">
    <h1>🤖 SoyTrader</h1>
    <p>AI Investment Assistant</p>
    <p>📅 {today}</p>
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

    st.markdown("## 🌅 오늘의 AI 브리핑")

    if st.button("🤖 오늘 브리핑 생성", use_container_width=True):
        with st.spinner("SoyTrader가 오늘 시장을 분석 중이에요..."):
            daily_briefing = create_daily_briefing(market_data)

        st.markdown(f"""
        <div class="ai-box">
            {daily_briefing}
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("## 🟢 AI Market Score")
    st.success("82점")
    st.info("오늘은 반도체 업종과 미국 기술주 흐름을 함께 봐야 하는 장입니다.")

    st.markdown("## 🌍 실시간 시장")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🇰🇷 코스피",
        format_market_value("코스피", kospi["value"]) if kospi else "N/A",
        f'{kospi["change"]:.2f}%' if kospi else None
    )

    col2.metric(
        "🇰🇷 코스닥",
        format_market_value("코스닥", kosdaq["value"]) if kosdaq else "N/A",
        f'{kosdaq["change"]:.2f}%' if kosdaq else None
    )

    col3.metric(
        "🇺🇸 나스닥",
        format_market_value("나스닥", nasdaq["value"]) if nasdaq else "N/A",
        f'{nasdaq["change"]:.2f}%' if nasdaq else None
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "🇺🇸 S&P500",
        format_market_value("S&P500", sp500["value"]) if sp500 else "N/A",
        f'{sp500["change"]:.2f}%' if sp500 else None
    )

    col5.metric(
        "💾 SOX 반도체",
        format_market_value("필라델피아 반도체", sox["value"]) if sox else "N/A",
        f'{sox["change"]:.2f}%' if sox else None
    )

    col6.metric(
        "💵 원/달러",
        format_market_value("원/달러 환율", exchange["value"]) if exchange else "N/A",
        f'{exchange["change"]:.2f}%' if exchange else None
    )

    st.markdown("## 🔥 오늘 관심종목")

    a, b, c = st.columns(3)

    a.markdown("""
    <div class="card">
        <h3>삼성전자</h3>
        <p>AI 메모리 · HBM</p>
        <b>⭐⭐⭐⭐☆</b>
    </div>
    """, unsafe_allow_html=True)

    b.markdown("""
    <div class="card">
        <h3>현대차</h3>
        <p>자동차 · 환율 수혜</p>
        <b>⭐⭐⭐⭐☆</b>
    </div>
    """, unsafe_allow_html=True)

    c.markdown("""
    <div class="card">
        <h3>SK하이닉스</h3>
        <p>HBM · AI 반도체</p>
        <b>⭐⭐⭐⭐⭐</b>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🤖 AI 시장 브리핑")

    if st.button("🧠 AI 브리핑 생성", use_container_width=True):
        market_prompt = f"""
너는 개인 투자자를 위한 시장 전략가야.

아래 시장 데이터를 바탕으로 오늘 시장을 쉽게 브리핑해줘.

[시장 데이터]
코스피: {format_market_value("코스피", kospi["value"]) if kospi else "N/A"} / 등락률: {f'{kospi["change"]:.2f}%' if kospi else "N/A"}
코스닥: {format_market_value("코스닥", kosdaq["value"]) if kosdaq else "N/A"} / 등락률: {f'{kosdaq["change"]:.2f}%' if kosdaq else "N/A"}
나스닥: {format_market_value("나스닥", nasdaq["value"]) if nasdaq else "N/A"} / 등락률: {f'{nasdaq["change"]:.2f}%' if nasdaq else "N/A"}
S&P500: {format_market_value("S&P500", sp500["value"]) if sp500 else "N/A"} / 등락률: {f'{sp500["change"]:.2f}%' if sp500 else "N/A"}
필라델피아 반도체: {format_market_value("필라델피아 반도체", sox["value"]) if sox else "N/A"} / 등락률: {f'{sox["change"]:.2f}%' if sox else "N/A"}
원/달러 환율: {format_market_value("원/달러 환율", exchange["value"]) if exchange else "N/A"} / 등락률: {f'{exchange["change"]:.2f}%' if exchange else "N/A"}

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

        st.markdown(f"""
        <div class="ai-box">
            {briefing}
        </div>
        """, unsafe_allow_html=True)