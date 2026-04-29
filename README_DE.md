# Structorex

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/structorex/structorex/blob/master/LICENSE)

**Structorex** ist ein leistungsstarkes Kommandozeilen-Tool, das einen detaillierten Bericht über die Dateistruktur und die Inhalte deines Projekts erstellt. Es generiert eine visuelle Baumstruktur und bettet den Quellcode der Dateien direkt in den Bericht ein. Ideal für die Kontext-Erstellung für LLMs (Künstliche Intelligenz), Projektübergaben und Dokumentation.

## ✨ Funktionen

- 🌳 **Visuelle Baumstruktur:** Übersichtliche Darstellung der Verzeichnishierarchie.
- 📄 **Inhalts-Inspektion:** Quellcode und Textinhalte werden direkt im Bericht angezeigt.
- ⚙️ **Modernes CLI:** Vollständig über Kommandozeilen-Parameter konfigurierbar.
- 🔒 **Sicherheits-Scanner:** Überspringt standardmäßig sensible Dateien wie `.env`, `id_rsa`, `.pem` oder `secrets.*`.
- 🚦 **Native `.gitignore` Unterstützung:** Ignoriert mithilfe von `pathspec` automatisch alles, was auch in Git ignoriert wird.
- 📝 **Vielseitige Formate:** Export als Text, Markdown, JSON oder interaktives HTML.
- 📦 **ZIP-Snapshot Export:** Erstellt ein sauberes ZIP-Archiv deines Projekts (ohne ignorierte Dateien).
- 🔣 **Smarte Codierung:** Erkennt Text-Codierungen (UTF-8, ISO-8859-1, etc.) automatisch dank `charset-normalizer`.
- ⚡ **Hohe Performance:** Paralleles Einlesen (`ThreadPoolExecutor`) mit dynamischem Fortschrittsbalken (`tqdm`).
- 🛡️ **Binär-Filterung:** Überspringt automatisch Bilder, Audio, Video und andere Binärdateien.

## 🚀 Installation

Direkt von PyPI installieren (Empfohlen):
```bash
pip install structorex
```

Oder aus dem Quellcode installieren:
```bash
git clone https://github.com/yourusername/structorex.git
cd structorex
pip install -e .
```

## 💻 Nutzung

### Standard-Befehle

Analysiert das aktuelle Verzeichnis und erstellt einen einfachen Textbericht:
```bash
structorex
```

Einen **Markdown**-Bericht generieren (Ideal für LLMs oder GitHub):
```bash
structorex . --format markdown --output projekt_bericht.md
```

Einen **interaktiven HTML**-Bericht generieren (mit klickbarem Verzeichnisbaum):
```bash
structorex . --format html --output index.html
```

Einen sauberen **ZIP-Snapshot** des Codes erstellen:
```bash
structorex . --export-zip sauberer_code.zip
```

### Erweiterte Konfiguration

Structorex bietet viele Argumente zur Feinjustierung:
```bash
structorex /pfad/zum/projekt -o output.json -f json --exclude node_modules dist --max-size 5
```

**Verfügbare Optionen:**
- `-h`, `--help`: Hilfe anzeigen.
- `-o`, `--output`: Dateiname der Ausgabe (Standard: `project_report.txt`).
- `-f`, `--format`: Ausgabeformat wählen (`text`, `markdown`, `json`, `html`).
- `-e`, `--exclude`: Zusätzliche Ordner ignorieren.
- `-a`, `--allowed`: Liste erlaubter Dateiendungen überschreiben (z.B. `.py` `.txt`).
- `-m`, `--max-size`: Maximale Dateigröße in MB (Standard: 10 MB).
- `-v`, `--verbose`: Ausführliches Logging aktivieren.
- `-s`, `--show-skipped`: Übersprungene Dateien im Baum dennoch anzeigen (als "[skipped]").
- `-z`, `--export-zip`: Ein sauberes ZIP-Archiv ausgeben.

## ⚙️ Konfigurationsdateien

Statt jedes Mal Argumente einzutippen, lädt Structorex automatisch Einstellungen aus deinem Projektverzeichnis, wenn dort eine der folgenden Dateien existiert:

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

## 📁 Projektstruktur (Quellcode)

```text
structorex/
├── src/structorex/
│   ├── __init__.py
│   ├── cli.py          # CLI Einstiegspunkt
│   ├── config.py       # Konfiguration
│   ├── writers.py      # Output-Generierung (Text, JSON, Markdown, HTML)
│   ├── utils.py        # Utils & ZIP Export
│   └── core/
│       ├── builder.py  # Baum-Generator
│       ├── components.py # Dateisystem-Komponenten
│       ├── filter.py   # Security & Mime-Filter
│       └── visitor.py  # Report-Logik & Threading
├── tests/              # Tests
├── pyproject.toml
└── .gitignore
```

## 🤝 Mitwirken
Beiträge sind immer willkommen! Bitte lies unsere [CONTRIBUTING.md](https://github.com/structorex/structorex/blob/master/CONTRIBUTING_DE.md) für Details zu unserem Code of Conduct und dem Prozess für Pull Requests.

## 📜 Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert – siehe die [LICENSE](https://github.com/structorex/structorex/blob/master/LICENSE) Datei für Details.
