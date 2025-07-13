import os
import requests
from dotenv import load_dotenv
from utils import build_prompt

# Load environment variables
load_dotenv()

# Get your OpenRouter API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# Debug check
print("🔑 Loaded API Key:", OPENROUTER_API_KEY[:8] + "********")

# Function to call OpenRouter's chat completion API and generate a persona
def generate_persona(posts, comments):
    prompt = build_prompt(posts, comments)

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
    elif response.status_code == 401:
        print("❌ Unauthorized: Invalid OpenRouter API key. Check your .env file.")
        return None
    else:
        print(f"❌ Error {response.status_code}: {response.text}")
        return None


# Function to save the generated persona to a text file
def save_persona(persona_text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(persona_text)
