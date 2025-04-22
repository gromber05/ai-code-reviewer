# 🤖 AI Code Reviewer for Code Projects

An automated code review tool powered by GPT (OpenAI). This GitHub-integrated bot analyzes Python code on Pull Requests and provides AI-generated feedback, suggestions, and potential improvements in code quality and best practices.

---

## 🚀 Motivation

Code reviews are critical for maintaining code quality but often take up a lot of developer time. This project helps automate that process by using a Large Language Model (LLM) to assist in reviewing Python code. It's particularly useful for open source projects, small teams, or educational repositories.

---

## ⚙️ Features

- Automatically reviews Python code in Pull Requests.
- Provides feedback on:
  - Code quality and readability.
  - Bad practices and potential bugs.
  - Suggestions for improvements.
- Posts comments directly on GitHub PRs.
- Extensible with linters like `pylint` or `flake8`.

---

## 🛠️ Tech Stack

- Python 3.10+
- groq API
- GitHub Actions
- GitHub REST API
- `requests`, `groq`

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```