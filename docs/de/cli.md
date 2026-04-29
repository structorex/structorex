# CLI Referenz

Alle verfügbaren Kommandozeilen-Argumente im Überblick.

```text
usage: structorex [-h] [-o OUTPUT] [-f {text,json,markdown,html}] [-e [EXCLUDE ...]] [-a [ALLOWED ...]] [-m MAX_SIZE] [-v] [-s] [-z EXPORT_ZIP] [path]
```

### Argumente
- `path` (Optional): Das zu scannende Verzeichnis. Standard ist das aktuelle Verzeichnis (`.`).
- `-o, --output`: Name der Ausgabedatei. Standard: `project_report.txt`.
- `-f, --format`: Format. Auswahl: `text`, `markdown`, `json`, `html`.
- `-e, --exclude`: Zusätzliche Ordner ignorieren (z.B. `docs` `tests`).
- `-a, --allowed`: Spezifische Dateiendungen erlauben (z.B. `.py` `.txt`).
- `-m, --max-size`: Maximale Dateigröße in MB. Standard: 10.
- `-v, --verbose`: Erweitertes Logging aktivieren.
- `-s, --show-skipped`: Übersprungene Dateien im Baum anzeigen.
- `-z, --export-zip`: Ein ZIP-Archiv anstelle/zusätzlich zum Report erstellen.
