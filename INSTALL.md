# 📦 Installation Guide

Complete installation instructions for all platforms.

## Quick Install

### macOS (Homebrew) - Recommended ⭐

```bash
# Add the AI Advisory tap
brew tap namanjn98/ai-advisory

# Install using Homebrew
brew install ai-advisory

# Set your API key
export OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Run it
ai-advisory ask "Hello world"
```

### Linux (Homebrew)

```bash
# Install Homebrew first (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add the AI Advisory tap
brew tap namanjn98/ai-advisory

# Install ai-advisory
brew install ai-advisory
```

### Python pip (All Platforms)

```bash
pip install ai-advisory
```

### From Source

```bash
git clone https://github.com/yourusername/ai-advisory.git
cd ai-advisory
pip install -e .
```

---

## Detailed Installation Instructions

### Method 1: Homebrew (macOS/Linux)

**Prerequisites:**
- macOS 10.15+ or Linux
- Homebrew installed

**Steps:**

1. **Add the Homebrew tap:**
   ```bash
   brew tap namanjn98/ai-advisory
   ```

2. **Install the formula:**
   ```bash
   brew install ai-advisory
   ```

3. **Verify installation:**
   ```bash
   ai-advisory --help
   ```

4. **Set API key (permanent):**
   ```bash
   echo 'export OPENROUTER_API_KEY=sk-or-v1-your-key' >> ~/.zshrc
   source ~/.zshrc
   ```

**Advantages:**
- ✅ Automatic dependency management
- ✅ Easy updates with `brew upgrade`
- ✅ System-wide installation
- ✅ No Python version conflicts

**Update:**
```bash
brew update
brew upgrade ai-advisory
```

**Uninstall:**
```bash
brew uninstall ai-advisory
```

---

### Method 2: pip (Python Package Manager)

**Prerequisites:**
- Python 3.10 or higher
- pip installed

**Steps:**

1. **Install via pip:**
   ```bash
   pip install ai-advisory
   ```

2. **Verify installation:**
   ```bash
   ai-advisory --help
   ```

**For system-wide installation (may require sudo):**
```bash
sudo pip install ai-advisory
```

**For user installation (no sudo needed):**
```bash
pip install --user ai-advisory
```

**Update:**
```bash
pip install --upgrade ai-advisory
```

**Uninstall:**
```bash
pip uninstall ai-advisory
```

---

### Method 3: pipx (Isolated Environment) - Recommended for Python Users

**Prerequisites:**
- Python 3.10+
- pipx (`brew install pipx` or `pip install pipx`)

**Steps:**

1. **Install with pipx:**
   ```bash
   pipx install ai-advisory
   ```

2. **Verify:**
   ```bash
   ai-advisory --help
   ```

**Advantages:**
- ✅ Isolated environment (no dependency conflicts)
- ✅ Always available in PATH
- ✅ Clean uninstall

**Update:**
```bash
pipx upgrade ai-advisory
```

**Uninstall:**
```bash
pipx uninstall ai-advisory
```

---

### Method 4: From Source (Development)

**Prerequisites:**
- Python 3.10+
- git

**Steps:**

1. **Clone repository:**
   ```bash
   git clone https://github.com/yourusername/ai-advisory.git
   cd ai-advisory
   ```

2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install in editable mode:**
   ```bash
   pip install -e .
   ```

4. **Verify:**
   ```bash
   ai-advisory --help
   ```

**Advantages:**
- ✅ Latest development version
- ✅ Easy to modify and contribute
- ✅ Isolated environment

**Update:**
```bash
cd ai-advisory
git pull origin main
pip install -e . --upgrade
```

---

## Platform-Specific Instructions

### macOS

**Using Homebrew (Recommended):**
```bash
brew install ai-advisory
```

**Using pip:**
```bash
# System Python (not recommended)
pip3 install ai-advisory

# With virtual environment (recommended)
python3 -m venv ~/.venvs/ai-advisory
source ~/.venvs/ai-advisory/bin/activate
pip install ai-advisory
```

**Add to PATH (if using venv):**
```bash
echo 'export PATH="$HOME/.venvs/ai-advisory/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

---

### Linux (Ubuntu/Debian)

**Using Homebrew:**
```bash
# Install Homebrew
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
source ~/.bashrc

# Install ai-advisory
brew install ai-advisory
```

**Using apt and pip:**
```bash
# Install Python 3.10+
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Install ai-advisory
pip3 install ai-advisory
```

---

### Windows

**Using pip:**
```powershell
# Install Python from python.org first

