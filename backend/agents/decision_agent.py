def should_contact(lead, research):

    score = research.get("score", 0)

    has_website = lead.get("website") is not None

    # decision rules
    if score >= 8:
        return True

    if score >= 6 and not has_website:
        return True

    return False