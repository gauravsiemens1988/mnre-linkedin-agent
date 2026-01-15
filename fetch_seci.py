import feedparser

SECI_RSS = "https://www.seci.co.in/Upload/Latest-News/rss.xml"

def fetch_seci_news():
    feed = feedparser.parse(SECI_RSS)

    items = []
    for entry in feed.entries:
        items.append({
            "source": "SECI",
            "title": entry.title,
            "link": entry.link,
            "published": entry.get("published", "")
        })

    print(f"SECI fetched {len(items)} items")
    return items
