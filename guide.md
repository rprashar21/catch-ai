# UV Package Manager Guide

## What is UV?

**UV** is a fast Python package manager written in Rust. It's like `npm` for Node.js or `maven` for Java, but **10-100x faster** than traditional Python tools.

### Benefits:
- ⚡ **Fast** - Resolves dependencies in milliseconds
- 🔒 **Reliable** - Lock files ensure reproducible builds
- 🎯 **All-in-one** - Replaces `pip`, `virtualenv`, and `poetry`
- 📦 **Modern** - Uses `pyproject.toml` standard

---

## Python Virtual Environment (venv)

### What is it?
A **virtual environment** is an isolated Python environment that keeps project dependencies separate.

### How it works:
- Each project gets its own `.venv/` folder
- Contains isolated Python and packages
- Prevents dependency conflicts
- Similar to Java's classpath isolation

### UV manages it automatically:
- Creates `.venv/` when you run `uv sync`
- No manual activation needed
- Use `uv run` to execute in the correct environment

---

## Comparison with Spring Boot

| Feature | Spring Boot | UV (Python) |
|---------|-------------|-------------|
| **Init** | Spring Initializr | `uv init` |
| **Config** | `pom.xml` | `pyproject.toml` |
| **Lock File** | `pom.xml.lock` | `uv.lock` |
| **Install** | `mvn install` | `uv sync` |
| **Run** | `mvn spring-boot:run` | `uv run uvicorn ...` |

---

## Quick Start

### 1. Create Project
```bash
uv init fastpi-projects
cd fastpi-projects
```

### 2. Add Dependencies
```bash
uv add fastapi
uv add "uvicorn[standard]"
uv add --dev pytest httpx
```

### 3. Install Dependencies
```bash
uv sync
```

### 4. Run Application
```bash
# Start server
uv run uvicorn app.main:app --reload

# Run tests
uv run pytest
```

---

## Common Commands

```bash
# Check Python location
uv run which python

# List packages
uv pip list

# Update dependencies
uv sync --upgrade

# Remove package
uv remove package-name
```

---

## Running the Server

```bash
uv run uvicorn app.main:app --reload
```

**Access:**
- API: http://127.0.0.1:8000
- Docs: http://127.0.0.1:8000/docs
- Health: http://127.0.0.1:8000/health

---

## IDE Setup

1. Find interpreter: `uv run which python`
2. In VS Code/Cursor: `Cmd+Shift+P` → "Python: Select Interpreter"
3. Choose: `.venv/bin/python`

---

## Summary

UV = Fast dependencies + Auto venv + Modern Python workflow

Just like Spring Boot simplifies Java, UV simplifies Python! 🚀

