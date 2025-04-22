# 🤝 Contributing to AI Code Reviewer

Thanks for your interest in contributing to this project! We welcome contributions of all kinds.

---

## 🛠️ Ways to Contribute

- 💡 **Feature suggestions**: Got a cool idea? Open an issue!
- 🐛 **Bug fixes**: Found a bug? Help us squash it!
- ✨ **New features**: Add more capabilities to the reviewer.
- 📝 **Improve documentation**: Docs are as important as code.
- 🌍 **Translations**: Help localize this project in other languages.

---

## 📦 Project Setup

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/ai-code-reviewer.git
cd ai-code-reviewer
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file (optional for local testing):**

```
OPENAI_API_KEY=your_key
GITHUB_TOKEN=your_token
GITHUB_REPOSITORY=youruser/yourrepo
PR_NUMBER=123
```

---

## 💡 Development Guidelines

- Write clear and concise code.
- Follow PEP8 style guidelines.
- Document your code with docstrings.
- Add unit tests when applicable.
- Keep commits clean and descriptive.

---

## 🧪 Testing

You can run the reviewer locally before deploying:

```bash
python -m reviewer.main
```

---

## ✅ Pull Request Checklist

- [ ] Code is linted (`pylint`, `black`, etc.).
- [ ] Code is tested and passes.
- [ ] Docs are updated if needed.
- [ ] PR description explains the problem and solution.
- [ ] You linked the related issue (if applicable).

---

## 📌 Interesting Extensions

Here are a few ideas you could help implement:
- Inline comments on specific lines (via GitHub API).
- Support for multiple languages (JavaScript, TypeScript, etc.).
- Custom rules and prompt templates.
- Web dashboard to manage reviews.

---

## 🙌 Thank You!

You're awesome. Your contributions help this project grow. If you have any questions, feel free to open a discussion or email the maintainers.