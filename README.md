# AI Advisory

Query multiple LLMs via OpenRouter API and run consensus evaluation.

## Installation

```bash
cd ai-advisory
pip install -e .
```

## Setup

Set your OpenRouter API token:

```bash
export OPENROUTER_API_KEY=your_token_here
```

Or pass it via the `--token` flag.

## Usage

```bash
# Interactive mode
ai-advisory ask

# Direct query
ai-advisory ask "What is the best programming language for beginners?"
```

## How It Works

### Level 1: Query All Models
- Queries 8 different LLMs concurrently (ChatGPT, Gemini, Qwen, Llama, Kimi, Mistral, Claude, DeepSeek)
- Displays all responses as numbered panels
- User selects which responses to advance to evaluation

### Level 2: Consensus Evaluation
- Selected responses are bundled into a meta-prompt
- All 8 models evaluate the responses, providing:
  - Ratings (1-10) with justification
  - Agreement/disagreement analysis
  - Pros and cons
  - Synthesized consensus answer
- All evaluations displayed for comprehensive comparison

## Models

| Model | OpenRouter ID |
|-------|--------------|
| ChatGPT | `openai/gpt-4.1` |
| Gemini | `google/gemini-2.5-flash` |
| Qwen | `qwen/qwen3-235b-a22b` |
| Llama | `meta-llama/llama-4-maverick` |
| Kimi | `moonshotai/kimi-k2` |
| Mistral | `mistralai/mistral-medium` |
| Claude | `anthropic/claude-sonnet-4.5` |
| DeepSeek | `deepseek/deepseek-r1` |
