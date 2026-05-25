def estimate_value(research):

    score = research["score"]

    if score >= 8:
        return "High-value client ($300–$1000 potential)"
    elif score >= 5:
        return "Medium-value client ($100–$300 potential)"
    else:
        return "Low-value client ($0–$100 potential)"