from backend.db import supabase
from backend.agents.followup_agent import schedule_followups
from backend.agents.email_agent import send_email
from backend.agents.outreach_agent import create_followup_message
from datetime import datetime

def send_followups():

    leads = schedule_followups()

    for lead in leads:

        msg = create_followup_message(lead)

        result = send_email(
            to_email=lead.get("email", "test@example.com"),
            subject="Quick follow-up",
            message=msg
        )

        supabase.table("outreach_queue") \
            .update({
                "last_sent_at": datetime.utcnow().isoformat(),
                "follow_up_count": lead.get("follow_up_count", 0) + 1,
                "status": "followed_up"
            }) \
            .eq("id", lead["id"]) \
            .execute()

    return {"followups_sent": len(leads)}