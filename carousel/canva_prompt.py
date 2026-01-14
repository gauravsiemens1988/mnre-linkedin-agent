def canva_prompt(slide, category):
    return f"""
Create a LinkedIn carousel slide.

Theme: Clean energy, {category}
Style: Minimal, professional, corporate
Colors: Green, white, dark grey
Font: Modern sans-serif
Layout: Centered headline, subtle icons

Slide text:
{slide['text']}

No stock photos. Use abstract energy graphics.
"""
