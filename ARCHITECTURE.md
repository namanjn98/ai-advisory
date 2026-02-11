# 🏗️ Architecture Overview

Detailed architecture and design decisions for AI Advisory.

## 📊 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Terminal                         │
└─────────────────────────────────┬───────────────────────────┘
                                  │
                                  │ CLI Command
                                  ▼
┌─────────────────────────────────────────────────────────────┐
│                      cli.py (Typer App)                      │
│  • Parse arguments                                           │
│  • Validate token                                            │
│  • Orchestrate workflow                                      │
└─────────┬───────────────────────────────────────────┬───────┘
          │                                           │
          │ Level 1                                   │ Level 2
          ▼                                           ▼
┌─────────────────────────┐              ┌─────────────────────────┐
│   models.query_all()    │              │   prompts.build_meta()  │
│  • Async HTTP calls     │              │  • Bundle responses     │
│  • Concurrent execution │              │  • Generate meta-prompt │
│  • Error handling       │              │                         │
└──────────┬──────────────┘              └───────────┬─────────────┘
           │                                         │
           │                                         │
           ▼                                         ▼
┌─────────────────────────────────────────────────────────────┐
│                    OpenRouter API                            │
│                https://openrouter.ai/api                     │
└──────┬──────────┬──────────┬──────────┬──────────┬──────────┘
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
    ┌───┐      ┌───┐      ┌───┐      ┌───┐      ┌───┐
    │GPT│      │CLU│      │GEM│      │DEE│ ...  │KIM│
    └───┘      └───┘      └───┘      └───┘      └───┘
       │          │          │          │          │
       └──────────┴──────────┴──────────┴──────────┘
                          │
                          │ Responses
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                  display.py (Rich UI)                        │
│  • Format responses as panels                                │
│  • Show spinners during API calls                            │
│  • Handle user input for selection                           │
│  • Color-code success/error states                           │
└─────────────────────────────────────────────────────────────┘
                          │
                          │ Visual Output
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                        User Terminal                         │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 1. ChatGPT (2.3s)                                   │    │
│  │ Response content...                                 │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                              │
│  Select responses: 1,3,5 ──────────────────────────────────►│
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │ 1. ChatGPT Evaluation (3.1s)                        │    │
│  │ Rating: 8/10, Agreement: ..., Consensus: ...        │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Core Components

### 1. `cli.py` - Main Application

**Responsibilities:**
- Parse command-line arguments with Typer
- Validate and resolve API token
- Orchestrate the two-level workflow
- Handle user interaction

**Key Functions:**
- `ask()`: Main command handler
- Token resolution from env or flag
- Response selection prompt

**Design Decisions:**
- Used Typer for clean CLI with auto-generated help
- Single command (`ask`) keeps interface simple
- Synchronous orchestration with async API calls

---

### 2. `models.py` - API Communication

**Responsibilities:**
- Async HTTP requests to OpenRouter
- Concurrent model querying
- Error handling and timeout management
- Response parsing

**Key Functions:**
- `query_model()`: Single model query with error handling
- `query_all_models()`: Parallel execution with `asyncio.gather()`

