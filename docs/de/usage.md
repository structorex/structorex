# Benutzerhandbuch

Structorex wird direkt im Terminal ausgeführt. Navigiere in dein Projekt, um loszulegen.

## Einfacher Scan

```bash
structorex
```
Erstellt eine `project_report.txt` mit Baum und Inhalten.

## Exportformate

**Markdown** (Ideal für ChatGPT/LLMs):
```bash
structorex . --format markdown --output context.md
```

**Interaktives HTML**:
```bash
structorex . --format html --output report.html
```

**JSON Daten**:
```bash
structorex . --format json --output data.json
```

## ZIP Snapshot
Ein gefiltertes ZIP-Backup deines Quellcodes:
```bash
structorex . --export-zip clean-source.zip
```

## Konfigurationsdatei
Speichere Einstellungen in `.structorex.yaml`:
```yaml
format: markdown
output: summary.md
exclude:
  - tests
max_size: 5
```
