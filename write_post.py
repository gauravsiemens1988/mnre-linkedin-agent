import os
import json
import google.generativeai as genai

NEW_ITEM_FILE = "new_item.json"
OUTPUT_FILE = "output/linkedin_post.md"

def write_linkedin_post():
    if not os.path.exists(NEW_ITEM_FILE):
        print("No new MNRE item to process.")
        return

    with open(NEW_ITEM_FILE, "r", encoding="utf-8") as f:
        item = json.load(f)

    title = item.get("title", "")
    url = item.get("url", "")

    prompt = f"""
You are a senior professional in India’s renewable energy sector.

Source: Official MNRE announcement

Title: {title}
Link: {url}

Write a LinkedIn post:
- 90 to 130 words
- Professional, insightful, leadership tone
- Explain policy or industry significance
- Subtly connect to green hydrogen / renewable energy ecosystem
- No emojis
- End with 3 to 5 relevant hashtags
"""

    genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
    model = genai.GenerativeModel("gemini-1.5-flash")

    response = model.generate_content(prompt)
    post_text = response.text.strip()

    os.makedirs("output", exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(post_text)

    print("LinkedIn post generated successfully.")

if __name__ == "__main__":
    write_linkedin_post()
