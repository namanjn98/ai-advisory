# 🚀 GitHub Repository Setup Guide

Complete guide to setting up this repository on GitHub for public distribution.

## 📋 Prerequisites

- GitHub account
- Git installed locally
- Repository code ready (already done ✅)

## 🎯 Step-by-Step Setup

### 1. Create GitHub Repository

**Option A: Using GitHub CLI (Recommended)**

```bash
# Make sure you're in the project directory
cd /Users/namanjain/AIplays/ai-advisory

# Create public repository
gh repo create ai-advisory --public --source=. --remote=origin \
  --description="Query multiple LLMs concurrently and run AI consensus evaluation via OpenRouter API"

# Push code
git push -u origin main
```

**Option B: Using GitHub Web Interface**

1. Go to [github.com/new](https://github.com/new)
2. Fill in repository details:
   - **Name:** `ai-advisory`
   - **Description:** `Query multiple LLMs concurrently and run AI consensus evaluation via OpenRouter API`
   - **Visibility:** Public
   - **Initialize:** Don't add README, .gitignore, or license (we have them)
3. Click "Create repository"
4. Follow the instructions to push existing code:

```bash
git remote add origin https://github.com/YOURUSERNAME/ai-advisory.git
git branch -M main
git push -u origin main
```

---

### 2. Configure Repository Settings

Go to `Settings` on your GitHub repository:

#### General Settings

**Features:**
- ✅ Issues
- ✅ Discussions
- ✅ Projects
- ❌ Wiki (using README.md instead)

**Pull Requests:**
- ✅ Allow squash merging
- ✅ Allow merge commits
- ✅ Allow rebase merging
- ✅ Automatically delete head branches

#### Topics

Add repository topics (Settings → General → Topics):
```
ai, llm, openrouter, cli, python, consensus, chatgpt, claude, gemini,
multi-model, openai, anthropic, google, command-line-tool
```

---

### 3. Create Repository Sections

#### About Section

Click "⚙️" next to "About" on the main repository page:

- **Description:** `Query multiple LLMs concurrently and run AI consensus evaluation via OpenRouter API`
- **Website:** (Leave blank or add docs site later)
- **Topics:** (Already added in step 2)
- ✅ Use your repository description

---

### 4. Create Release (v0.1.0)

Releases are needed for Homebrew installation and pip distribution.

**Using GitHub CLI:**

```bash
# Create and push a tag
git tag -a v0.1.0 -m "Initial release - Multi-LLM consensus evaluation"
git push origin v0.1.0

# Create release
gh release create v0.1.0 \
  --title "v0.1.0 - Initial Release" \
  --notes "$(cat <<'EOF'
## 🎉 Initial Release

First stable release of AI Advisory!

### Features

- ✨ Query 8 AI models concurrently (ChatGPT, Claude, Gemini, DeepSeek, Qwen, Llama, Mistral, Kimi)
- 🔄 Two-level consensus system
- 🎨 Beautiful terminal UI with Rich
- ⚡ Async HTTP requests with httpx
- 🛡️ Robust error handling
- 📊 Interactive response selection

### Installation

**Homebrew (coming soon):**
\`\`\`bash
brew install ai-advisory
\`\`\`

**pip:**
\`\`\`bash
pip install ai-advisory
\`\`\`

**From source:**
\`\`\`bash
git clone https://github.com/YOURUSERNAME/ai-advisory.git
cd ai-advisory
pip install -e .
\`\`\`

### Quick Start

\`\`\`bash
export OPENROUTER_API_KEY=your-key
ai-advisory ask "What is the best programming language for beginners?"
\`\`\`

### What's Next

- [ ] PyPI distribution
- [ ] Homebrew tap
- [ ] Response caching
- [ ] Streaming support
- [ ] Additional models

EOF
)"
```

**Using GitHub Web Interface:**

1. Go to `Releases` → `Create a new release`
2. Tag version: `v0.1.0`
3. Release title: `v0.1.0 - Initial Release`
4. Copy the notes from above
5. Click `Publish release`

---

### 5. Update Formula SHA256

After creating the release, get the tarball SHA256:

```bash
# Download release tarball
curl -L https://github.com/YOURUSERNAME/ai-advisory/archive/refs/tags/v0.1.0.tar.gz -o v0.1.0.tar.gz

# Calculate SHA256
shasum -a 256 v0.1.0.tar.gz

# Clean up
rm v0.1.0.tar.gz
```

Update `Formula/ai-advisory.rb` with:
- Replace `YOURUSERNAME` with your GitHub username
- Add the SHA256 hash to the formula

```bash
# Edit the formula
nano Formula/ai-advisory.rb

# Commit and push
git add Formula/ai-advisory.rb
git commit -m "Update Homebrew formula with release SHA256"
git push
```

---

### 6. Set Up Homebrew Tap (Optional but Recommended)

Create a separate tap repository for easier installation:

```bash
# Create tap repository
gh repo create homebrew-ai-advisory --public \
  --description="Homebrew tap for AI Advisory"

# Clone the tap
cd ..
git clone https://github.com/YOURUSERNAME/homebrew-ai-advisory.git
cd homebrew-ai-advisory

# Copy formula
cp ../ai-advisory/Formula/ai-advisory.rb ./
git add ai-advisory.rb
git commit -m "Add AI Advisory formula"
git push

# Now users can install with:
# brew tap YOURUSERNAME/ai-advisory
# brew install ai-advisory
```

---

### 7. Create GitHub Actions (Optional)

Create `.github/workflows/test.yml` for CI/CD:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, macos-latest, windows-latest]
        python-version: ['3.10', '3.11', '3.12']

    steps:
    - uses: actions/checkout@v4

    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -e .

    - name: Test CLI
      run: |
        ai-advisory --help
