def analyze_reply(text):

    text = text.lower()

    if "interested" in text:
        return {
            "intent": "hot",
            "stage": "qualified",
            "reply": "Great — we would love to show you a demo and discuss solutions for your business."
        }

    if "price" in text:
        return {
            "intent": "pricing",
            "stage": "negotiation",
            "reply": "Our pricing depends on the systems needed. We can discuss the best option for your business."
        }

    if "not interested" in text:
        return {
            "intent": "cold",
            "stage": "closed_lost",
            "reply": "Understood. Thank you for your time."
        }

    return {
        "intent": "neutral",
        "stage": "pending",
        "reply": "Thank you for your response."
    }