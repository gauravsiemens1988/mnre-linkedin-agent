def adapt_tone(content, voice):
    if voice == "first_person":
        return content.replace("This signals", "I see this as signaling")
    if voice == "third_person":
        return content.replace("I believe", "The industry is seeing")
    return content
