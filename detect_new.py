import json
import os
print("🚀 LinkedIn Agent run started")

LATEST_FILE = "latest_news.json"
MEMORY_FILE = "memory.json"
NEW_ITEM_FILE = "new_item.json"

def detect_new_item():
    if not os.path.exists(LATEST_FILE):
        print("No latest news file found.")
        return

    with open(LATEST_FILE, "r", encoding="utf-8") as f:
        latest_news = json.load(f)

    if not latest_news:
        print("No news items found.")
        return

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = json.load(f)

    for item in latest_news:
        url = item.get("url")
        source = item.get("source", "UNKNOWN")

        if not url:
            continue

        if url not in memory:
            with open(NEW_ITEM_FILE, "w", encoding="utf-8") as f:
                json.dump(item, f, indent=2, ensure_ascii=False)

            memory[url] = {
                "source": source
            }

            with open(MEMORY_FILE, "w", encoding="utf-8") as f:
                json.dump(memory, f, indent=2, ensure_ascii=False)

            print(f"New {source} news detected.")
            return

    print("✅ Agent ran successfully. No new items found in this run.")


if __name__ == "__main__":
    detect_new_item()

