from branding.profiles import BRAND_PROFILES
from branding.tone_adapter import adapt_tone

def apply_brand(content, brand_type):
    profile = BRAND_PROFILES[brand_type]

    branded = f"""{profile['intro']}

{content}

{profile['closing']}
— {profile['author']}
"""
    return adapt_tone(branded, profile["voice"])
