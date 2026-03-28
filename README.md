# AI Code Review CLI (`aicr`)

[![Python version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/AI-Google%20Gemini-orange.svg)](https://aistudio.google.com/)

**AI Code Review** (`aicr`) is a powerful, terminal-based assistant that leverages Google's Gemini AI to automate your code review process. It helps you maintain high code quality, enforce naming conventions, catch potential bugs early, and keep your codebase clean.

![Demo](https://raw.githubusercontent.com/placeholder-demo.gif)

> 🚀 **Roadmap:** Currently, the `aicr review` command focuses on analyzing the **latest commit**. Upcoming updates will introduce full repository codebase analysis and architectural reviews, allowing the AI to detect contextual issues across your entire project.

## ✨ Features

- **Automated Last-Commit Review:** Instantly analyze your latest changes (`HEAD~1..HEAD`) before pushing.
- **AI-Powered Insights:** Get intelligent feedback on readability, performance, potential bugs, and naming conventions.
- **Clean CLI Output:** Beautiful, easy-to-read Markdown rendering directly in your terminal.
- **Language Agnostic:** Works with any programming language supported by Git.
- **Customizable:** Use `.aireview.yml` to ignore specific directories or switch AI models.

## 🛠 Installation

You can install `aicr` via `pipx` (recommended) or directly using `pip`.

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/ai-code-review.git
cd ai-code-review

# Install via pip
pip install -e .

# Or using pipx
pipx install -e .
```

## 🔑 Configuration

To interact with the Gemini API, you need a free API key:
1. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).
2. Export the key as an environment variable:

```bash
export GEMINI_API_KEY=your_api_key_here
```
*(Tip: Add this to your `.bashrc` or `.zshrc` to make it persistent).*

### Optional: `.aireview.yml`
You can customize the review process by placing a `.aireview.yml` file in your project's root:
```yaml
model: "gemini-2.5-flash"
ignore_paths:
  - "tests/"
  - "node_modules/"
  - "venv/"
```

## 🚀 Usage

Navigate to any Git repository where you've made at least one recent commit:

```bash
cd your-project-folder/
aicr review
```

The CLI will extract the diff of your latest commit, send it to Gemini, and print out a concise, actionable code review right in your terminal.

## 🚨 Troubleshooting

- **`aicr: command not found`:** Ensure your Python bin directory (e.g., `~/.local/bin`) is in your system `PATH`. Alternatively, run `python -m aicr.cli review`.
- **Missing API Key:** If you see an API key error, verify that you exported it correctly (`echo $GEMINI_API_KEY`).