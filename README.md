# 🤖 CodeWise Reviewer

An automated code review tool powered by GPT (OpenAI). This GitHub-integrated bot analyzes code in Pull Requests and provides AI-generated feedback, suggestions, and potential improvements in code quality and best practices.

---

## 🚀 Motivation

Code reviews are critical for maintaining code quality but often take up a lot of developer time. **CodeWise Reviewer** helps automate that process by using a Large Language Model (LLM) to assist in reviewing code. It's particularly useful for open source projects, small teams, or educational repositories.

---

## ⚙️ Features

- Automatically reviews code in Pull Requests.
- Provides feedback on:
  - Code quality and readability.
  - Bad practices and potential bugs.
  - Suggestions for improvements.
- Posts comments directly on GitHub PRs.
- Extensible with linters like `pylint` or `flake8`.
- Supports multiple file types (e.g., `.py`, `.js`, `.html`).

---

## 🛠️ Tech Stack

- Python 3.10+
- groq API
- GitHub Actions
- GitHub REST API
- `requests`, `dotenv`

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/your-username/codewise-reviewer.git
cd codewise-reviewer
```
### 2. Install dependencies

```bash
pip install -r requirements.txt
```