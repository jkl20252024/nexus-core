from backend.db import supabase


def mark_replied(email):

    supabase.table("outreach_queue") \
        .update({
            "replied": True,
            "status": "replied"
        }) \
        .eq("email", email) \
        .execute()


def get_pipeline_stats():

    data = supabase.table("outreach_queue").select("*").execute().data

    total_value = sum([x.get("estimated_value", 0) for x in data if x["deal_closed"]])

    return {
        "total_leads": len(data),
        "revenue_pipeline": total_value,
        "closed_deals": len([x for x in data if x["deal_closed"]]),
        "active_deals": len([x for x in data if x["stage"] == "interested"])
    }

def mark_interested(id):
    supabase.table("outreach_queue") \
        .update({"stage": "interested"}) \
        .eq("id", id) \
        .execute()


def close_deal(id, value):
    supabase.table("outreach_queue") \
        .update({
            "stage": "closed_won",
            "deal_closed": True,
            "estimated_value": value
        }) \
        .eq("id", id) \
        .execute()
    
def estimate_value(score):

    if score >= 9:
        return 5000
    elif score >= 7:
        return 2000
    elif score >= 5:
        return 500
    else:
        return 100
    
    def update_lead_stage(lead_id, score):

        if score >= 9:
            stage = "hot"
        elif score >= 7:
            stage = "warm"
        elif score >= 5:
            stage = "cold"
        else:
            stage = "unqualified"

        supabase.table("outreach_queue")
    
def evaluate_lead(lead, research):

    score = research.get("score", 0)

    priority = "low"

    if score >= 8:
        priority = "high"
    elif score >= 6:
        priority = "medium"

    return {
        "score": score,
        "priority": priority,
        "stage": "approved"
    }       