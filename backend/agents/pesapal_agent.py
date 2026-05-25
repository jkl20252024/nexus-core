import requests
import os
import uuid

from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

CONSUMER_KEY = os.getenv("PESAPAL_CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("PESAPAL_CONSUMER_SECRET")

import os
from dotenv import load_dotenv

load_dotenv()

consumer_key = os.getenv("PESAPAL_CONSUMER_KEY")
consumer_secret = os.getenv("PESAPAL_CONSUMER_SECRET")


def get_token():

    url = "https://cybqa.pesapal.com/pesapalv3/api/Auth/RequestToken"

    payload = {
        "consumer_key": CONSUMER_KEY,
        "consumer_secret": CONSUMER_SECRET
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.json()
def register_ipn():

    token_data = get_token()

    token = token_data["token"]

    url = "https://cybqa.pesapal.com/pesapalv3/api/URLSetup/RegisterIPN"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "url": "http://127.0.0.1:8000/payment-callback",
        "ipn_notification_type": "GET"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    return response.json()


def create_payment_link(amount, email, name):

    token_data = get_token()

    token = token_data["token"]

    url = "https://cybqa.pesapal.com/pesapalv3/api/Transactions/SubmitOrderRequest"

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "id": str(uuid.uuid4()),
        "currency": "UGX",
        "amount": amount,
        "description": "Nexus Core AI Service",
        "callback_url": "http://127.0.0.1:8000/payment-callback",
        "notification_id": "2ef4b6cd-b8ee-494d-8caf-da58c1d2e8de",

        "billing_address": {
            "email_address": email,
            "phone_number": "0784871971",
            "country_code": "UG",
            "first_name": name,
            "last_name": "Client"
        }
    }

def check_payment_status(order_tracking_id):

    token_data = get_token()
    token = token_data["token"]

    url = f"https://cybqa.pesapal.com/pesapalv3/api/Transactions/GetTransactionStatus?orderTrackingId={order_tracking_id}"

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # normalize response (IMPORTANT FIX)
    status = data.get("payment_status_description")

    if status is None:
        data["payment_status_description"] = "PENDING"

    return data