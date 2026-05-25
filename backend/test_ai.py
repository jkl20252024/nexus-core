from backend.ai_client import client

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Say hello from Nexus Core"
        }
    ]
)

print(response.choices[0].message.content)