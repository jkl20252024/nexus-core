from backend.db import supabase

def log_event(event_type, data):

    supabase.table("logs").insert({
        "event_type": event_type,
        "data": data
    }).execute()