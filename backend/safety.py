from backend.db import supabase

def is_autonomy_enabled():

    res = supabase.table("system_control") \
        .select("*") \
        .limit(1) \
        .execute()

    if not res.data:
        return False

    return res.data[0]["autonomy_enabled"]


def set_autonomy(state: bool):

    supabase.table("system_control") \
        .update({"autonomy_enabled": state}) \
        .eq("id", 1) \
        .execute()