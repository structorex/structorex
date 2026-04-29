# API Reference

Structorex is primarily a CLI tool, but its internal modules can be used programmatically.

## Core Modules

- `structorex.core.builder.ProjectBuilder`: Traverses directories and builds the AST-like tree of nodes.
- `structorex.core.filter.FileFilter`: Handles `.gitignore` path matching, mime-type detection, and security rules.
- `structorex.core.visitor.ProjectStructureVisitor`: Traverses the tree and queues files for parallel reading using `tqdm` and `ThreadPoolExecutor`.
- `structorex.writers`: Contains classes `TextReportWriter`, `MarkdownReportWriter`, `JsonReportWriter`, and `HtmlReportWriter` to generate outputs.
