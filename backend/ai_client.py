import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

print("Loaded key:", api_key[:15] if api_key else "NONE")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)