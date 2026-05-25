def generate_outreach(lead, research, crm):

    name = lead.get("name", "there")
    score = research.get("score", 0)

    if score >= 8:
        tone = "high-value"
        offer = "free priority AI growth audit"
    elif score >= 6:
        tone = "standard"
        offer = "free AI automation demo"
    else:
        tone = "light"
        offer = "quick business visibility check"

    message = f"""
Hello {name},

We help businesses like yours improve visibility and automate customer flow.

We noticed some opportunities in your current setup and would like to offer a {offer}.

Would you be open to a quick conversation this week?
"""

    return {
        "tone": tone,
        "message": message.strip(),
        "cta": "book_call"
    }