import streamlit as st


def show_news_page():
    st.title("📰 뉴스 분석")

    st.markdown("""
    <div class="card">
        <h3>AI 뉴스 분석</h3>
        <p>시장 뉴스, 종목 뉴스, 업종별 이슈를 분석하는 페이지입니다.</p>
        <p>다음 버전에서 실시간 뉴스 요약 기능을 추가할 예정입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("현재 뉴스 기능은 📊 종목 분석 페이지에서 먼저 사용할 수 있어요.")