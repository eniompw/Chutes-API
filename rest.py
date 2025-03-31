import requests
import os

API_TOKEN = os.getenv("CHUTES_API_TOKEN")
API_URL = "https://llm.chutes.ai/v1/chat/completions"

if not API_TOKEN:
    print("Error: CHUTES_API_TOKEN environment variable not set.")
else:
    payload = {
        "model": "deepseek-ai/DeepSeek-V3-Base",
        "messages": [{"role": "user", "content": "What is the capital of France?"}],
        "max_tokens": 32
    }
    headers = {"Authorization": f"Bearer {API_TOKEN}"}

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        response.raise_for_status() # Check for HTTP 4xx/5xx errors
        print(response.json()["choices"][0]["message"]["content"])
    except Exception as e: # Catches request errors, JSON errors, key errors etc.
        print(f"An error occurred: {e}")
