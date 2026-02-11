# 🧠 AI Advisory

> Get consensus answers from 8 leading AI models simultaneously. Query multiple LLMs, see their responses side-by-side, then let them evaluate and synthesize the best answer.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 What is AI Advisory?

AI Advisory is a CLI tool that helps you get better, more reliable answers by:

1. **Querying 8 different AI models at once** (ChatGPT, Claude, Gemini, DeepSeek, and more)
2. **Displaying all responses side-by-side** so you can compare perspectives
3. **Running a consensus round** where all models evaluate the responses and synthesize the best answer

Perfect for:
- 🔬 Research questions requiring multiple perspectives
- 💡 Complex technical decisions
- 📝 Writing that benefits from diverse viewpoints
- 🎓 Learning by seeing how different models approach the same problem

## ✨ Features

- **8 Top AI Models**: ChatGPT, Claude, Gemini, Qwen, Llama, Kimi, Mistral, DeepSeek
- **Concurrent Queries**: All models queried simultaneously for speed
- **Beautiful Terminal UI**: Rich panels with color-coded responses
- **Smart Selection**: Choose which responses to advance to evaluation
- **Consensus Analysis**: Models rate each other and synthesize final answers
- **Error Resilient**: One model failing doesn't affect others

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- An [OpenRouter](https://openrouter.ai/) API key (free tier available)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-advisory.git
   cd ai-advisory
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the package:**
   ```bash
   pip install -e .
   ```

4. **Set your OpenRouter API key:**
   ```bash
   export OPENROUTER_API_KEY=your_key_here
   ```

   > 💡 Get your free API key at [openrouter.ai/keys](https://openrouter.ai/keys)

### Your First Query

```bash
ai-advisory ask "What is the best way to learn Python?"
```

That's it! Watch as 8 AI models analyze your question, then select the best responses for consensus evaluation.

## 📖 Usage Guide

### Basic Usage

**Interactive Mode** (prompts you for the question):
```bash
ai-advisory ask
```

**Direct Query**:
```bash
ai-advisory ask "Your question here"
```

**With Custom Token**:
```bash
ai-advisory ask "Your question" --token sk-or-v1-xxxxx
```

### Example Workflow

1. **Run a query:**
   ```bash
   ai-advisory ask "Should I use REST or GraphQL for my API?"
   ```

2. **View responses:**
   - Each model's response appears in a numbered, color-coded panel
   - Green = successful response
   - Red = error (with details)
   - Elapsed time shown for each

3. **Select responses:**
   ```
   Select responses to advance (comma-separated numbers 1-8, or 'all'): 1,3,5,7
   ```
   Or type `all` to include all successful responses

4. **Read consensus:**
   - All 8 models evaluate the selected responses
   - Each provides ratings, analysis, and a synthesized answer
   - Compare the consensus answers to get the best insights

## 🤖 Models Included

| Model | Provider | Strengths |
|-------|----------|-----------|
| **ChatGPT** | OpenAI | General knowledge, conversational |
| **Claude** | Anthropic | Long-form analysis, nuanced reasoning |
| **Gemini** | Google | Multimodal, fast responses |
| **DeepSeek** | DeepSeek | Advanced reasoning, math/code |
| **Qwen** | Alibaba | Multilingual, technical |
| **Llama** | Meta | Open-source, balanced |
| **Mistral** | Mistral AI | European perspective, efficient |
| **Kimi** | Moonshot | Long context, detailed |

## 🎨 How It Works

### Level 1: Parallel Query
```
Your Question → [8 AI Models Queried Simultaneously]
                      ↓
         8 Responses Displayed in Panels
                      ↓
              You Select Best Ones
```

### Level 2: Consensus Evaluation
```
Selected Responses → [All 8 Models Evaluate]
                           ↓
        Each Model Provides:
        • Ratings (1-10) with justification
        • Agreement/disagreement analysis
        • Pros & cons of each response
        • Synthesized consensus answer
                           ↓
          8 Evaluation Panels Displayed
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
export OPENROUTER_API_KEY=sk-or-v1-xxxxx

# Optional: Add to your shell profile (~/.bashrc, ~/.zshrc)
echo 'export OPENROUTER_API_KEY=sk-or-v1-xxxxx' >> ~/.bashrc
```

### API Costs

OpenRouter pricing varies by model. Typical query costs:
- Level 1 (8 models): ~$0.01-0.05 per query
- Level 2 (8 evaluations): ~$0.02-0.10 per query

> 💡 OpenRouter offers free credits to new users. Check current pricing at [openrouter.ai/models](https://openrouter.ai/models)

## 📚 Use Cases

### Research & Analysis
```bash
ai-advisory ask "What are the implications of quantum computing on cryptography?"
```
Get diverse expert perspectives on complex topics.

### Technical Decisions
```bash
ai-advisory ask "Should I use PostgreSQL or MongoDB for a social media app?"
```
Compare architectural recommendations from multiple AI viewpoints.

### Creative Writing
```bash
ai-advisory ask "Write an opening paragraph for a sci-fi novel about AI consciousness"
```
See different creative approaches, then get a synthesized best version.

### Learning & Education
```bash
ai-advisory ask "Explain how blockchain works to a 12-year-old"
```
Compare teaching styles and get the clearest explanation.

## 🛠️ Development

### Project Structure
```
ai-advisory/
├── ai_advisory/
│   ├── cli.py          # Main CLI app (Typer)
│   ├── models.py       # Async API calls (httpx)
│   ├── prompts.py      # Meta-prompt templates
│   ├── display.py      # Rich terminal UI
│   └── config.py       # Model registry & settings
├── pyproject.toml      # Package configuration
└── README.md           # This file
```

### Running Tests
```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests (coming soon)
pytest
```

### Contributing

Contributions welcome! Ideas for improvements:
- Add more models
- Streaming responses
- Save/export results
- Custom model selection
- Response caching

## 🐛 Troubleshooting

**"No API token provided" error:**
```bash
export OPENROUTER_API_KEY=your_key_here
```

**"Command not found: ai-advisory":**
```bash
# Make sure you're in the virtual environment
source venv/bin/activate
pip install -e .
```

**Models timing out:**
- Some models may be slower. Successful responses will still display.
- Timeout is set to 60 seconds per model.

**Import errors:**
```bash
# Reinstall dependencies
pip install --upgrade -e .
```

## 📄 License

MIT License - feel free to use in your projects!

## 🙏 Acknowledgments

- Built with [Typer](https://typer.tiangolo.com/) for CLI
- [Rich](https://rich.readthedocs.io/) for beautiful terminal output
- [httpx](https://www.python-httpx.org/) for async HTTP
- [OpenRouter](https://openrouter.ai/) for unified LLM access

## 📞 Support

- 🐛 [Report issues](https://github.com/yourusername/ai-advisory/issues)
- 💡 [Request features](https://github.com/yourusername/ai-advisory/issues/new)
- ⭐ Star the repo if you find it useful!

---

**Made with ❤️ for better AI-assisted decision making**
