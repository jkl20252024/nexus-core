from datetime import datetime, timedelta
from backend.db import supabase

from backend.agents.heat_agent import compute_heat


def should_follow_up(research, lead):

    heat = compute_heat(research, lead)

    # 🔥 dynamic timing rules
    if heat < 40:
        return False  # ignore cold leads automatically

    if heat >= 80:
        return True  # follow up fast (high priority)

    if heat >= 50:
        # moderate delay logic handled elsewhere
        return True
    supabase.table("lead_metrics").insert({
    "lead_name": lead["name"],
    "score": research["score"],
    "heat": heat,
    "contacted": True
}).execute()

    return False




# 🔥 IMPORTANT WRAPPER (THIS FIXES YOUR AUTONOMY ERRORS)
def send_followups():
    return schedule_followups()

from backend.agents.followup_agent import schedule_followups
from backend.agents.closer_agent import generate_outreach


def send_followups():

    leads = schedule_followups()
    results = []

    for lead in leads:

        message = f"Hi {lead['lead_name']}, just following up on our previous message."

        supabase.table("outreach_queue").update({
            "message": message,
            "status": "followup_ready"
        }).eq("id", lead["id"]).execute()

        results.append({
            "lead": lead["lead_name"],
            "message": message
        })

    return results