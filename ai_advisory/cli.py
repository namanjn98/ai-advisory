import asyncio
from typing import Optional

import typer

from .config import MODELS, resolve_token
from .models import query_all_models
from .prompts import build_meta_prompt
from .display import console, show_spinner, display_response, display_evaluation, get_selection

app = typer.Typer(help="Query multiple LLMs and run consensus evaluation")


@app.command()
def ask(
    query: Optional[str] = typer.Argument(None, help="The question to ask all models"),
    token: Optional[str] = typer.Option(None, "--token", "-t", help="OpenRouter API token"),
):
    """Ask a question to multiple AI models and get consensus evaluation."""

    # Resolve token
    api_token = resolve_token(token)

    # Get query if not provided
    if not query:
        query = typer.prompt("Enter your question")

    console.print(f"\n[bold]Query:[/bold] {query}\n")

    # Level 1: Query all models
    console.print("[bold cyan]Level 1: Querying all models...[/bold cyan]\n")

    messages = [{"role": "user", "content": query}]

    with show_spinner("Querying 8 models concurrently..."):
        responses = asyncio.run(query_all_models(MODELS, messages, api_token))

    # Display all responses
    for i, response in enumerate(responses, 1):
        display_response(i, response)

    # Filter successful responses for selection
    successful_responses = [
        (i, r) for i, r in enumerate(responses, 1) if r["success"]
    ]

    if not successful_responses:
        console.print("\n[red]Error: No successful responses to evaluate.[/red]")
        raise typer.Exit(1)

    # Get user selection
    max_index = len(responses)
    selected_indices = get_selection(max_index)

    # Filter selected responses (only successful ones can be selected)
    selected_responses = [
        responses[i - 1] for i in selected_indices
        if responses[i - 1]["success"]
    ]

    if not selected_responses:
        console.print("\n[red]Error: No valid responses selected.[/red]")
        raise typer.Exit(1)

    console.print(f"\n[bold green]Selected {len(selected_responses)} responses for evaluation[/bold green]\n")

    # Level 2: Consensus evaluation
    console.print("[bold cyan]Level 2: Running consensus evaluation...[/bold cyan]\n")

    meta_prompt = build_meta_prompt(query, selected_responses)
    meta_messages = [{"role": "user", "content": meta_prompt}]

    with show_spinner("Evaluating with all 8 models..."):
        evaluations = asyncio.run(query_all_models(MODELS, meta_messages, api_token))

    # Display all evaluations
    for i, evaluation in enumerate(evaluations, 1):
        display_evaluation(i, evaluation)

    console.print("\n[bold green]✓ Consensus evaluation complete![/bold green]\n")


if __name__ == "__main__":
    app()
