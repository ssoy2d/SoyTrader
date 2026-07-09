import streamlit as st


def score_card(title, score, message):
    if score >= 80:
        status = "매우 긍정적"
        emoji = "🟢"
    elif score >= 60:
        status = "긍정적"
        emoji = "🟡"
    else:
        status = "주의"
        emoji = "🔴"

    st.markdown(f"""
    <div class="score-card">
        <div class="small-label">{title}</div>
        <div class="score-number">{emoji} {score}</div>
        <h3>{status}</h3>
        <p>{message}</p>
    </div>
    """, unsafe_allow_html=True)


def watch_card(name, theme, score, memo):
    st.markdown(f"""
    <div class="watch-card">
        <h3>{name}</h3>
        <p>{theme}</p>
        <h2>{score}점</h2>
        <p>{memo}</p>
    </div>
    """, unsafe_allow_html=True)