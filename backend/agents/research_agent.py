def research_business(lead):

    score = 0
    issues = []

    name = lead.get("name", "").lower()

    # basic digital presence heuristics
    if not lead.get("website"):
        score += 3
        issues.append("No website detected")

    # brand strength checks (simple intelligence layer)
    weak_brands = ["cafe", "bistro", "kfc", "nando"]

    if any(word in name for word in weak_brands):
        score += 2
        issues.append("High competition market segment")

    # location boost
    if lead.get("location") == "Kampala":
        score += 2

    # default opportunity signal
    score += 3
    issues.append("No automation systems detected")

    return {
        "business_name": lead["name"],
        "issues": issues,
        "score": score
    }