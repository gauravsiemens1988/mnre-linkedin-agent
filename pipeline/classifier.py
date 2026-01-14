from filters.green_keywords import KEYWORDS

def classify(article_text):
    scores = {}

    for category, words in KEYWORDS.items():
        scores[category] = sum(
            1 for w in words if w.lower() in article_text.lower()
        )

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return "other"

    return best
