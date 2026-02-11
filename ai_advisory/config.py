import os
import sys

MODELS = [
    {"name": "ChatGPT", "id": "openai/gpt-4.1"},
    {"name": "Gemini", "id": "google/gemini-2.5-flash"},
    {"name": "Qwen", "id": "qwen/qwen3-235b-a22b"},
    {"name": "Llama", "id": "meta-llama/llama-4-maverick"},
    {"name": "Kimi", "id": "moonshotai/kimi-k2"},
    {"name": "Mistral", "id": "mistralai/mistral-medium"},
    {"name": "Claude", "id": "anthropic/claude-sonnet-4.5"},
    {"name": "DeepSeek", "id": "deepseek/deepseek-r1"},
]

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1/chat/completions"


def resolve_token(token: str | None) -> str:
    """Resolve API token from flag or environment variable."""
    resolved = token or os.environ.get("OPENROUTER_API_KEY")
    if not resolved:
        print(
            "Error: No API token provided.\n"
            "Set OPENROUTER_API_KEY env var or pass --token flag.",
            file=sys.stderr,
        )
        sys.exit(1)
    return resolved
