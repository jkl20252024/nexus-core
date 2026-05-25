def create_message(lead, research):
    return f"""
Hello {lead['name']},

We help businesses in Kampala grow using AI systems.

We noticed:
- Weak online presence
- Missing automation systems
- No structured digital tools

We can help you build:
- Website
- Booking system
- Marketing automation

Would you like a free demo?
"""

def create_followup_message(lead):

    return f"""
Hi {lead['business_name']},

Just following up on my previous message.

We can still help you:
- increase customers
- improve online visibility
- set up automation systems

Let me know if you'd like a quick demo.
"""