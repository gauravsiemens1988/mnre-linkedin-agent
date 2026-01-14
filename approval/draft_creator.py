from generator.post_generator import generate_post

STYLES = ["insight", "policy_explainer", "leadership"]

def create_drafts(article, llm):
    drafts = []

    for style in STYLES:
        post = generate_post(article, style, llm)
        drafts.append({
            "title": article["title"],
            "category": article["category"],
            "style": style,
            "content": post
        })

    return drafts
