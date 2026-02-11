# Contributing to AI Advisory

Thank you for considering contributing to AI Advisory! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/ai-advisory.git
   cd ai-advisory
   ```
3. **Create a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install in development mode**:
   ```bash
   pip install -e .
   ```

## 🔧 Development Workflow

1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines

3. **Test your changes**:
   ```bash
   # Manual testing
   ai-advisory ask "Test question"

   # Verify no errors with different scenarios
   ai-advisory ask "Another test" --token custom_token
   ```

4. **Commit your changes**:
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Open a Pull Request** on GitHub

## 📝 Commit Message Guidelines

We follow conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `style:` Code style changes (formatting, etc.)
- `refactor:` Code refactoring
- `test:` Adding or updating tests
- `chore:` Maintenance tasks

Examples:
```
feat: add support for custom model selection
fix: handle network timeout errors gracefully
docs: update installation instructions
```

## 🎯 Areas for Contribution

### High Priority
- [ ] Add unit tests for all modules
- [ ] Add integration tests with mock API responses
- [ ] Implement response caching to reduce API costs
- [ ] Add streaming support for real-time responses
- [ ] Create configuration file support (`~/.ai-advisory.yaml`)

### Features
- [ ] Allow custom model selection (subset of 8)
- [ ] Export results to JSON/Markdown
- [ ] Add response comparison view (side-by-side)
- [ ] Interactive TUI mode with keyboard navigation
- [ ] Add support for image inputs (multimodal models)
- [ ] Template system for common queries
- [ ] History/favorites system

### Documentation
- [ ] Add video tutorial/demo
- [ ] Create example use cases
- [ ] Write API documentation
- [ ] Add troubleshooting guide
- [ ] Create development guide

### Infrastructure
- [ ] Set up CI/CD pipeline
- [ ] Add code coverage reporting
- [ ] Create Docker image
- [ ] Add pre-commit hooks
- [ ] Set up automated releases

## 🧪 Testing Guidelines

(Tests to be implemented)

```python
# Example test structure
def test_query_model_success():
    """Test successful model query"""
    pass

def test_query_model_timeout():
    """Test timeout handling"""
    pass

def test_meta_prompt_generation():
    """Test meta-prompt builder"""
    pass
```

## 📋 Code Style

- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Add docstrings for public functions
- Keep functions focused and small
- Use descriptive variable names

Example:
```python
async def query_model(
    model_id: str,
    model_name: str,
    messages: List[Dict[str, str]],
    token: str,
    timeout: int = 60,
) -> Dict[str, Any]:
    """Query a single model via OpenRouter API.

    Args:
        model_id: OpenRouter model identifier
        model_name: Human-readable model name
        messages: Chat messages in OpenAI format
        token: OpenRouter API token
        timeout: Request timeout in seconds

    Returns:
        Dictionary with success status and response data
    """
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to reproduce**: Exact steps to trigger the bug
3. **Expected behavior**: What should happen
4. **Actual behavior**: What actually happens
5. **Environment**:
   - OS and version
   - Python version
   - ai-advisory version
6. **Error messages**: Full error output if applicable

## 💡 Feature Requests

When requesting features:

1. **Use case**: Describe why you need this feature
2. **Proposed solution**: How you envision it working
3. **Alternatives**: Other approaches you've considered
4. **Additional context**: Any other relevant information

## 🤝 Code Review Process

All contributions go through code review:

1. Automated checks must pass (when implemented)
2. At least one maintainer review required
3. Address review feedback
4. Maintainer merges when approved

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Every contribution helps make AI Advisory better for everyone. We appreciate your time and effort!
