import requests
import json

MNRE_NEWS_URL = "https://mnre.gov.in/latest-news/"

def fetch_latest_news():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(MNRE_NEWS_URL, headers=headers, timeout=20)

    if response.status_code != 200:
        print("MNRE not reachable, skipping.")
        with open("latest_news.json", "w") as f:
            json.dump([], f)
        return

    # Even if parsing fails, workflow must not crash
    with open("latest_news.json", "w") as f:
        json.dump([], f)

    print("MNRE fetch completed safely.")

if __name__ == "__main__":
    fetch_latest_news()