**Design Decisions:**
- httpx for async HTTP (better than requests for concurrency)
- Individual try/except per model (failures don't cascade)
- 60-second timeout per request
- Structured response format (success, content, elapsed time)

**Error Handling:**
```python
try:
    # API call
except httpx.TimeoutException:
    # Timeout-specific error
except httpx.HTTPStatusError:
    # HTTP error with status code
except Exception:
    # Catch-all for unexpected errors
```

---

### 3. `prompts.py` - Meta-Prompt Generation

**Responsibilities:**
- Build Level 2 consensus evaluation prompts
- Format responses for evaluation
- Structure evaluation criteria

**Key Functions:**
- `build_meta_prompt()`: Creates comprehensive evaluation prompt

**Prompt Structure:**
```
Original Query: [user question]

Responses:
  1. [Model A response]
  2. [Model B response]
  ...

Evaluation Criteria:
  - Ratings (1-10)
  - Agreement analysis
  - Disagreement analysis
  - Pros & cons
  - Consensus answer
```

**Design Decisions:**
- Explicit evaluation criteria for consistent results
- Numbered responses for easy reference
- Includes original query for context

---

### 4. `display.py` - User Interface

**Responsibilities:**
- Rich terminal UI rendering
- Spinner animations during API calls
- Color-coded response panels
- User input handling

**Key Functions:**
- `display_response()`: Level 1 response panels (green/red)
- `display_evaluation()`: Level 2 evaluation panels (magenta)
- `get_selection()`: Interactive response selection
- `show_spinner()`: Loading animations

**Visual Elements:**
```python
# Green panel for success
Panel(content, border_style="green", title="1. ChatGPT (2.3s)")

# Red panel for errors
Panel(error, border_style="red", title="1. ChatGPT - ERROR")

# Magenta for evaluations
Panel(eval, border_style="magenta", title="1. ChatGPT Evaluation")
```

**Design Decisions:**
- Rich library for beautiful terminal output
- Color coding for quick visual scanning
- Elapsed time helps users understand performance
- Flexible selection (numbers or 'all')

---

### 5. `config.py` - Configuration

**Responsibilities:**
- Model registry (8 models with OpenRouter IDs)
- API endpoint configuration
- Token resolution logic

**Model Registry:**
```python
MODELS = [
    {"name": "ChatGPT", "id": "openai/gpt-4.1"},
    {"name": "Gemini", "id": "google/gemini-2.5-flash"},
    # ... 8 total
]
```

**Design Decisions:**
- Centralized model configuration
- Easy to add/remove models
- Name + ID mapping for display and API
- Token fallback: flag → env var → error

---

## 🔄 Data Flow

### Level 1: Initial Query

```
1. User Input
   ↓
2. Token Resolution
   ↓
3. Create Messages Array: [{"role": "user", "content": query}]
   ↓
4. Async Query All Models (concurrent)
   ↓
5. Parse Responses (success/error for each)
   ↓
6. Display All Responses as Panels
   ↓
7. User Selects Responses (interactive)
```

### Level 2: Consensus Evaluation

```
1. Filter Selected Responses (successful only)
   ↓
2. Build Meta-Prompt with Selected Responses
   ↓
3. Create Meta-Messages Array
   ↓
4. Async Query All Models Again (concurrent)
   ↓
5. Parse Evaluations
   ↓
6. Display All Evaluations as Panels
```

---

## 🚀 Performance Characteristics

### Concurrency Model

- **Async I/O**: All API calls use asyncio
- **Parallel Execution**: `asyncio.gather()` for simultaneous requests
- **No Retries**: Failed requests fail fast (no doubled costs)

### Timing

Typical execution times:

| Operation | Time |
|-----------|------|
| Single model query | 1-5 seconds |
| Level 1 (8 concurrent) | 2-6 seconds |
| Level 2 (8 concurrent) | 3-8 seconds |
| Total workflow | 5-15 seconds |

### Resource Usage

- **Memory**: Minimal (<50MB typical)
- **Network**: 8 concurrent HTTP requests
- **CPU**: Low (I/O bound, not CPU bound)

---

## 🔒 Security Considerations

### API Token Handling

- Never logged or displayed
- Environment variable preferred
- Flag option for flexibility
- Clear error if missing

### Input Validation

- User queries: No validation (sent as-is to models)
- Selection input: Validated range and format
- Token: Basic presence check

### Error Information

- API errors shown to user (for debugging)
- No sensitive data in error messages
- Detailed HTTP status codes included

---

## 🎨 Design Patterns

### 1. **Async/Await Pattern**

```python
async def query_model(...):
    async with httpx.AsyncClient() as client:
        response = await client.post(...)
```

**Why:** Enables concurrent API calls without threads

### 2. **Structured Response Pattern**

```python
{
    "success": True/False,
    "name": "Model Name",
    "content": "...",
    "elapsed": 2.3,
    "error": "..." (if failed)
}
```

**Why:** Consistent interface for both success and failure

### 3. **Separation of Concerns**

- CLI orchestration (cli.py)
- API communication (models.py)
- Prompt generation (prompts.py)
- UI rendering (display.py)
- Configuration (config.py)

**Why:** Each module has single responsibility

### 4. **Fail-Fast with Graceful Degradation**

```python
try:
    result = await query_model()
except Exception as e:
    # Return error structure, don't crash
    return {"success": False, "error": str(e)}
```

**Why:** One model failure doesn't affect others

---

## 📦 Dependencies

### Direct Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| typer | CLI framework | >=0.9 |
| httpx | Async HTTP | >=0.25 |
| rich | Terminal UI | >=13.0 |

### Transitive Dependencies

- click (via typer) - CLI utilities
- anyio (via httpx) - Async compatibility
- certifi (via httpx) - SSL certificates
- h11 (via httpx) - HTTP/1.1 protocol

**Total Size:** ~5MB installed

---

## 🔄 Extension Points

### Adding New Models

```python
# In config.py
MODELS.append({
    "name": "NewModel",
    "id": "provider/model-id"
})
```

### Custom Prompts

```python
# In prompts.py
def build_custom_prompt(query, responses):
    # Custom prompt logic
    return prompt
```

### Alternative Display

```python
# Create new display function
def display_json(responses):
    import json
    print(json.dumps(responses, indent=2))
```

### Caching Layer

```python
# Add to models.py
CACHE = {}

async def query_model_cached(model_id, messages):
    cache_key = hash((model_id, str(messages)))
    if cache_key in CACHE:
        return CACHE[cache_key]
    result = await query_model(model_id, messages)
    CACHE[cache_key] = result
    return result
```

---

## 🧪 Testing Strategy

### Unit Tests (Future)

- `test_config.py`: Token resolution logic
- `test_prompts.py`: Meta-prompt generation
- `test_models.py`: Response parsing (mocked API)

### Integration Tests (Future)

- End-to-end workflow with mock API
- Error handling scenarios
- User input validation

### Manual Testing

Current approach:
1. Test with real API (small queries to minimize cost)
2. Verify all 8 models respond
3. Test error scenarios (invalid token, network errors)
4. Test selection logic (numbers, 'all', invalid input)

---

## 📈 Future Improvements

### Performance

- [ ] Response streaming for real-time output
- [ ] Caching to reduce API costs
- [ ] Parallel Level 1 and Level 2 (pipeline)

### Features

- [ ] Model selection (subset of 8)
- [ ] Custom evaluation criteria
- [ ] Export results (JSON/Markdown)
- [ ] History tracking
- [ ] Configuration file

### User Experience

- [ ] Interactive TUI (textual)
- [ ] Response comparison view
- [ ] Progress bars per model
- [ ] Syntax highlighting for code responses

### Infrastructure

- [ ] Unit tests
- [ ] CI/CD pipeline
- [ ] Docker image
- [ ] Pre-commit hooks

---

## 🎯 Architectural Decisions

### Why OpenRouter?

- ✅ Single API for multiple providers
- ✅ Unified pricing and billing
- ✅ OpenAI-compatible interface
- ✅ No need for multiple API keys

### Why Async Instead of Threads?

- ✅ Better for I/O-bound operations
- ✅ More efficient resource usage
- ✅ Cleaner error handling
- ✅ Python async ecosystem maturity

### Why No Database?

- ✅ Simple CLI tool
- ✅ Stateless operation
- ✅ Easier installation
- ❓ May add optional caching later

### Why Rich Instead of Click?

- ✅ Beautiful colored output
- ✅ Panels, tables, progress bars
- ✅ Better user experience
- ✅ Works well with Typer (uses click underneath)

### Why No Retries?

- ✅ Avoid doubled API costs
- ✅ Faster failure feedback
- ✅ User can retry entire query if needed
- ❓ May add optional retry with exponential backoff

---

## 📐 Code Metrics

### Lines of Code

| File | Lines | Purpose |
|------|-------|---------|
| cli.py | ~80 | Main application |
| models.py | ~70 | API communication |
| prompts.py | ~40 | Prompt generation |
| display.py | ~90 | UI rendering |
| config.py | ~30 | Configuration |
| **Total** | **~310** | Core functionality |

### Complexity

- **Cyclomatic Complexity**: Low (mostly linear flow)
- **Dependency Depth**: 1 level (no nested dependencies)
- **Function Size**: Small (10-40 lines average)

---

This architecture prioritizes:
- **Simplicity**: Easy to understand and modify
- **Reliability**: Robust error handling
- **Performance**: Concurrent API calls
- **User Experience**: Beautiful terminal output
- **Extensibility**: Easy to add models/features
