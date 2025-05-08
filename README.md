# CodeWise Reviewer

CodeWise Reviewer is an AI-powered tool designed to automate code reviews for your local repositories. It leverages advanced language models to analyze code, detect potential issues, and provide constructive feedback, saving time and improving team collaboration.

---

## 🚀 Features

- **Automatic Code Reviews**: Analyze code for best practices, potential bugs, and style improvements.
- **Multi-language Support**: Generate reviews in English or Spanish.
- **File Filtering**: Specify file extensions to include in the review (e.g., `.py`, `.js`, `.html`).
- **Markdown Output**: Save reviews as Markdown files for easy sharing.
- **GitHub Integration**: Post comments directly on pull requests.
- **Large File Handling**: Automatically skips files larger than 10 MB.

---

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/codewise-reviewer.git
   cd codewise-reviewer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `key.env` file in the root directory.
   - Add the following keys:
     ```
     GROQ_API_KEY=your_groq_api_key
     GITHUB_TOKEN=your_github_token
     ```

4. Install [Doxygen](https://www.doxygen.nl/) if you want to generate documentation.

---

## 📖 Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Follow the prompts:
   - Enter the repository path (default: current directory).
   - Specify file extensions to include (e.g., `.py,.js`).
   - Choose the language for the review (English or Spanish).

3. Reviews will be saved in the `output` directory as Markdown files.

---

## 🔧 Configuration

### Doxygen
The project includes a `Doxyfile` for generating documentation. To use it:
1. Install Doxygen.
2. Run:
   ```bash
   doxygen Doxyfile
   ```
3. Documentation will be generated in the `./doxygen` directory.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or feedback, feel free to reach out at [your-email@example.com](mailto:your-email@example.com).

---

## 🌟 Acknowledgments

- Powered by [Groq API](https://www.groq.com/).
- GitHub API integration for seamless pull request comments.
- Inspired by the need for efficient and automated code reviews.