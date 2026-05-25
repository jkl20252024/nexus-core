from apscheduler.schedulers.background import BackgroundScheduler
from backend.orchestrator import run_pipeline
from backend.agents.followup_sender import send_followups
from backend.safety import is_autonomy_enabled
from backend.db import supabase
from datetime import datetime
from backend.agents.followup_agent import send_followups

def safe_run_pipeline():

    if not is_autonomy_enabled():
        return "AUTONOMY DISABLED"

    result = run_pipeline()

    supabase.table("system_control") \
        .update({"last_run": datetime.utcnow().isoformat()}) \
        .eq("id", 1) \
        .execute()

    return result


def safe_followups():

    if not is_autonomy_enabled():
        return "AUTONOMY DISABLED"

    return send_followups()


def start_autonomy():

    scheduler = BackgroundScheduler()

    scheduler.add_job(safe_run_pipeline, "interval", minutes=10)
    scheduler.add_job(safe_followups, "interval", minutes=15)

    scheduler.start()

    return "SAFE AUTONOMY ACTIVE"