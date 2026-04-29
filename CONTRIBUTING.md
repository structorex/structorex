# Contributing to Structorex

First off, thank you for considering contributing to Structorex! It's people like you that make Structorex such a great tool.

## How to Contribute

### 1. Report a Bug or Request a Feature
If you find a bug or have an idea for a new feature, please open an issue on GitHub. Include as much detail as possible:
- Steps to reproduce the bug
- Expected behavior vs actual behavior
- Your operating system and Python version

### 2. Submit a Pull Request
If you'd like to fix a bug or add a feature yourself:
1. Fork the repository and clone it locally.
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`).
3. Make your changes and add tests if applicable.
4. Run tests and linting (`pytest`, `ruff`, `mypy`).
5. Commit your changes with a clear and descriptive commit message.
6. Push your branch and open a Pull Request.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/structorex.git
   cd structorex
   ```
2. Install in editable mode with dev dependencies:
   ```bash
   pip install -e .[dev]
   ```
3. Run the test suite to ensure everything is working:
   ```bash
   pytest
   ```

## Coding Guidelines
- Follow **PEP 8** standard for Python code.
- Write docstrings for all public classes, methods, and functions.
- Add Type Hints for better maintainability.
- Keep performance in mind (use generators, lazy evaluation, threading where appropriate).

Thank you for your support!