# Usage Guide

Structorex operates directly from your command line. Navigate to your project folder to get started.

## Basic Scan

```bash
structorex
```
This generates a `project_report.txt` with a visual tree and file contents.

## Export Formats

**Markdown** (Ideal for LLMs):
```bash
structorex . --format markdown --output context.md
```

**Interactive HTML**:
```bash
structorex . --format html --output report.html
```

**JSON Data**:
```bash
structorex . --format json --output data.json
```

## ZIP Snapshot
Create a filtered `.zip` backup of your source code:
```bash
structorex . --export-zip clean-source.zip
```

## Configuration File
You can save preferences in `.structorex.yaml`:
```yaml
format: markdown
output: summary.md
exclude:
  - tests
max_size: 5
```
