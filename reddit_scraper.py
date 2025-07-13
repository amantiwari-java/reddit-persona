import praw
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()
print("📦 Reddit Client ID:", os.getenv("REDDIT_CLIENT_ID"))


# Setup Reddit API
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

# 🧠 Function to get posts and comments
def get_user_data(username, limit=30):
    user = reddit.redditor(username)
    posts = []
    comments = []

    # Get posts
    for submission in user.submissions.new(limit=limit):
        post_text = f"[POST] {submission.title}\n{submission.selftext}".strip()
        posts.append(post_text)

    # Get comments
    for comment in user.comments.new(limit=limit):
        comment_text = f"[COMMENT] {comment.body}".strip()
        comments.append(comment_text)

    return posts, comments

# ✅ Run & print to check output
if __name__ == "__main__":
    posts, comments = get_user_data("kojied", limit=10)

    print("\n--- Posts ---")
    for p in posts:
        print(p, "\n")

    print("\n--- Comments ---")
    for c in comments:
        print(c, "\n")
