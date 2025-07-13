import os
import requests
from dotenv import load_dotenv
from utils import build_prompt

load_dotenv()

# Load API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Function to call OpenRouter API
def generate_persona(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        print("Error:", response.status_code, response.text)
        return None
