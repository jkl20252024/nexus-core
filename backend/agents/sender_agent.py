from backend.db import supabase
from backend.agents.email_agent import send_email

def send_next_email():

    row = supabase.table("outreach_queue") \
        .select("*") \
        .eq("sent", False) \
        .limit(1) \
        .execute()

    if not row.data:
        return "No messages"

    item = row.data[0]

    # REAL SEND
    result = send_email(
        to_email=item.get("email", "test@example.com"),
        subject="AI Growth Opportunity",
        message=item["message"]
    )

    supabase.table("outreach_queue") \
        .update({
            "sent": True,
            "status": "sent"
        }) \
        .eq("id", item["id"]) \
        .execute()

    return {"status": result}