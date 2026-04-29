# Mitwirken bei Structorex

Zunächst einmal vielen Dank, dass du in Erwägung ziehst, zu Structorex beizutragen! Es sind Leute wie du, die Structorex zu einem so großartigen Werkzeug machen.

## Wie du helfen kannst

### 1. Einen Fehler melden oder ein Feature anfragen
Wenn du einen Fehler findest oder eine Idee für eine neue Funktion hast, öffne bitte ein Issue auf GitHub. Füge so viele Details wie möglich hinzu:
- Schritte zur Reproduktion des Fehlers
- Erwartetes Verhalten vs. tatsächliches Verhalten
- Dein Betriebssystem und deine Python-Version

### 2. Einen Pull Request einreichen
Wenn du einen Fehler beheben oder selbst ein Feature hinzufügen möchtest:
1. Forke das Repository und klone es lokal.
2. Erstelle einen neuen Branch für dein Feature (`git checkout -b feature/tolles-feature`).
3. Nimm deine Änderungen vor und füge, wenn möglich, Tests hinzu.
4. Führe Tests und Linting durch (`pytest`, `ruff`, `mypy`).
5. Committe deine Änderungen mit einer klaren und beschreibenden Commit-Nachricht.
6. Pushe deinen Branch und öffne einen Pull Request.

## Entwicklungs-Setup

1. Repository klonen:
   ```bash
   git clone https://github.com/yourusername/structorex.git
   cd structorex
   ```
2. Im Entwicklermodus mit Entwickler-Abhängigkeiten installieren:
   ```bash
   pip install -e .[dev]
   ```
3. Die Test-Suite ausführen, um sicherzustellen, dass alles funktioniert:
   ```bash
   pytest
   ```

## Coding-Richtlinien
- Befolge den **PEP 8** Standard für Python-Code.
- Schreibe Docstrings für alle öffentlichen Klassen, Methoden und Funktionen.
- Füge Type Hints für eine bessere Wartbarkeit hinzu.
- Achte auf die Performance (nutze Generatoren, Threading, etc. wo es Sinn macht).

Vielen Dank für deine Unterstützung!
