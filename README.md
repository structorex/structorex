# Structorex

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Structorex** is a powerful command-line tool that generates a detailed report of your project's file structure and file contents. It provides a visual representation of your directory hierarchy and allows you to inspect file contents directly within the generated report. Ideal for LLM context generation, project handovers, and documentation.

## ✨ Features

- 🌳 **Visual Tree Structure:** Generates a clear, visual representation of your directory structure.
- 📄 **Content Inspection:** Embeds the contents of text-based files directly into the report.
- ⚙️ **Powerful CLI:** Fully configurable via command-line arguments (`argparse` based).
- 🔒 **Security Scanning:** Automatically ignores sensitive files like `.env`, `id_rsa`, `.pem`, `.key`, and `secrets.*` by default.
- 🚦 **Native `.gitignore` Support:** Respects your project's `.gitignore` rules out of the box using `pathspec`.
- 📝 **Multiple Formats:** Export reports in Text, Markdown, JSON, or interactive HTML.
- 📦 **ZIP-Snapshot Export:** Create a clean ZIP archive of your filtered project files.
- 🔣 **Smart Encoding:** Automatically detects text encodings (UTF-8, ISO-8859-1, etc.) using `charset-normalizer`.
- ⚡ **High Performance:** Uses parallel file reading (`ThreadPoolExecutor`) and displays a progress bar (`tqdm`) for massive projects.
- 🛡️ **Binary Filtering:** Automatically skips images, audio, video, and other binary files using mime-type and size validation.

## 🚀 Installation

Install directly from PyPI (recommended):
```bash
pip install structorex
```

Or install from source:
```bash
git clone https://github.com/yourusername/structorex.git
cd structorex
pip install -e .
```

## 💻 Usage

### Basic Commands

Analyze the current directory and generate a simple text report:
```bash
structorex
```

Generate a **Markdown** report (great for reading on GitHub or passing to LLMs):
```bash
structorex . --format markdown --output project_report.md
```

Generate an **Interactive HTML** report:
```bash
structorex . --format html --output index.html
```

Create a **ZIP Snapshot** of your clean, filtered code:
```bash
structorex . --export-zip clean_source_code.zip
```

### Advanced Configuration

Structorex provides flexible command line arguments to tweak exactly what is scanned:
```bash
structorex /path/to/project -o output.json -f json --exclude node_modules dist --max-size 5
```

**Available Options:**
- `-h`, `--help`: Show the help message and exit.
- `-o`, `--output`: Specifies output filename (default: `project_report.txt`).
- `-f`, `--format`: Output format, choose from `text`, `markdown`, `json`, or `html`.
- `-e`, `--exclude`: Additional directories to exclude manually.
- `-a`, `--allowed`: Override allowed file extensions (e.g. `.py` `.txt`).
- `-m`, `--max-size`: Maximum file size in MB to read content (default 10 MB).
- `-v`, `--verbose`: Enable verbose logging.
- `-s`, `--show-skipped`: Show skipped files in the report tree instead of hiding them.
- `-z`, `--export-zip`: Create a clean ZIP archive of the filtered project files.

## ⚙️ Configuration Files

Instead of typing out all arguments every time, Structorex automatically loads settings from your project directory if you have one of the following files:

**`.structorex.yaml`**
```yaml
format: markdown
output: summary.md
exclude:
  - tests
  - docs
max_size: 2
```

**`pyproject.toml`**
```toml
[tool.structorex]
format = "json"
output = "analysis.json"
exclude = ["build", ".tox"]
```

It supports `.structorex.yaml`, `.structorex.json`, and `pyproject.toml`. Command-line arguments always override configuration file settings.

## 📁 Project Structure

```text
structorex/
├── src/structorex/
│   ├── __init__.py
│   ├── cli.py          # CLI entry point
│   ├── config.py       # Configuration and CLI arguments
│   ├── writers.py      # Output formatters (Text, JSON, Markdown, HTML)
│   ├── utils.py        # Logging, ZIP generation
│   └── core/
│       ├── builder.py  # Builds file system tree using scandir
│       ├── components.py # File system components
│       ├── filter.py   # File filtering and security scanner
│       └── visitor.py  # Report generation & Threading
├── tests/              # Test suite
├── pyproject.toml      # Project configuration
└── .gitignore
```

## 🤝 Contributing
Contributions are always welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.