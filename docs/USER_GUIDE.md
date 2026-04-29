# Structorex - Official User Guide 🚀

Welcome to **Structorex**! This tool helps you instantly read entire source code projects, visualize their file structure, and securely export their contents.

It is perfect for providing context to AI models (like ChatGPT or Claude), generating project documentation, or creating clean source code backups.

---

## 🛠️ Installation

Ensure you have Python 3.8 or higher installed.
Install the tool globally on your system:

```bash
pip install structorex
```

---

## 📖 1. Quick Start

Open your terminal, navigate to your project directory, and run:

```bash
structorex
```

**What happens?**
1. Structorex scans all folders and files.
2. It automatically ignores non-essential files (images, `.git`, `node_modules`).
3. It securely filters out sensitive data (`.env`, `id_rsa`, `.pem`).
4. It creates a file named `project_report.txt` containing a clean file tree at the top and the complete source code at the bottom.

To scan a different directory without navigating to it:
```bash
structorex /path/to/my/project
```

---

## 🤖 2. Feed your code to AI / LLMs (Markdown)

AIs read **Markdown** (`.md`) best. Structorex has a dedicated mode that formats your code with proper syntax highlighting.

```bash
structorex . --format markdown --output my_ai_prompt.md
```
Open `my_ai_prompt.md`, copy everything (Ctrl+A, Ctrl+C), and paste it directly into your AI chat. The AI will instantly understand your entire project architecture!

---

## 🌐 3. Interactive HTML Reports

Prefer exploring your project directly in the browser? Generate an interactive webpage:

```bash
structorex . --format html --output project.html
```
Double-click `project.html` to open it. You'll see a clickable table of contents on the left. Click on any file, and its source code will appear on the right!

---

## 📦 4. Exporting a Clean ZIP Snapshot

Often you need to share source code, but without the clutter (`node_modules`, compiled files, passwords). Structorex can create a clean, filtered backup for you:

```bash
structorex . --export-zip clean_code.zip
```
The result is a small, pristine ZIP file containing only your actual source code.

---

## 🛡️ 5. What exactly is filtered?

Structorex is smart. By default, it skips files you don't want in your reports:
1. **`.gitignore`**: Anything listed in your `.gitignore` is skipped.
2. **Secrets**: Files like `.env`, `secrets.json`, `.pem` are **always blocked** for security.
3. **Large Files**: Files over 10 MB are skipped (change this with `--max-size 50`).
4. **Binary Files**: Images, videos, `.exe`, or PDFs are ignored automatically.

If you want to **additionally** exclude specific folders:
```bash
structorex . --exclude frontend/build docs tests
```

---

## ⚙️ 6. Persistent Configuration

If you consistently use the same settings in a project (e.g., always exporting HTML, always excluding folder X), you don't need to type the arguments every time.

Create a file named `.structorex.yaml` in your project folder:

```yaml
format: html
output: documentation.html
exclude:
  - tests
  - old_backend
max_size: 5
```
Now, simply typing `structorex` will automatically load these settings!

*(Note: Python developers can add this to their `pyproject.toml` under `[tool.structorex]` instead).*

---

## 🛟 7. Help & Command Reference

If you need a quick reminder, view the help page in the terminal:

```bash
structorex --help
```

Enjoy using Structorex! 🚀
