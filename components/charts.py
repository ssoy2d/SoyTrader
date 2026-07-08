import yfinance as yf
import plotly.graph_objects as go
import streamlit as st


@st.cache_data(ttl=300)
def get_chart_data(ticker):
    stock = yf.Ticker(ticker)
    return stock.history(period="3mo")


def show_candlestick_chart(ticker, title="차트"):
    st.write("✅ 차트 함수 실행됨")
    st.write(f"Ticker: {ticker}")

    data = get_chart_data(ticker)

    if data.empty:
        st.warning("차트 데이터를 가져오지 못했어요.")
        return

    fig = go.Figure()

    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name=title
        )
    )

    fig.update_layout(
        title=title,
        height=500,
        xaxis_rangeslider_visible=False,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    st.plotly_chart(fig, use_container_width=True)