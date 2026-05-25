from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.orchestrator import run_pipeline, safe_run_pipeline
from backend.agents.pesapal_agent import get_token
from backend.agents.pesapal_agent import create_payment_link
from backend.agents.pesapal_agent import register_ipn
from backend.agents.pesapal_agent import check_payment_status
from backend.agents.pesapal_agent import check_payment_status
from backend.agents.client_activation_agent import activate_client
from backend.db import supabase
from fastapi.middleware.cors import CORSMiddleware

from backend.agents.email_agent import send_email
from backend.orchestrator import (
    run_pipeline,
    safe_run_pipeline
)

from backend.agents.reply_agent import analyze_reply

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"status": "AI Agency System Running"}


@app.get("/run")
def run():

    result = safe_run_pipeline()

    return {
        "result": result
    }


@app.get("/dashboard")
def dashboard():

    data = safe_run_pipeline()

    total_revenue = 0

    if isinstance(data, list):
        total_revenue = sum(
            item.get("revenue", 0)
            for item in data
        )

    return {
        "leads": data,
        "pipeline_size": len(data) if isinstance(data, list) else 0,
        "total_estimated_revenue": total_revenue
    }


@app.get("/reply-test")
def reply_test(message: str):

    result = analyze_reply(message)

    return result

@app.get("/send-test")
def send_test():

    result = send_email(
        "YOUR_REAL_EMAIL@gmail.com",
        "AI Agency Test",
        "Your AI agency system is now sending real emails."
    )

    return result

@app.get("/pesapal-test")
def pesapal_test():

    return get_token()

@app.get("/pay")
def pay():

    return create_payment_link(
        amount=50000,
        email="client@test.com",
        name="Test"
    )

@app.get("/payment-callback")
def payment_callback():

    return {
        "status": "callback received"
    }
@app.get("/register-ipn")
def reg_ipn():

    return register_ipn()

@app.get("/payment-status/{tracking_id}")
def payment_status(tracking_id: str):

    result = check_payment_status(tracking_id)

    status = result.get("payment_status_description", "").upper()

    # AUTO CLIENT ACTIVATION
    if status == "COMPLETED":

        payment_data = {
            "name": "Paid Client",
            "email": "paidclient@test.com",
            "amount": result.get("amount"),
            "tracking_id": tracking_id
        }

        activate_client(payment_data)

        print("🔥 CLIENT ACTIVATED")

    return result
@app.get("/dashboard-stats")
def dashboard_stats():

    payments = supabase.table("payments").select("*").execute().data

    businesses = supabase.table("businesses").select("*").execute().data

    outreach = supabase.table("outreach_queue").select("*").execute().data

    total_revenue = sum(
        float(p.get("amount", 0))
        for p in payments
    )

    return {
        "total_clients": len(payments),

        "total_revenue": total_revenue,

        "total_leads": len(businesses),

        "total_outreach": len(outreach),

        "payments": payments,

        "businesses": businesses,

        "outreach": outreach
    }
