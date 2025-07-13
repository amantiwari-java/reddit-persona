from reddit_scraper import get_user_data
from persona_generator import generate_persona, save_persona
import re
import os
print("OPENROUTER_API_KEY from env:", repr(os.getenv("OPENROUTER_API_KEY")))

profile_urls = [
    "https://www.reddit.com/user/kojied/",
    "https://www.reddit.com/user/Hungry-Move-6603/"
]

def extract_username(url):
    match = re.search(r"reddit\.com/user/([^/]+)", url)
    return match.group(1) if match else None

for url in profile_urls:
    username = extract_username(url)
    if username:
        print(f"🔍 Generating persona for {username}...")
        posts, comments = get_user_data(username)
        persona = generate_persona(posts, comments)

        if persona is None:
            print(f"❌ Failed to generate persona for {username}. Skipping save.")
            continue  # Skip saving and move to next

        save_persona(persona, f"{username}_persona.txt")
        print(f"✅ Saved {username}_persona.txt\n")
    else:
        print(f"❌ Invalid Reddit URL: {url}")
