# CLI Reference

Structorex provides a flexible command-line interface.

```text
usage: structorex [-h] [-o OUTPUT] [-f {text,json,markdown,html}] [-e [EXCLUDE ...]] [-a [ALLOWED ...]] [-m MAX_SIZE] [-v] [-s] [-z EXPORT_ZIP] [path]
```

### Arguments
- `path` (Optional): The directory to scan. Defaults to the current directory (`.`).
- `-o, --output`: Name of the output file. Default is `project_report.txt`.
- `-f, --format`: Output format. Choices: `text`, `markdown`, `json`, `html`.
- `-e, --exclude`: Additional directories to exclude (e.g. `docs` `tests`).
- `-a, --allowed`: Specific file extensions to allow (e.g. `.py` `.txt`).
- `-m, --max-size`: Maximum file size in MB. Default: 10.
- `-v, --verbose`: Enable verbose logging.
- `-s, --show-skipped`: Show files skipped by filters in the tree.
- `-z, --export-zip`: Create a ZIP archive instead of/alongside a report.
