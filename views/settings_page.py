import streamlit as st


def show_settings_page():
    st.title("⚙️ 설정")

    st.markdown("""
    <div class="card">
        <h3>SoyTrader</h3>
        <p>AI 투자비서</p>
        <p><b>Version:</b> v1.0 refactor</p>
    </div>
    """, unsafe_allow_html=True)

    st.info("API Key는 Streamlit Secrets 또는 .env에서 관리합니다.")