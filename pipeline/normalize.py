def normalize_article(article, source):
    return {
        "title": article.get("title", "").strip(),
        "summary": article.get("summary", "").strip(),
        "link": article.get("link"),
        "published": article.get("published"),
        "source": source,
    }
