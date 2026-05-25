def estimate_deal_value(lead, research):

    score = research.get("score", 0)

    business_type = lead.get("type", "").lower()

    base = 300

    # industry multipliers
    if "restaurant" in business_type:
        base += 200

    if "salon" in business_type:
        base += 150

    if "hotel" in business_type:
        base += 500

    # stronger leads = bigger deal
    estimated = base + (score * 100)

    return estimated
def estimate_close_probability(research):

    score = research.get("score", 0)

    if score >= 8:
        return 0.8

    if score >= 5:
        return 0.5

    return 0.2
def calculate_expected_value(lead, research):

    deal_value = estimate_deal_value(lead, research)

    probability = estimate_close_probability(research)

    expected_value = deal_value * probability

    return {
        "deal_value": deal_value,
        "close_probability": probability,
        "expected_value": expected_value
    }