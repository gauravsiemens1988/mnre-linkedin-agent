from generator.prompt_templates import POST_STYLES
from generator.hashtag_engine import get_hashtags

def generate_post(article, style, llm):
    prompt = POST_STYLES[style].format(
        title=article["title"],
        summary=article.get("summary", ""),
        source=article["source"]
    )

    content = llm(prompt)

    hashtags = " ".join(get_hashtags(article["category"]))

    return f"{content}\n\n{hashtags}"