```

---

### 8. Publish to PyPI (Optional)

For `pip install ai-advisory` to work globally:

```bash
# Install build tools
pip install build twine

# Build package
python -m build

# Test upload to TestPyPI first
python -m twine upload --repository testpypi dist/*

# If successful, upload to PyPI
python -m twine upload dist/*
```

---

### 9. Add Repository Badges

Update `README.md` to include your actual GitHub username:

```markdown
[![GitHub stars](https://img.shields.io/github/stars/YOURUSERNAME/ai-advisory?style=social)](https://github.com/YOURUSERNAME/ai-advisory)
[![GitHub forks](https://img.shields.io/github/forks/YOURUSERNAME/ai-advisory?style=social)](https://github.com/YOURUSERNAME/ai-advisory/fork)
[![GitHub issues](https://img.shields.io/github/issues/YOURUSERNAME/ai-advisory)](https://github.com/YOURUSERNAME/ai-advisory/issues)
[![GitHub release](https://img.shields.io/github/v/release/YOURUSERNAME/ai-advisory)](https://github.com/YOURUSERNAME/ai-advisory/releases)
```

---

### 10. Create Community Files

GitHub will prompt you to add:

- **Code of Conduct:** Use GitHub's default
- **Security Policy:** Create `SECURITY.md`
- **Support:** Enable Discussions

---

## 📝 Post-Setup Checklist

After completing the setup:

- [ ] Repository is public
- [ ] All code is pushed to main branch
- [ ] v0.1.0 release created with notes
- [ ] Topics added to repository
- [ ] Repository description set
- [ ] Issues enabled
- [ ] Discussions enabled (optional)
- [ ] Homebrew formula updated with correct SHA256
- [ ] Homebrew tap created (optional)
- [ ] README badges updated with your username
- [ ] Social preview image added (Settings → Social preview)

---

## 🎯 Making It Discoverable

### 1. Share on Social Media

**Twitter/X:**
```
🚀 Just released AI Advisory - a CLI tool that queries 8 AI models
simultaneously and generates consensus answers!

✨ ChatGPT + Claude + Gemini + DeepSeek + more
🔄 Two-level consensus evaluation
⚡ Beautiful terminal UI

Check it out: https://github.com/YOURUSERNAME/ai-advisory

#AI #LLM #OpenSource #CLI
```

**Reddit:**
- r/Python
- r/commandline
- r/MachineLearning
- r/ArtificialIntelligence

**Hacker News:**
- Submit with title: "AI Advisory – Query multiple LLMs and get consensus answers"

### 2. Add to Lists

- [Awesome CLI Apps](https://github.com/agarrharr/awesome-cli-apps)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [Awesome AI Tools](https://github.com/mahseema/awesome-ai-tools)

### 3. Write Blog Post

Share on:
- Dev.to
- Medium
- Your personal blog
- Hashnode

---

## 🔄 Updating the Repository

When making updates:

```bash
# Make changes
git add .
git commit -m "feat: add new feature"
git push

# Create new release
git tag -a v0.2.0 -m "Version 0.2.0"
git push origin v0.2.0
gh release create v0.2.0 --title "v0.2.0" --notes "Release notes here"

# Update Homebrew formula if needed
```

---

## 📊 Analytics & Insights

Track your repository's growth:

- **Stars:** Repository popularity
- **Forks:** Active contributors
- **Issues:** User engagement
- **Traffic:** Settings → Insights → Traffic
- **Contributors:** Settings → Insights → Contributors

---

## ✅ Your Repository is Ready!

The AI Advisory repository is now:

✅ Professionally documented
✅ Easy to install (multiple methods)
✅ Well-structured for contributions
✅ Ready for PyPI distribution
✅ Set up for Homebrew installation
✅ Optimized for discoverability

**Next:** Push your code to GitHub and share it with the world! 🎉
