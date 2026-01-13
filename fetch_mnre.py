import requests
from bs4 import BeautifulSoup
import json

MNRE_NEWS_URL = "https://mnre.gov.in/press-releases/"

def fetch_latest_news():
    response = requests.get(MNRE_NEWS_URL, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    news_items = []

    # MNRE press releases are listed as links
    for link in soup.select("a"):
        href = link.get("href", "")
        title = link.get_text(strip=True)

        if "/press-releases/" in href and title:
            full_url = href if href.startswith("http") else f"https://mnre.gov.in{href}"
            news_items.append({
                "title": title,
                "url": full_url
            })

    # Keep only latest 5 unique items
    unique_news = {item["url"]: item for item in news_items}
    latest_news = list(unique_news.values())[:5]

    with open("latest_news.json", "w", encoding="utf-8") as f:
        json.dump(latest_news, f, indent=2, ensure_ascii=False)

    print(f"Fetched {len(latest_news)} MNRE news items.")

if __name__ == "__main__":
    fetch_latest_news()
