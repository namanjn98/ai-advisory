from typing import List, Dict, Any

from rich.console import Console
from rich.panel import Panel
from rich.spinner import Spinner
from rich.live import Live

console = Console()


def show_spinner(text: str):
    """Show a spinner with text."""
    return Live(Spinner("dots", text=text), console=console, transient=True)


def display_response(index: int, response: Dict[str, Any]):
    """Display a single model response as a panel."""
    if response["success"]:
        title = f"[green]{index}. {response['name']} ({response['elapsed']:.1f}s)"
        content = response["content"]
        border_style = "green"
    else:
        title = f"[red]{index}. {response['name']} - ERROR ({response['elapsed']:.1f}s)"
        content = f"[red]{response['error']}"
        border_style = "red"

    panel = Panel(
        content,
        title=title,
        border_style=border_style,
        expand=False,
    )
    console.print(panel)


def display_evaluation(index: int, response: Dict[str, Any]):
    """Display a Level 2 evaluation response."""
    if response["success"]:
        title = f"[magenta]{index}. {response['name']} Evaluation ({response['elapsed']:.1f}s)"
        content = response["content"]
        border_style = "magenta"
    else:
        title = f"[red]{index}. {response['name']} - ERROR ({response['elapsed']:.1f}s)"
        content = f"[red]{response['error']}"
        border_style = "red"

    panel = Panel(
        content,
        title=title,
        border_style=border_style,
        expand=False,
    )
    console.print(panel)


def get_selection(max_num: int) -> List[int]:
    """Prompt user to select responses to advance."""
    while True:
        selection = console.input(
            f"\n[bold cyan]Select responses to advance (comma-separated numbers 1-{max_num}, or 'all'):[/bold cyan] "
        ).strip()

        if selection.lower() == "all":
            return list(range(1, max_num + 1))

        try:
            numbers = [int(n.strip()) for n in selection.split(",")]
            if all(1 <= n <= max_num for n in numbers):
                return sorted(set(numbers))  # Remove duplicates and sort
            else:
                console.print(f"[red]Error: All numbers must be between 1 and {max_num}[/red]")
        except ValueError:
            console.print("[red]Error: Invalid input. Use comma-separated numbers or 'all'[/red]")
