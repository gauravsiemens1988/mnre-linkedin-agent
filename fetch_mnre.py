import feedparser

MNRE_RSS = "https://mnre.gov.in/feeds/latest_news.xml"

def fetch_mnre_news():
    feed = feedparser.parse(MNRE_RSS)

    items = []
    for entry in feed.entries:
        items.append({
            "title": entry.title,
            "url": entry.link,
            "source": "MNRE"
        })

    print(f"MNRE fetched {len(items)} items")
    return items
