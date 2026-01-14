HASHTAGS = {
    "hydrogen": [
        "#GreenHydrogen", "#HydrogenEconomy", "#Electrolysers"
    ],
    "green_ammonia": [
        "#GreenAmmonia", "#Decarbonization"
    ],
    "solar": [
        "#SolarEnergy", "#RenewableEnergy"
    ],
    "policy": [
        "#EnergyPolicy", "#MNRE", "#SECI"
    ],
    "events": [
        "#EnergySummit", "#CleanEnergy"
    ]
}

def get_hashtags(category):
    base = ["#EnergyTransition", "#Sustainability"]
    return base + HASHTAGS.get(category, [])
