# Справочник по API

Structorex — это в первую очередь инструмент CLI, но его модули можно использовать и программно.

## Основные модули

- `structorex.core.builder.ProjectBuilder`: Обходит каталоги и строит дерево узлов.
- `structorex.core.filter.FileFilter`: Обрабатывает `.gitignore`, MIME-типы и правила безопасности.
- `structorex.core.visitor.ProjectStructureVisitor`: Обходит дерево и ставит файлы в очередь на параллельное чтение (`ThreadPoolExecutor`).
- `structorex.writers`: Содержит классы форматирования (`TextReportWriter`, `MarkdownReportWriter` и др.).
