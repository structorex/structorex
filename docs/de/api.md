# API Referenz

Structorex ist primär ein CLI-Tool, aber die Module können auch im Code genutzt werden.

## Kernmodule

- `structorex.core.builder.ProjectBuilder`: Durchsucht Verzeichnisse und baut den Baum.
- `structorex.core.filter.FileFilter`: Behandelt `.gitignore`, Mime-Types und Security-Regeln.
- `structorex.core.visitor.ProjectStructureVisitor`: Traversiert den Baum und liest Dateien parallel über den `ThreadPoolExecutor`.
- `structorex.writers`: Beinhaltet die Writer-Klassen (`TextReportWriter`, `MarkdownReportWriter`, etc.) für die Ausgabe.
