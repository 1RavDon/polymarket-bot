import requests
import time

url = "https://gamma-api.polymarket.com/markets"

while True:
    try:
        response = requests.get(url)
        markets = response.json()

        print("\n--- LIVE POLYMARKET MARKETS ---")

        for market in markets[:5]:
            question = market.get("question", "No question")
            print(question)

        print("\nRefreshing in 30 seconds...\n")

    except Exception as e:
        print("Error:", e)

    time.sleep(30)
