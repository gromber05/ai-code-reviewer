from groq import analyze_code_with_groq
from github_api import post_comment
import os

def get_python_files(repo_path):
    python_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files

def clean_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_code_review():
    clean_console()
    repo_path = input("Enter the path to the repository (default: current directory): ").strip()
    if not repo_path:
        repo_path = "." 

    files_to_review = get_python_files(repo_path)

    for file_path in files_to_review:
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()

        review = analyze_code_with_groq(code, file_path)
        output_file = f"{file_path}_review.md"
        with open(output_file, 'w', encoding='utf-8') as md_file:
            md_file.write(f"# Code Review for {file_path}\n\n")
            md_file.write(review)
        print(f"Review for {file_path} has been saved to {output_file}")

        pr_number = os.getenv("PR_NUMBER")
        if pr_number:
            post_comment(pr_number, review)

if __name__ == "__main__":
    run_code_review()