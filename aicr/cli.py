import typer
import os
from .config import load_config
from .git import get_last_commit_diff
from .llm import initialize_gemini, get_code_review
from .renderer import show_error, show_review

app = typer.Typer(help="AI Code Review CLI with Gemini")

def get_system_prompt() -> str:
    prompt_path = os.path.join(os.path.dirname(__file__), "..", "prompts", "system.md")
    if not os.path.exists(prompt_path):
        return "You are an expert AI code reviewer. Please review the provided git diff."
    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read().strip()

@app.command()
def review():
    config = load_config()
    
    if not config.api_key:
        show_error("GEMINI_API_KEY environment variable is missing. Get one from https://aistudio.google.com/apikey")
        raise typer.Exit(code=1)

    diff = get_last_commit_diff()
    if not diff:
        show_error("Could not extract git diff. Verify you are inside a Git repository with correct history.")
        raise typer.Exit(code=1)

    system_prompt = get_system_prompt()
    initialize_gemini(config)
    
    try:
        review_text = get_code_review(diff, config, system_prompt)
        show_review(review_text)
    except Exception as e:
        show_error(f"Failed to communicate with Gemini API: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
