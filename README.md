# 🧠 Reddit Persona Generator

This project scrapes a Reddit user's posts and comments, analyzes their writing, and generates a full user persona using a Large Language Model (LLM) via the [OpenRouter API](https://openrouter.ai/).

---

## 🚀 Features

- ✅ Takes Reddit profile URL as input  
- ✅ Scrapes posts and comments using `praw`  
- ✅ Generates a detailed persona with **citations** using an LLM  
- ✅ Saves output to a `.txt` file  
- ✅ Fully modular and easy to extend  
- ✅ Follows PEP-8 and includes inline comments  

---

## 📦 How to Run

### 1. Clone the Repo

```bash
git clone https://github.com/amantiwari-java/reddit-persona.git
cd reddit-persona
2. Create a .env File
Create a .env file in the root directory and add your API credentials:

env
Copy
Edit
OPENROUTER_API_KEY=your_openrouter_api_key
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_custom_user_agent
🔐 Don't worry! .env is ignored by .gitignore so your secrets stay safe.

3. Install Dependencies
Install the required Python packages using pip:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the Script
bash
Copy
Edit
python main.py
This will:

Scrape posts/comments from usernames listed in main.py

Generate user personas using OpenRouter's LLM API

Save each persona to a .txt file (e.g., kojied_persona.txt)

📂 Output Files
You will find output like:

kojied_persona.txt

Hungry-Move-6603_persona.txt

Each file includes:

Name, Age, Gender, Occupation

Interests & Hobbies

Personality Traits

Citations from actual posts/comments

🧪 Sample Output
vbnet
Copy
Edit
**User Persona:**

Name: Alex (assumed based on username "overpaidengineer")  
Estimated Age: Early 30s  
Occupation: iOS Developer  
...  
Citations:
- [POST] Creating an AR shopping assistant in VisionOS  
- [COMMENT] “Consumerism makes us numb...”  
🛠 Tech Stack
Python

praw (Reddit API)

requests

python-dotenv

OpenRouter API for LLM calls

📝 Notes
If you get a 408 error from OpenRouter, it's a timeout — retry after a short pause.

Reddit rate limits excessive requests — avoid too many usernames in one run.

Code follows PEP-8 and includes inline comments & docstrings for clarity.

📧 Contact
If you have questions, contact:
📩 amantiwari84044@gmail.com

✅ Made with ❤️ for BeyondChats AI/LLM Internship Assignment