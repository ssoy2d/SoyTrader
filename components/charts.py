import streamlit as st
import yfinance as yf
import plotly.graph_objects as go
from plotly.subplots import make_subplots


@st.cache_data(ttl=300)
def get_chart_data(ticker, period="3mo"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)

    if data.empty:
        return data

    data["MA5"] = data["Close"].rolling(window=5).mean()
    data["MA20"] = data["Close"].rolling(window=20).mean()
    data["MA60"] = data["Close"].rolling(window=60).mean()

    delta = data["Close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    data["RSI"] = 100 - (100 / (1 + rs))

    ema12 = data["Close"].ewm(span=12, adjust=False).mean()
    ema26 = data["Close"].ewm(span=26, adjust=False).mean()

    data["MACD"] = ema12 - ema26
    data["Signal"] = data["MACD"].ewm(span=9, adjust=False).mean()
    data["MACD_Hist"] = data["MACD"] - data["Signal"]

    return data


def show_advanced_chart(ticker, title="차트"):
    period = st.radio(
        "기간 선택",
        ["1mo", "3mo", "6mo", "1y"],
        horizontal=True,
        index=1
    )

    data = get_chart_data(ticker, period)

    if data.empty:
        st.warning("차트 데이터를 가져오지 못했어요.")
        return

    fig = make_subplots(
        rows=4,
        cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,
        row_heights=[0.5, 0.18, 0.16, 0.16],
        subplot_titles=(
            f"{title} 캔들차트",
            "거래량",
            "RSI",
            "MACD"
        )
    )

    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data["Open"],
            high=data["High"],
            low=data["Low"],
            close=data["Close"],
            name="캔들"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA5"],
            mode="lines",
            name="MA5"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA20"],
            mode="lines",
            name="MA20"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MA60"],
            mode="lines",
            name="MA60"
        ),
        row=1,
        col=1
    )

    fig.add_trace(
        go.Bar(
            x=data.index,
            y=data["Volume"],
            name="거래량"
        ),
        row=2,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["RSI"],
            mode="lines",
            name="RSI"
        ),
        row=3,
        col=1
    )

    fig.add_hline(y=70, line_dash="dash", row=3, col=1)
    fig.add_hline(y=30, line_dash="dash", row=3, col=1)

    fig.add_trace(
        go.Bar(
            x=data.index,
            y=data["MACD_Hist"],
            name="MACD Histogram"
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["MACD"],
            mode="lines",
            name="MACD"
        ),
        row=4,
        col=1
    )

    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data["Signal"],
            mode="lines",
            name="Signal"
        ),
        row=4,
        col=1
    )

    fig.update_layout(
        height=900,
        template="plotly_white",
        xaxis_rangeslider_visible=False,
        margin=dict(l=20, r=20, t=60, b=20),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    st.plotly_chart(fig, use_container_width=True)