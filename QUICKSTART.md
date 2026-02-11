# ⚡ Quick Start Guide

Get up and running with AI Advisory in 5 minutes.

## 📦 Installation

### Option 1: Homebrew (macOS/Linux) - Recommended

```bash
brew tap yourusername/ai-advisory
brew install ai-advisory
```

### Option 2: pip (All platforms)

```bash
pip install ai-advisory
```

### Option 3: From Source

```bash
git clone https://github.com/yourusername/ai-advisory.git
cd ai-advisory
pip install -e .
```

## 🔑 Get Your API Key

1. Go to [openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up for a free account
3. Create an API key
4. Copy the key (starts with `sk-or-v1-`)

## ⚙️ Configure

Add your API key to your environment:

**macOS/Linux (Bash/Zsh):**
```bash
echo 'export OPENROUTER_API_KEY=sk-or-v1-your-key-here' >> ~/.bashrc
source ~/.bashrc
```

**macOS (Zsh - default on modern macOS):**
```bash
echo 'export OPENROUTER_API_KEY=sk-or-v1-your-key-here' >> ~/.zshrc
source ~/.zshrc
```

**Windows (PowerShell):**
```powershell
[System.Environment]::SetEnvironmentVariable('OPENROUTER_API_KEY', 'sk-or-v1-your-key-here', 'User')
```

**Temporary (current session only):**
```bash
export OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

## 🚀 Run Your First Query

```bash
ai-advisory ask "What is the best programming language for beginners?"
```

You'll see:
1. ⏳ Spinner while querying 8 AI models
2. 📊 8 response panels (green = success, red = error)
3. ❓ Prompt to select responses for evaluation
4. 🔮 8 consensus evaluations with synthesized answers

## 📋 Common Commands

**Interactive mode:**
```bash
ai-advisory ask
```

**Direct query:**
```bash
ai-advisory ask "Your question here"
```

**Custom token:**
```bash
ai-advisory ask "Your question" --token sk-or-v1-xxxxx
```

**Get help:**
```bash
ai-advisory --help
```

## 💡 Example Queries

**Technical Decision:**
```bash
ai-advisory ask "Should I use PostgreSQL or MongoDB for my app?"
```

**Learning:**
```bash
ai-advisory ask "Explain async/await in JavaScript with examples"
```

**Creative:**
```bash
ai-advisory ask "Write a tagline for a productivity app for developers"
```

**Research:**
```bash
ai-advisory ask "What are the security implications of using JWT tokens?"
```

## 🎯 Workflow Tips

1. **Read all Level 1 responses** - Each model has unique insights
2. **Select diverse perspectives** - Don't just pick similar answers
3. **Read consensus carefully** - The synthesized answers often combine the best of all responses
4. **Iterate** - Use answers to ask more specific follow-up questions

## 🐛 Troubleshooting

**Command not found:**
```bash
# Make sure installation completed successfully
which ai-advisory

# Reinstall if needed
pip install --force-reinstall ai-advisory
```

**No API token:**
```bash
# Verify token is set
echo $OPENROUTER_API_KEY

# If empty, set it again
export OPENROUTER_API_KEY=your-key-here
```

**Models timing out:**
- Normal for some models during high load
- Successful responses will still display
- Try again if too many fail

## 📚 Next Steps

- Read [EXAMPLES.md](EXAMPLES.md) for real-world use cases
- Check [README.md](README.md) for full documentation
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## 💰 Costs

- Free OpenRouter credits for new users
- Typical query: $0.01-0.05 (Level 1)
- Evaluation: $0.02-0.10 (Level 2)
- Check current pricing: [openrouter.ai/models](https://openrouter.ai/models)

## ❤️ Enjoy!

You're all set! Start asking questions and get better answers through AI consensus.

**Star the repo** if you find it useful: ⭐
