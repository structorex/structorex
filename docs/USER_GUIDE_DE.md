# Structorex - Das offizielle Benutzerhandbuch 🚀

Willkommen bei **Structorex**! Dieses Tool hilft dir, sekundenschnell komplette Quellcode-Projekte einzulesen, deren Dateistruktur zu visualisieren und die Inhalte sicher und sauber zu exportieren. 

Perfekt, um den eigenen Code an KI-Modelle (wie ChatGPT, Claude) zu übergeben oder um Projektdokumentationen zu erstellen.

---

## 🛠️ Installation

Stelle sicher, dass du Python 3.8 oder höher installiert hast.
Installiere das Tool ganz einfach global auf deinem System:

```bash
pip install structorex
```

---

## 📖 1. Der schnelle Einstieg

Öffne dein Terminal und navigiere in den Ordner deines Projekts. Führe einfach diesen Befehl aus:

```bash
structorex
```

**Was passiert?**
1. Structorex durchsucht alle Ordner und Dateien.
2. Es ignoriert automatisch unwichtige Dateien (Bilder, `.git`, `node_modules`).
3. Es filtert automatisch sensible Daten (`.env`, `id_rsa`).
4. Es erstellt eine Datei namens `project_report.txt`, die oben einen sauberen Dateibaum und unten den kompletten Code enthält.

Wenn du ein anderes Verzeichnis scannen willst, ohne dorthin zu navigieren:
```bash
structorex C:\Pfad\zu\meinem\projekt
```

---

## 🤖 2. Code an ChatGPT & Co. übergeben (Markdown)

KIs lesen am besten **Markdown** (`.md`). Structorex hat dafür einen extra Modus, der deinen Code mit echtem Syntax-Highlighting formatiert.

```bash
structorex . --format markdown --output mein_ki_prompt.md
```
Du kannst nun die Datei `mein_ki_prompt.md` öffnen, alles kopieren (Strg+A, Strg+C) und direkt in dein KI-Fenster einfügen. Die KI versteht dadurch sofort dein gesamtes Projekt!

---

## 🌐 3. Der interaktive HTML-Bericht

Möchtest du dir dein Projekt lieber selbst übersichtlich im Browser anschauen? Generiere eine interaktive Webseite:

```bash
structorex . --format html --output projekt.html
```
Öffne die `projekt.html` mit einem Doppelklick. Du hast nun links ein anklickbares Inhaltsverzeichnis. Klickst du auf eine Datei, erscheint der Code auf der rechten Seite!

---

## 📦 4. Quellcode als saubere ZIP-Datei sichern

Oft möchte man Quellcode verschicken, aber ohne den ganzen Müll (`node_modules`, `.git`, kompilierte Dateien, Passwörter). Structorex kann dir direkt ein sauberes, gefiltertes Backup erstellen:

```bash
structorex . --export-zip clean_code.zip
```
Das Resultat ist eine kleine, saubere ZIP-Datei, die nur deinen echten Code enthält.

---

## 🛡️ 5. Was wird eigentlich gefiltert?

Structorex ist schlau. Es überspringt standardmäßig Dateien, die du nicht in deinem Report haben willst:
1. **`.gitignore`**: Alles, was in deiner `.gitignore` steht, wird ignoriert.
2. **Secrets**: Dateien wie `.env`, `secrets.json`, `.pem` werden aus Sicherheitsgründen **immer blockiert**.
3. **Große Dateien**: Dateien über 10 MB werden übersprungen (lässt sich mit `--max-size 50` ändern).
4. **Binärdateien**: Bilder, Videos, `.exe` oder PDFs werden ignoriert.

Wenn du bestimmte Ordner **zusätzlich** ausschließen willst:
```bash
structorex . --exclude frontend/build docs tests
```

---

## ⚙️ 6. Dauerhafte Projekt-Konfiguration

Wenn du in einem Projekt immer die gleichen Einstellungen nutzt (z.B. immer HTML-Export, immer Ordner X ausschließen), musst du das nicht jedes Mal neu eintippen.

Erstelle einfach eine Datei namens `.structorex.yaml` im Ordner:

```yaml
format: html
output: dokumentation.html
exclude:
  - tests
  - altes_backend
max_size: 5
```
Wenn du nun im Terminal einfach nur `structorex` eingibst, lädt das Tool automatisch diese Einstellungen!

*(Hinweis: Falls du Python-Entwickler bist, kannst du das stattdessen auch in deine `pyproject.toml` unter `[tool.structorex]` schreiben).*

---

## 🛟 7. Hilfe & alle Befehle anzeigen

Wenn du mal nicht weiterweißt, lass dir einfach die Hilfeseite im Terminal anzeigen:

```bash
structorex --help
```

Viel Spaß mit Structorex! 🚀
