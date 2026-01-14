def score(article):
    score = 0

    if article["category"] in ["policy", "hydrogen", "green_ammonia"]:
        score += 3

    if "MNRE" in article["title"] or "SECI" in article["title"]:
        score += 2

    if "tender" in article["title"].lower():
        score += 2

    return score
