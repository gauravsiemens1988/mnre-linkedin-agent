import requests
from bs4 import BeautifulSoup
import json

MNRE_NEWS_URL = "https://mnre.gov.in/latest-news/"

def fetch_latest_news():
    headers = {
        "User-Agent": "Mozilla/5.0 (MNRE-Agent/1.0)"
    }

    response = requests.get(MNRE_NEWS_URL, headers=headers, timeout=20)

    # Do NOT crash on HTTP error
    if response.status_code != 200:
        print(f"MNRE site returned status {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    news_items = []

    for link in soup.find_all("a", href=True):
        title = link.get_text(strip=True)
        href = link["href"]

        if title and "/latest-news/" in href:
            full_url = href if href.startswith("http") else f"https://mnre.gov.in{href}"
            news_items.append({
                "title": title,
                "url": full_url
            })

    # Remove duplicates & keep latest 5
    unique = {item["url"]: item for item in news_items}
    latest_news = list(unique.values())[:5]

    with open("latest_news.json", "w", encoding="utf-8") as f:
        json.dump(latest_news, f, indent=2, ensure_ascii=False)

    print(f"Fetched {len(latest_news)} MNRE news items.")

if __name__ == "__main__":
    fetch_latest_news()

