import streamlit as st


def load_css():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #F8FAFC 0%, #EEF4FF 100%);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1280px;
    }

    section[data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    h1, h2, h3 {
        color: #0F172A;
        font-weight: 800;
        letter-spacing: -0.03em;
    }

    p {
        color: #475569;
    }

    div[data-testid="metric-container"] {
        background: #FFFFFF;
        border-radius: 22px;
        padding: 22px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.07);
        transition: all 0.25s ease;
    }

    div[data-testid="metric-container"]:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.12);
    }

    .hero-card {
        background: linear-gradient(135deg, #2563EB 0%, #60A5FA 100%);
        padding: 34px;
        border-radius: 30px;
        color: white;
        margin-bottom: 28px;
        box-shadow: 0 18px 45px rgba(37, 99, 235, 0.25);
    }

    .hero-card h1 {
        color: white;
        margin-bottom: 8px;
        font-size: 42px;
    }

    .hero-card p {
        color: #EFF6FF;
        font-size: 17px;
        margin-bottom: 4px;
    }

    .section-card {
        background: #FFFFFF;
        padding: 24px;
        border-radius: 26px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.07);
        margin-bottom: 24px;
    }

    .ai-box {
        background: #F8FAFC;
        border: 1px solid #DBEAFE;
        border-left: 8px solid #2563EB;
        padding: 22px;
        border-radius: 22px;
        margin-top: 16px;
        box-shadow: 0 8px 25px rgba(37, 99, 235, 0.08);
        white-space: pre-wrap;
    }

    .watch-card {
        background: #FFFFFF;
        padding: 22px;
        border-radius: 24px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.07);
        transition: all 0.25s ease;
        min-height: 150px;
    }

    .watch-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.12);
    }

    .watch-card h3 {
        margin-bottom: 8px;
        color: #0F172A;
    }

    .watch-card p {
        margin-bottom: 10px;
        color: #64748B;
    }

    .score-card {
        background: #FFFFFF;
        padding: 28px;
        border-radius: 28px;
        border: 1px solid #E5E7EB;
        box-shadow: 0 12px 35px rgba(15, 23, 42, 0.08);
        margin-bottom: 24px;
    }

    .score-number {
        font-size: 56px;
        font-weight: 900;
        color: #2563EB;
        line-height: 1;
    }

    .small-label {
        font-size: 14px;
        color: #64748B;
        font-weight: 600;
    }

    div.stButton > button {
        border-radius: 16px;
        border: none;
        background: linear-gradient(135deg, #2563EB 0%, #60A5FA 100%);
        color: white;
        font-weight: 700;
        padding: 0.75rem 1.2rem;
        box-shadow: 0 10px 25px rgba(37, 99, 235, 0.22);
        transition: all 0.25s ease;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 15px 35px rgba(37, 99, 235, 0.3);
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)