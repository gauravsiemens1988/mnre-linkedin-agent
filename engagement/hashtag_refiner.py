def refined_hashtags(category):
    core = ["#EnergyTransition", "#CleanEnergy"]
    if category == "hydrogen":
        core += ["#GreenHydrogen", "#Electrolysers"]
    if category == "solar":
        core += ["#SolarEnergy"]
    if category == "policy":
        core += ["#EnergyPolicy", "#MNRE", "#SECI"]
    return " ".join(core)
