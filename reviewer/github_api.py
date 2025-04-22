import requests
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY")
API_URL = f"https://api.github.com/repos/{REPO}"

def post_comment(pr_number, comment):
    url = f"{API_URL}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": comment}
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 201:
        print("Failed to post comment:", response.content)
    else:
        print("Comment posted successfully.")
