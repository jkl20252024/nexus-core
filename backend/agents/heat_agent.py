def compute_heat(research, lead):

    score = research.get("score", 0)

    has_website = lead.get("website") is not None

    heat = 0

    # base intelligence
    heat += score * 10

    # weak online presence = higher urgency
    if not has_website:
        heat += 20

    # high-value businesses respond faster (assumption model)
    if score >= 8:
        heat += 30

    return min(100, heat)