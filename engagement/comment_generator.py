from engagement.comment_templates import COMMENT_TEMPLATES
from engagement.hashtag_refiner import refined_hashtags
import random

def generate_first_comment(category):
    template = random.choice(list(COMMENT_TEMPLATES.values()))

    comment = template.format(category=category)

    hashtags = refined_hashtags(category)

    return f"{comment}\n\n{hashtags}"
