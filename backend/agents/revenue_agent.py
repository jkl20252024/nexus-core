def estimate_revenue(score, has_website=False):

    base = 0

    if score >= 9:
        base = 5000
    elif score >= 8:
        base = 2500
    elif score >= 6:
        base = 1000
    elif score >= 4:
        base = 300
    else:
        base = 100

    # boost if weak online presence (bigger opportunity)
    if not has_website:
        base *= 1.3

    return round(base, 2)