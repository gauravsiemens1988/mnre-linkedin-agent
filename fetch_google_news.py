import feedparser

GOOGLE_NEWS_RSS = (
    "https://news.google.com/rss/search?"
    "q=green+energy+OR+green+hydrogen+OR+solar+OR+green+ammonia"
    "&hl=en-IN&gl=IN&ceid=IN:en"
)

def fetch_google_green_news():
    feed = feedparser.parse(GOOGLE_NEWS_RSS)

    items = []
    for entry in feed.entries:
        items.append({
            "title": entry.title,
            "url": entry.link,
            "source": "Google News"
        })

    print(f"Google News fetched {len(items)} items")
    return items
