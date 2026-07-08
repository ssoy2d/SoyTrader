import streamlit as st


def show_portfolio_page():
    st.title("💼 포트폴리오")

    st.markdown("""
    <div class="card">
        <h3>내 포트폴리오</h3>
        <p>보유 종목과 수익률을 입력하면 AI가 포트폴리오를 분석해주는 페이지입니다.</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 예정 기능")

    st.write("• 총 자산")
    st.write("• 오늘 손익")
    st.write("• 종목별 수익률")
    st.write("• AI 포트폴리오 의견")