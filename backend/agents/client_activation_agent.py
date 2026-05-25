from backend.db import supabase


def activate_client(payment_data):

    data = {
        "client_name": payment_data.get("name"),
        "client_email": payment_data.get("email"),
        "amount": payment_data.get("amount"),
        "tracking_id": payment_data.get("tracking_id"),
        "status": "ACTIVE"
    }

    result = supabase.table("payments").insert(data).execute()

    return result.data