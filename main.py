from stock import get_stock_data
from gpt import ask_gpt
from config import STOCKS

print("=" * 40)
print("🤖 SoyTrader")
print("=" * 40)

for key, (company, _) in STOCKS.items():
    print(f"{key}. {company}")

custom_menu = str(len(STOCKS) + 1)
exit_menu = str(len(STOCKS) + 2)

print(f"{custom_menu}. 직접 입력")
print(f"{exit_menu}. 종료")

menu = input("\n번호를 입력하세요 : ")

if menu in STOCKS:
    company, ticker = STOCKS[menu]

elif menu == custom_menu:
    ticker = input("종목코드 입력 (예: 005930.KS): ")
    company = ticker

else:
    print("프로그램을 종료합니다.")
    exit()

stock = get_stock_data(ticker)

if stock is None:
    print("주가 데이터를 가져오지 못했습니다.")
    exit()

prompt = f"""
너는 대한민국 최고의 주식 애널리스트다.

종목 : {company}

현재가 : {stock["price"]:,.0f}원
등락률 : {stock["change"]:.2f}%
거래량 : {stock["volume"]:,.0f}

위 정보를 바탕으로

1. 오늘 시장 상황
2. 투자 포인트
3. 리스크
4. 한줄 요약

을 이해하기 쉽게 설명해줘.
"""

answer = ask_gpt(prompt)

print("\n" + "=" * 40)
print(answer)
print("=" * 40)