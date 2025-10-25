import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("FINNHUB_API_KEY")
SYMBOL = "000660.KS"  # SK hynix

def fetch_financials(symbol):
    """재무제표 호출"""
    url = f"https://finnhub.io/api/v1/stock/financials"
    params = {
        "symbol": symbol,
        "statement": "ic",  # 손익계산서 (bs=대차대조표, cf=현금흐름표)
        "freq": "annual",
        "token": API_KEY,
    }
    res = requests.get(url, params=params)
    if res.status_code != 200:
        raise Exception(f"HTTP {res.status_code}: {res.text}")
    return res.json()

def fetch_quote(symbol):
    """현재가 호출"""
    url = f"https://finnhub.io/api/v1/quote"
    params = {"symbol": symbol, "token": API_KEY}
    res = requests.get(url, params=params)
    return res.json()

def main():
    print(f"🔍 Checking SK hynix ({SYMBOL}) ...")

    quote = fetch_quote(SYMBOL)
    print(f"📈 Current price data: {quote}")

    data = fetch_financials(SYMBOL)
    if not data or not data.get("financials"):
        print("❌ 재무제표 데이터가 None 또는 비어있습니다.")
    else:
        print("✅ 재무제표 데이터가 존재합니다.")
        print(f"항목 수: {len(data['financials'])}")
        print(f"예시 항목: {list(data['financials'][0].keys())[:10]}")

if __name__ == "__main__":
    main()
