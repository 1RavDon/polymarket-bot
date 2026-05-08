import requests
import time

BOT_TOKEN = "8379444114:AAFVs3vNoWllD1czc-GR0ifpWCqaFAE7RGc"
CHAT_ID = "8592614390"

url = "https://gamma-api.polymarket.com/markets"

paper_trades = {}

def send_telegram_message(message):

    telegram_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(telegram_url, data=payload)

while True:

    try:

        response = requests.get(url)
        markets = response.json()

        print("\n=== TELEGRAM PAPER TRADING BOT ===\n")

        for market in markets[:50]:

            question = market.get("question", "Unknown")

            change = market.get("oneDayPriceChange", 0)

            price = market.get("lastTradePrice", 0)

            if abs(change) >= 0.01:

                if question not in paper_trades:

                    paper_trades[question] = price

                    alert = f"""
🟢 PAPER BUY SIGNAL

Market:
{question}

Entry Price:
{price}

24h Change:
{round(change * 100, 2)}%
"""

                    print(alert)

                    send_telegram_message(alert)

        print("\nRefreshing in 60 seconds...\n")

    except Exception as e:

        print("Error:", e)

    time.sleep(60)
