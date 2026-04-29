# Руководство пользователя

Structorex работает прямо в терминале. Перейдите в папку вашего проекта, чтобы начать.

## Простое сканирование

```bash
structorex
```
Создаст `project_report.txt` с деревом и содержимым файлов.

## Форматы экспорта

**Markdown** (Идеально для ИИ/LLM):
```bash
structorex . --format markdown --output context.md
```

**Интерактивный HTML**:
```bash
structorex . --format html --output report.html
```

**JSON-данные**:
```bash
structorex . --format json --output data.json
```

## ZIP-снимок
Создайте отфильтрованную `.zip` копию исходного кода:
```bash
structorex . --export-zip clean-source.zip
```

## Файл конфигурации
Сохраняйте настройки в `.structorex.yaml`:
```yaml
format: markdown
output: summary.md
exclude:
  - tests
max_size: 5
```
