from backend.agents.lead_agent import find_leads
from backend.agents.research_agent import research_business
from backend.agents.finance_agent import estimate_value
from backend.agents.outreach_agent import create_message
from backend.db import supabase
from backend.agents.crm_agent import get_pipeline_stats
from backend.agents.revenue_agent import estimate_revenue
from backend.agents.closer_agent import generate_outreach
from backend.agents.heat_agent import compute_heat
from backend.agents.lead_agent import find_leads
from backend.agents.research_agent import research_business
from backend.agents.decision_agent import should_contact
from backend.agents.crm_agent import evaluate_lead
from backend.agents.revenue_agent import estimate_revenue
from backend.agents.closer_agent import generate_outreach
from backend.agents.money_agent import calculate_expected_value
from backend.agents.email_agent import send_email

def run_pipeline():

    leads = find_leads()

    results = []
    total_score = 0  # ✅ MUST be here

    for lead in leads:

        research = research_business(lead)
        value = estimate_value(research)
        message = create_message(lead, research)

        total_score += research["score"]

        supabase.table("businesses").insert({
            "name": lead["name"],
            "type": lead["type"],
            "location": lead["location"],
            "website": lead["website"],
            "score": research["score"]
        }).execute()

        supabase.table("outreach_queue").insert({
            "business_name": lead["name"],
            "message": message,
            "status": "queued",
            "sent": False
        }).execute()

        supabase.table("businesses").insert({
            "name": lead["name"],
            "type": lead["type"],
            "location": lead["location"]
        }).execute()

        results.append({
            "lead": lead,
            "research": research,
            "value": value,
            "message": message
        })

    avg_score = total_score / len(leads) if leads else 0  # ✅ safe

    supabase.table("runs").insert({
        "total_leads": len(leads),
        "avg_score": avg_score,
        "summary": f"Processed {len(leads)} leads"
    }).execute()
    money = calculate_expected_value(lead, research)


def get_pipeline_stats():

    data = supabase.table("outreach_queue").select("*").execute().data

    total_revenue = sum([
        x.get("estimated_value", 0)
        for x in data
    ])

    high_value = len([
        x for x in data
        if x.get("estimated_value", 0) >= 2000
    ])

    return {
        "pipeline_value": total_revenue,
        "high_value_leads": high_value,
        "total_leads": len(data)
    }

from backend.agents.lead_agent import find_leads
from backend.agents.research_agent import research_business
from backend.agents.crm_agent import evaluate_lead

from backend.agents.decision_agent import should_contact



def run_pipeline():

    leads = find_leads()
    results = []

    for lead in leads:

        research = research_business(lead)

        if not should_contact(lead, research):
            continue

        crm = evaluate_lead(lead, research)

        revenue = estimate_revenue(
            research.get("score", 0),
            lead.get("website") is None
        )

        outreach = generate_outreach(lead, research, crm)

        email_result = send_email(
    "client@email.com",
    "AI Growth Opportunity",
    outreach["message"]
)

        money = calculate_expected_value(lead, research)

        results.append({
    
            "lead": lead,
            "score": research.get("score", 0),
            "revenue": revenue,
            "money": money,
            "stage": crm.get("priority", "unknown"),
            "message": outreach.get("message", "")
     })

    return results
def safe_run_pipeline():

    try:
        return run_pipeline()
    except Exception as e:
        return {"error": str(e)}
    

    
    def safe_run_pipeline():

        try:
            return run_pipeline()

        except Exception as e:
            return {
                "error": str(e)
            }