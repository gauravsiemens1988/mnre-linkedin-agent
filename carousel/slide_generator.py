def generate_slides(post_text, category):
    slides = []

    slides.append({
        "slide": 1,
        "type": "hook",
        "text": "India’s clean energy transition just took a decisive step."
    })

    slides.append({
        "slide": 2,
        "type": "context",
        "text": post_text.split("\n")[0]
    })

    slides.append({
        "slide": 3,
        "type": "key_points",
        "text": "• Policy clarity\n• Market visibility\n• Faster execution"
    })

    slides.append({
        "slide": 4,
        "type": "impact",
        "text": "What this means for developers, OEMs, and investors."
    })

    slides.append({
        "slide": 5,
        "type": "closing",
        "text": "This is how ecosystems scale — not just projects."
    })

    return slides