# Install ai-advisory
pip install ai-advisory
```

**Using Windows Subsystem for Linux (WSL):**
```bash
# Follow Linux instructions above
```

**Add to PATH (if needed):**
```powershell
# Run as Administrator
[System.Environment]::SetEnvironmentVariable(
    "Path",
    $env:Path + ";C:\Users\YourUsername\AppData\Local\Programs\Python\Python311\Scripts",
    "Machine"
)
```

---

## Post-Installation Setup

### 1. Get OpenRouter API Key

1. Visit [openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up for free
3. Create an API key
4. Copy the key (format: `sk-or-v1-...`)

### 2. Configure API Key

**Permanent (Recommended):**

**macOS/Linux (Bash):**
```bash
echo 'export OPENROUTER_API_KEY=sk-or-v1-your-key' >> ~/.bashrc
source ~/.bashrc
```

**macOS (Zsh - default):**
```bash
echo 'export OPENROUTER_API_KEY=sk-or-v1-your-key' >> ~/.zshrc
source ~/.zshrc
```

**Linux (Fish):**
```bash
echo 'set -x OPENROUTER_API_KEY sk-or-v1-your-key' >> ~/.config/fish/config.fish
source ~/.config/fish/config.fish
```

**Windows (PowerShell):**
```powershell
[System.Environment]::SetEnvironmentVariable(
    'OPENROUTER_API_KEY',
    'sk-or-v1-your-key',
    'User'
)
```

**Temporary (Current Session Only):**
```bash
export OPENROUTER_API_KEY=sk-or-v1-your-key
```

### 3. Verify Setup

```bash
# Check installation
ai-advisory --help

# Check API key
echo $OPENROUTER_API_KEY

# Test query
ai-advisory ask "Hello, how are you?"
```

---

## Troubleshooting

### Command not found

**Issue:** `ai-advisory: command not found`

**Solutions:**

1. **Check if installed:**
   ```bash
   pip show ai-advisory  # or: brew list ai-advisory
   ```

2. **Find installation path:**
   ```bash
   which ai-advisory
   ```

3. **Add to PATH:**
   ```bash
   # Find where pip installed it
   pip show ai-advisory | grep Location

   # Add to PATH
   export PATH="$PATH:/path/to/bin"
   ```

4. **Reinstall:**
   ```bash
   pip install --force-reinstall ai-advisory
   ```

---

### Python version issues

**Issue:** `Requires Python 3.10+`

**Solutions:**

1. **Check Python version:**
   ```bash
   python3 --version
   ```

2. **Install Python 3.10+:**
   ```bash
   # macOS
   brew install python@3.11

   # Ubuntu
   sudo apt install python3.11
   ```

3. **Use specific Python version:**
   ```bash
   python3.11 -m pip install ai-advisory
   ```

---

### API key not found

**Issue:** `No API token provided`

**Solutions:**

1. **Verify environment variable:**
   ```bash
   echo $OPENROUTER_API_KEY
   ```

2. **Set it permanently:**
   ```bash
   echo 'export OPENROUTER_API_KEY=your-key' >> ~/.zshrc
   source ~/.zshrc
   ```

3. **Pass via flag:**
   ```bash
   ai-advisory ask "test" --token sk-or-v1-your-key
   ```

---

### Permission denied

**Issue:** Permission errors during installation

**Solutions:**

1. **Use user install:**
   ```bash
   pip install --user ai-advisory
   ```

2. **Use virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install ai-advisory
   ```

3. **Use pipx:**
   ```bash
   pipx install ai-advisory
   ```

---

## Updating

### Homebrew
```bash
brew update
brew upgrade ai-advisory
```

### pip
```bash
pip install --upgrade ai-advisory
```

### pipx
```bash
pipx upgrade ai-advisory
```

### From Source
```bash
cd ai-advisory
git pull
pip install -e . --upgrade
```

---

## Uninstalling

### Homebrew
```bash
brew uninstall ai-advisory
```

### pip
```bash
pip uninstall ai-advisory
```

### pipx
```bash
pipx uninstall ai-advisory
```

### From Source
```bash
# Deactivate venv if active
deactivate

# Remove directory
rm -rf ai-advisory
```

---

## Next Steps

✅ Installation complete!

1. **Read the [Quick Start](QUICKSTART.md)** to learn basic usage
2. **Check [Examples](EXAMPLES.md)** for real-world use cases
3. **See [README](README.md)** for full documentation

---

## Need Help?

- 📖 [Documentation](README.md)
- 🐛 [Report Issues](https://github.com/yourusername/ai-advisory/issues)
- 💬 [Discussions](https://github.com/yourusername/ai-advisory/discussions)
