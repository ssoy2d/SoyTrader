from services.gpt import ask_gpt
from services.market import format_market_value


def create_daily_briefing(market_data):
    kospi = market_data.get("코스피")
    kosdaq = market_data.get("코스닥")
    nasdaq = market_data.get("나스닥")
    sp500 = market_data.get("S&P500")
    sox = market_data.get("필라델피아 반도체")
    exchange = market_data.get("원/달러 환율")

    prompt = f"""
너는 개인 투자자를 위한 AI 투자비서 SoyTrader야.

아래 시장 데이터를 바탕으로 소영님이 오늘 시장을 빠르게 이해할 수 있게 브리핑해줘.

[시장 데이터]
코스피: {format_market_value("코스피", kospi["value"]) if kospi else "N/A"} / {f'{kospi["change"]:.2f}%' if kospi else "N/A"}
코스닥: {format_market_value("코스닥", kosdaq["value"]) if kosdaq else "N/A"} / {f'{kosdaq["change"]:.2f}%' if kosdaq else "N/A"}
나스닥: {format_market_value("나스닥", nasdaq["value"]) if nasdaq else "N/A"} / {f'{nasdaq["change"]:.2f}%' if nasdaq else "N/A"}
S&P500: {format_market_value("S&P500", sp500["value"]) if sp500 else "N/A"} / {f'{sp500["change"]:.2f}%' if sp500 else "N/A"}
SOX 반도체: {format_market_value("필라델피아 반도체", sox["value"]) if sox else "N/A"} / {f'{sox["change"]:.2f}%' if sox else "N/A"}
원/달러 환율: {format_market_value("원/달러 환율", exchange["value"]) if exchange else "N/A"} / {f'{exchange["change"]:.2f}%' if exchange else "N/A"}

관심종목:
삼성전자, 현대차, SK하이닉스

아래 형식으로 작성해줘.

🌅 오늘의 AI 브리핑

1. 오늘 시장 분위기
2. 반도체 업종 체크포인트
3. 환율이 주식시장에 주는 영향
4. 오늘 소영님이 봐야 할 종목
5. 한줄 전략

단, 매수/매도는 단정하지 말고 신중하게 말해줘.
"""

    return ask_gpt(prompt)