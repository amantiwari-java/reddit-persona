from reddit_scraper import get_user_data
from utils import build_prompt
from persona_generator import generate_persona

if __name__ == "__main__":
    username = "kojied"  # or any Reddit username
    posts, comments = get_user_data(username, limit=15)

    prompt = build_prompt(posts, comments)

    persona = generate_persona(prompt)

    if persona:
        with open(f"{username}_persona.txt", "w", encoding="utf-8") as f:
            f.write(persona)
        print(f"✅ Persona saved to {username}_persona.txt")
    else:
        print("❌ Failed to generate persona.")
