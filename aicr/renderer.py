from rich.console import Console
from rich.markdown import Markdown

def show_error(message: str) -> None:
    console = Console()
    console.print(f"[bold red]Error:[/bold red] {message}")

def show_review(review_text: str) -> None:
    console = Console()
    markdown = Markdown(review_text)
    console.print(markdown)
