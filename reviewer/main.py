from reviewer.gpt import analyze_code_with_gpt
from reviewer.github_api import post_comment
import os

def run_code_review():
    files_to_review = ["script.py"]

    for file_path in files_to_review:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()

        review = analyze_code_with_gpt(code, file_path)
        print(f"REVIEW:\n{review}")

        pr_number = os.getenv("PR_NUMBER")
        if pr_number:
            post_comment(pr_number, review)
