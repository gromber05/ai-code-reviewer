import requests
import os
import subprocess
from dotenv import load_dotenv
from dotenv import get_key

load_dotenv()

def get_local_repo_url():
    """
    Obtiene la URL del repositorio remoto configurado en el repositorio local.
    Si no hay un repositorio configurado, devuelve None.
    """
    try:
        result = subprocess.run(
            ["git", "config", "--get", "remote.origin.url"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        repo_url = result.stdout.strip()
        if repo_url.endswith(".git"):
            repo_url = repo_url[:-4]  
        return repo_url
    except subprocess.CalledProcessError:
        print("No Git repository found or no remote URL configured.")
        return None

def get_next_pr_number():
    """
    Obtiene el siguiente número de Pull Request abierto en el repositorio.
    """
    repo_url = get_local_repo_url()
    if not repo_url:
        print("No repository URL found. Skipping PR retrieval.")
        return None

    repo = repo_url.split("github.com/")[-1]
    if not repo:
        print("Invalid repository URL format.")
        return None

    github_token = os.getenv("GITHUB_TOKEN")
    if not github_token:
        print("GITHUB_TOKEN is not set in the environment variables.")
        return None

    api_url = f"https://api.github.com/repos/{repo}/pulls"
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(api_url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch PRs: {response.status_code} - {response.content}")
        return None

    prs = response.json()
    if not prs:
        print("No open Pull Requests found.")
        return None

    return prs[0]["number"]

def post_comment(comment):
    """
    Publica un comentario en el Pull Request.
    """
    pr_number = get_next_pr_number()
    if not pr_number:
        print("No PR number available. Cannot post comment.")
        return

    repo_url = get_local_repo_url()
    if not repo_url:
        print("No repository URL found. Skipping comment posting.")
        return

    repo = repo_url.split("github.com/")[-1]
    api_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"

    github_token = get_key("project.env", "GITHUB_TOKEN")
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"body": comment}
    response = requests.post(api_url, headers=headers, json=data)

    if response.status_code != 201:
        print("Failed to post comment:", response.content)
    else:
        print(f"Comment posted successfully on PR #{pr_number}.")
