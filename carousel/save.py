import json

def save_carousel(draft_id, slides, prompts):
    data = {
        "draft_id": draft_id,
        "slides": slides,
        "canva_prompts": prompts
    }

    with open(f"carousel/{draft_id}_carousel.json", "w") as f:
        json.dump(data, f, indent=2)
